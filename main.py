from time import perf_counter
from time import sleep
from libs import Cnn
from libs import logger


""" Class Main

Class utama untuk menjalankan function scraping dari Cnn service

"""
class Main:
    def __init__(self) -> None:
        self.__main_url = 'https://www.cnnindonesia.com/indeks/2/1'

    """ create_url()
    function untuk merubah nilai page dari url

    Params:
      url (str): URL utama
      page (int): Page yang ingin di terapkan

    Returns:
      str: URL setelah nilai page dirubah
    """
    def create_url(self, url: str, page: int) -> str:
        raw = url.split('/')
        raw[-1] = str(page)
        return '/'.join(raw)


    """ ex()
    function utama yang harus di jalankan ketika ingin menggunakan fungsi dari class

    Param:
      self: untuk memanggil function ini class harus di deklarasikan menjadi Object

    """
    def ex(self):
        page = 1

        while True:

            """
            Mendklarasikan Class Cnn
            cnn adalah Object dari class Cnn

            NB: Perhatikan Huruf Kapital
            """
            cnn = Cnn()

            # memanggil function create_url, dan hasil dari function disimpan di variable base_url
            base_url = self.create_url(url=self.__main_url, page=page)


            """
            Memanggil function ex() dari Class Cnn yang berada di file service/Cnn.py
            
            variable hanya akan berisi 2 pilihan boolead True | False
            jika result True maka looping akan di lanjutkan
            jika resukt False maka looping akan berhenti karena data yang harus di ambil sudah habis
            """
            results = cnn.ex(main_url=base_url, page=page)
            if not results : break
            
            # menambah nilai page yang di gunakan untuk merubah url
            page+=1
        


"""
Jika file main.py di jalankan maka code di bawah ini yang akan di jalankan
"""
if __name__ == '__main__':

    # digunakan untuk menyimpan waktu saat code di jalankan (Optional)
    start = perf_counter()

    # logging (Optional)
    logger.info('CNN Scraping start.. ')
    print()


    """
    Mendklarasikan Class Main yang ada di atas
    main adalah Object dari class Main

    NB: Perhatikan Huruf Kapital
    """
    main = Main()

    # memanggil function ex() dari class Main
    main.ex()

    logger.info('scraping is complete..')
    logger.info(f'total scraping time: {perf_counter() - start}')

