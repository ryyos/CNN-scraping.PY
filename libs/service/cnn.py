import requests
import re

from pyquery import PyQuery
from requests import Response
from datetime import datetime
from time import time
from icecream import ic

from libs.utils.parser import HtmlParser
from libs.utils.logs import logger
from libs.utils.writer import Writer
from libs.utils.corrector import vname

# Class Cnn class utama yang di gunakan untuk mengambil data dari Cnn
class Cnn:
    def __init__(self) -> None:

        # mendlkarasikan Class HtmlParser() untuk memparser HTML dari file utils parser.py
        self.__parser = HtmlParser()

        # mendlkarasikan Class Writer() untuk menulis content kedalam file dari file utils writer.py
        self.__writer = Writer()
        
        # Domain utama dari website Cnn
        self.MAIN_DOMAIN = 'www.cnnindonesia.com'
    

    """ __filter_str()
    function untuk memfilter text yang masuk / untuk menghapus beberapa karakter anomali

    Params:
      text (str): text yang ingin di filter

    Returns:
      str: text hasil filter
    """
    def __filter_str(self, text: str) -> str:
        cleaned_text = text.replace('ADVERTISEMENT SCROLL TO CONTINUE WITH CONTENT', ' ') \
                           .replace('[Gambas:Video CNN]', '') \
                           .replace('/', ' ') \
                           .replace('\xa0k', ' ') \
                           .replace('\u00a0', '') \
                           .replace('\"', "'") \
                           .replace('\n', '') # maksudnya mengganti charakter '\n' menjadi ''
            
        return cleaned_text



    """ extract_data()
    function untuk mengextract / menentukan data apa yang ingin di ambil dari article website

    Params:
      url_article (str): url article / url card yang ingin di extract

    Returns:
      dict: dictionary yang berisi data yang telah di ambil
    """
    def extract_data(self, url_article: str) -> dict:

        # response adalah hasil dari request ke url_article
        response: Response = requests.get(url=url_article)

        # merubah response yang berupa HTML untuk di jadikan Pyquery
        html: PyQuery = PyQuery(response.text)

        # Mengambil body utama dari html dengan menggunakan selector yang tepat
        body = html.find(selector='div.grow-0.w-leftcontent.min-w-0')

        # mengambil tags dari content dengan menggunakan parser dari class HtmlParser | check Line 19
        tags = self.__parser.ex(html=body, selector='div.my-5 a')
        
        # Dictionary yang berisi data yang ingin di ambil
        result_extract = {
            'content_url': url_article,
            'posted': self.__parser.ex(html=body, selector='div:nth-child(5)').text(),
            'media_url': self.__parser.ex(html=body, selector='div:nth-child(8) img').attr('src'),
            'tags': [re.sub(r'\s+', ' ', tag.text.strip()) if tag.text else None for tag in tags],
            'article': self.__filter_str(text=self.__parser.ex(html=body, selector='p').text())
        }

        # menambahkan domain kedalam tags yang ada di dalam dictionary
        result_extract["tags"].append(self.MAIN_DOMAIN)

        return result_extract
        

    """ ex()
    function utama yang harus di panggil ketika ingin menggunakan fungsi dari class

    Param:
      main_url (str): url page yang ingin di scraping dan yang dikirimkan dari main.py
      page (int): page website (di function ini page hanya di gunakan untuk keperluan log)

    Returns:
      boolean = akan mereturn False jika data sudah habis dan akan Mereturn True jika data masih ada
    """
    def ex(self, main_url: str, page: int) -> None:
        

        # response adalah hasil dari request ke main_url
        response: Response = requests.get(url=main_url)

        # merubah response yang berupa HTML untuk di jadikan Pyquery
        html: PyQuery = PyQuery(response.text)

        # mengambil semua crads article 
        cards = html.find(selector='div.flex.gap-6 article')

        # jika data sudah habis maka akan mereturn False
        if not cards: return False
        

        # Melooping semua cards untuk mexetract data setiap card nya
        for card in cards:
            card_data: dict = {
                'domain': self.MAIN_DOMAIN,
                'crawling_time': str(datetime.now()),
                'crawling_time_epoch': int(time()),
                'url': main_url,
                'title': self.__parser.ex(html=card, selector='a span:last-child h2').text(),
                'categories': self.__parser.ex(html=card, selector='a span:last-child span:first-child').text(),

                # memanggil functions extract_data untuk mengextract data card nya
                'article': self.extract_data(url_article=self.__parser.ex(html=card, selector='a').attr('href'))
            }

            # loger (Optional)
            print()
            logger.info(f'status: {response.status_code}')
            logger.info(f'page: {page}')
            logger.info(f'main_url: {main_url}')
            logger.info(f'title: {card_data["title"]}')
            logger.info(f'categories: {card_data["categories"]}')
            print()

            # Menulis data kedalam file json dengan memanggul function ex() dari class Writer() | check Line 22
            self.__writer.ex(path=f'data/{vname(card_data["title"])}.json', content=card_data)
        
        if cards: return True
        

        
        