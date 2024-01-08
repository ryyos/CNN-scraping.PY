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

class Cnn:
    def __init__(self) -> None:

        self.__parser = HtmlParser()
        self.__writer = Writer()
        
        self.MAIN_DOMAIN = 'www.cnnindonesia.com'
    

    def __filter_str(self, text: str) -> str:
        cleaned_text = text.replace('ADVERTISEMENT SCROLL TO CONTINUE WITH CONTENT', ' ') \
                           .replace('[Gambas:Video CNN]', '') \
                           .replace('/', ' ') \
                           .replace('\xa0k', ' ') \
                           .replace('\u00a0', '') \
                           .replace('\"', "'") \
                           .replace('\n', '')
            
        return cleaned_text


    def extract_data(self, url_article: str):

        response: Response = requests.get(url=url_article)
        html: PyQuery = PyQuery(response.text)
        body = html.find(selector='div.grow-0.w-leftcontent.min-w-0')

        tags = self.__parser.ex(html=body, selector='div.my-5 a')
        
        result_extract = {
            'content_url': url_article,
            'posted': self.__parser.ex(html=body, selector='div:nth-child(5)').text(),
            'media_url': self.__parser.ex(html=body, selector='div:nth-child(8) img').attr('src'),
            'tags': [re.sub(r'\s+', ' ', tag.text.strip()) if tag.text else None for tag in tags],
            'article': self.__filter_str(text=self.__parser.ex(html=body, selector='p').text())
        }

        tags.append(self.MAIN_DOMAIN)
        return result_extract
        

    def ex(self, main_url: str, page: int) -> None:
        
        response: Response = requests.get(url=main_url)
        html: PyQuery = PyQuery(response.text)

        cards = html.find(selector='div.flex.gap-6 article')

        if not cards: return False
        

        for card in cards:
            card_data: dict = {
                'domain': self.MAIN_DOMAIN,
                'crawling_time': str(datetime.now()),
                'crawling_time_epoch': int(time()),
                'url': main_url,
                'title': self.__parser.ex(html=card, selector='a span:last-child h2').text(),
                'categories': self.__parser.ex(html=card, selector='a span:last-child span:first-child').text(),

                'article': self.extract_data(url_article=self.__parser.ex(html=card, selector='a').attr('href'))
            }

            print()
            logger.info(f'status: {response.status_code}')
            logger.info(f'page: {page}')
            logger.info(f'main_url: {main_url}')
            logger.info(f'title: {card_data["title"]}')
            logger.info(f'categories: {card_data["categories"]}')
            print()

            self.__writer.ex(path=f'data/{vname(card_data["title"])}.json', content=card_data)
        
        if cards: return True
        

        
        