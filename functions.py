from urllib.parse import urlparse
import logging
import yaml
import pickle
import urllib.request
from bs4 import BeautifulSoup
from html.parser import HTMLParser
import os
from collections import Counter


def add_protocol_to_url(url):
    """Add http:// protocol to url."""
    if not urlparse(url).scheme:
        url = 'http://' + url

    return url


# parse yaml-file
def parse_yaml_file():
    a_yaml_file = open("synonyms.yaml")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    
    return parsed_yaml_file


# unpickle results from DB
def unpickle_db_results(results):
    unpickled_list = pickle.loads(results, fix_imports=True,
                                  encoding="ASCII", errors="strict",
                                  buffers=None)
    print(unpickled_list)
    
    return unpickled_list


class ContaTags:

    def __init__(self, url):
        self.url = url
        self.arquivos = []
        self.tags = []
        self.Lista = []

    def run(self):
        # check if we enter a URL without the protocol
        global url        # переменную сделаем глобальной
        url = self.url                  # declared a variable
        if not urlparse(url).scheme:
            url = 'http://' + url

        logging.info(url)  # use declared url variable
        # download html content: request - response
        response = urllib.request.urlopen(url)  # use url variable
        webContent = response.read()
        # write to a file
        f = open('webpage.html', 'wb')
        f.write(webContent)
        f.close

        class MyHTMLParser(HTMLParser):

            def handle_starttag(self, tag, attrs):
                count.append(tag)

            def handle_endtag(self, tag):
                count.append(tag)

        parser = MyHTMLParser()

        for file in os.listdir(path=os.getcwd()):
            if file.endswith(".html"):
                self.arquivos.append(file)
                caminho = os.getcwd() + "\\" + file
                doc = open(caminho, "r", encoding="utf8")
                soup = BeautifulSoup(doc, 'html.parser')
                count = []
                parser.feed(soup.prettify())
                self.tags.append(count)

        z = []

        for i, item in enumerate(self.tags):
            z.append(Counter(self.tags[i]))

        # print(z)  # a list with a the collections.Counter Object
        # list with the collections.Counter Object to a dict
        tag_dict = dict(z[0])
        print(tag_dict)
        
        return tag_dict
