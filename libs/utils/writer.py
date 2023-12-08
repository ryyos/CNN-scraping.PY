import json

class Writer:
    def __init__(self) -> None:
        pass

    def ex(self, path: str, content: any) -> None:
        with open(path, 'w') as file:
            json.dump(content, file, indent=2)