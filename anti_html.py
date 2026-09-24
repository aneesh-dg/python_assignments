import sys
from html.parser import HTMLParser
from urllib.request import urlopen

class HTMLStripper(HTMLParser):
    def __init__(self):
        super().__init__()
        self.text = []

    def handle_data(self, data):
        self.text.append(data)

    def get_text(self):
        return "".join(self.text)

def main():
    url = sys.argv[1]
    with urlopen(url) as response:
        html = response.read().decode("utf-8")
    parser = HTMLStripper()
    parser.feed(html)
    print(parser.get_text())

if __name__ == "__main__":
    main()