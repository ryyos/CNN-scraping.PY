import requests
import json
from time import sleep
from pyquery import PyQuery
from requests import Response
from libs.utils.parser import HtmlParser

class Scrapper:
    def __init__(self) -> None:
        self.__results: list[dict] = []
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
                'posted': self.__parser.ex(html=article, selector='a span:last-child span:last-child').text().split('•')[-1],
                'url': self.__parser.ex(html=article, selector='a').attr('href')
            }

            urls.append(self.__parser.ex(html=article, selector='a').attr('href'))
            self.__results.append(header_data)

            id += 1
        
        with open('private/data/test.json', 'w') as file:
            json.dump(self.__results, file, indent=2)
        return urls
            


    def extract_data(self, req_url: str):
        response: Response = requests.get(url=req_url)
        html: PyQuery = PyQuery(response.text)
        pass


    def ex(self, main_url: str) -> None:
        urls = self.filter_url(req_url=main_url)

        for index, url in enumerate(urls):

            pass

        self.extract_data(req_url=main_url)
        pass