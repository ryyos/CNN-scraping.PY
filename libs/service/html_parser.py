import requests
import json
import re
from time import sleep
from pyquery import PyQuery
from requests import Response
from datetime import datetime as time
from libs.utils.parser import HtmlParser
from libs.utils.logs import Logs

class Scrapper:
    def __init__(self) -> None:
        self.__temporary: list[dict] = []
        self.__results: dict = dict()
        self.__logs: Logs = Logs()
        self.__parser = HtmlParser()
        pass
    

    def filter_url(self, req_url: str):
        urls: list[str] = []
        response: Response = requests.get(url=req_url)
        html: PyQuery = PyQuery(response.text)
        id: int = 1

        articles = html.find(selector='div.flex.gap-6 article')

        for article in articles:
            header_data: dict = {
                'id': id,
                'title': self.__parser.ex(html=article, selector='a span:last-child h2').text(),
                'categories': self.__parser.ex(html=article, selector='a span:last-child span:first-child').text(),
                'url': self.__parser.ex(html=article, selector='a').attr('href')
            }

            urls.append(self.__parser.ex(html=article, selector='a').attr('href'))
            self.__temporary.append(header_data)

            id += 1

        return urls

    def __filter_str(self, text: str) -> str:
        cleaned_text = text.replace('ADVERTISEMENT SCROLL TO CONTINUE WITH CONTENT', ' ') \
                           .replace('[Gambas:Video CNN]', '') \
                           .replace('/', ' ') \
                           .replace('\xa0k', ' ') \
                           .replace('\u00a0', '') \
                           .replace('\"', "'") \
                           .replace('\n', '')
            
        return cleaned_text


    def extract_data(self, req_url: str, log_page: int, log_no: int, log_base_url: str, log_url_scrap: str, log_title: str):
        self.__logs.ex(page=log_page, base_url=log_base_url, child_url=log_url_scrap, title=log_title, no=log_no)

        response: Response = requests.get(url=req_url)
        html: PyQuery = PyQuery(response.text)
        body = html.find(selector='div.grow-0.w-leftcontent.min-w-0')

        result_extract = {
            'posted': self.__parser.ex(html=body, selector='div:nth-child(5)').text(),
            'media_url': self.__parser.ex(html=body, selector='div:nth-child(8) img').attr('src'),
            'tags': [re.sub(r'\s+', ' ', tag.text.strip()) for tag in self.__parser.ex(html=body, selector='div.my-5 a')],
            'article': self.__filter_str(text=self.__parser.ex(html=body, selector='p').text())
        }
        
        return result_extract
        


    def ex(self, main_url: str, page: int) -> None:
        no = 0

        urls = self.filter_url(req_url=main_url)
        if len(urls) == 0: return 'Empety'

        for index, url in enumerate(urls):
            no += 1
            self.__temporary[index]['konten'] = self.extract_data(req_url=url, \
                                                                    log_page=page, \
                                                                    log_no=no, \
                                                                    log_base_url=main_url, \
                                                                    log_url_scrap=url, \
                                                                    log_title=self.__temporary[index].get('title'))
        
        self.__results.update({
            'page': page,
            'main_url': main_url,
            'time': str(time.now()),
            'datas': self.__temporary
        })

        return self.__results

        

        
        