from datetime import datetime as time

class Logs:
    def __init__(self) -> None:
        pass

    def ex(self, page: int, no: int, title: str, base_url: str, child_url: str) -> None:
        log = f"""
Page: {page}
No: {no}
Title: {title}
Base_url: {base_url}
scrapping_url: {child_url}
Status: success
Time: {time.now()}
            """
        
        print(log)