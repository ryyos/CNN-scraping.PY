import requests
import json
import re
from time import sleep
from pyquery import PyQuery
from requests import Response
from datetime import datetime as time
from libs.utils.parser import HtmlParser

class Scrapper:
    def __init__(self) -> None:
        self.__temporary: list[dict] = []
        self.__results: dict = dict()
        self.__results.update({'konten': []})
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
                'tag': self.__parser.ex(html=article, selector='a span:last-child span:first-child').text(),
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
                           .replace('\u00a0', '')
            
        return cleaned_text


    def extract_data(self, req_url: str):
        print('url masuk scraping -> ', req_url)

        response: Response = requests.get(url=req_url)
        html: PyQuery = PyQuery(response.text)
        body = html.find(selector='div.grow-0.w-leftcontent.min-w-0')

        result_extract = {
            'posted': self.__parser.ex(html=body, selector='div:nth-child(5)').text(),
            'media_url': self.__parser.ex(html=body, selector='div:nth-child(8) img').attr('src'),
            'tags': [re.sub(r'\s+', ' ', tag.text.strip()) for tag in self.__parser.ex(html=body, selector='div.my-5 a')],
            'article': self.__filter_str(text=self.__parser.ex(html=body, selector='p').text())
        }
        # print(result_extract)
        sleep(1)
        return result_extract
        


    def ex(self, main_url: str, page: int) -> None:
        
        urls = self.filter_url(req_url=main_url)

        for index, url in enumerate(urls):
            # self.extract_data(req_url=url)
            self.__temporary[index]['konten'] = self.extract_data(req_url=url)
        
        self.__results.update({
            'page': page,
            'main_url': main_url,
            'time': str(time.now()),
            'datas': self.__temporary
        })

        with open('private/data/test6.json', 'w') as file:
            json.dump(self.__results, file, indent=2)

        sleep(10)
        return self.__results

        

        
        