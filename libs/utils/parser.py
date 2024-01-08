from pyquery import PyQuery


""" HtmlParser
class yang di gunakan untuk memparser atau memfilter HTML 
berdasarkan seletor yang di tentukan
"""
class HtmlParser:
    def __init__(self) -> None:
        pass

    def ex(self, html: PyQuery, selector: str) -> PyQuery:
        result = None
        try:
            html: str = PyQuery(html)
            result = html.find(selector)
        except Exception as err:
            print(err)

        finally:
            return result