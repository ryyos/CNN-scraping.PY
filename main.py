from time import sleep
from libs import Scrapper
from libs import Writer

class Main:
    def __init__(self, main_url: str) -> None:
        self.__main_url: str = main_url
        self.__write: Writer = Writer()
        
        pass


    def create_url(self, url: str, page: int) -> str:
        raw = url.split('/')
        raw[-1] = str(page)
        return '/'.join(raw)

    def ex(self):
        page = 1

        one_hundred = []
        all_data = []

        while True:
            __scrapper: Scrapper = Scrapper()
            base_url = self.create_url(url=self.__main_url, page=page)

            results = __scrapper.ex(main_url=base_url, page=page)

            one_hundred.append(results)
            all_data.append(results)

            if len(one_hundred) == 100: self.__write.ex(path=f'data/hundred/page{str(page)}.json', content=one_hundred); one_hundred.clear()
            if results == 'Empety': self.__write.ex(path=f'data/all/datas.json', content=all_data); all_data.clear(); break
            self.__write.ex(path=f'data/page/page{str(page)}.json', content=results)
            
            page+=1
        


if __name__ == '__main__':
    main = Main(main_url='https://www.cnnindonesia.com/indeks/2/1')
    main.ex()