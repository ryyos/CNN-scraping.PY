from time import perf_counter
from time import sleep
from libs import Cnn
from libs import logger

class Main:
    def __init__(self) -> None:
        self.__main_url = 'https://www.cnnindonesia.com/indeks/2/1'


    def create_url(self, url: str, page: int) -> str:
        raw = url.split('/')
        raw[-1] = str(page)
        return '/'.join(raw)

    def ex(self):
        page = 1

        while True:
            cnn = Cnn()
            base_url = self.create_url(url=self.__main_url, page=page)

            results = cnn.ex(main_url=base_url, page=page)
            if not results : break
            
            page+=1
        


if __name__ == '__main__':
    start = perf_counter()

    logger.info('CNN Scraping start.. ')
    print()

    main = Main()
    main.ex()

    logger.info('scraping is complete..')
    logger.info(f'total scraping time: {perf_counter() - start}')

