from libs import Scrapper

class Main:
    def __init__(self, main_url: str) -> None:
        self.__main_url: str = main_url
        self.__scrapper: Scrapper = Scrapper()
        pass

    def main():
        pass

    def ex(self):
        self.__scrapper.ex(main_url=self.__main_url, page=1)


if __name__ == '__main__':
    main = Main(main_url='https://www.cnnindonesia.com/indeks/2/1')
    main.ex()