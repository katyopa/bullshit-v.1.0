from sqlalchemy import select
import database as db


# add http:// protocol to url
def add_protocol_to_url(url):
    from urllib.parse import urlparse

    if not urlparse(url).scheme:
        url = 'http://' + url

    url
    return(url)


# parse yaml-file
def parse_yaml_file():
    import yaml

    a_yaml_file = open("synonyms.yaml")
    parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
    return parsed_yaml_file


# connect to DB and execute select
def select_from_db(full_url):
    select_data = (select(db.tagcounter_db.c.tagcount).where
                   (db.tagcounter_db.c.url == full_url))

    connection = db.engine.connect()

    results = connection.execute(select_data).fetchall()
    connection.close()
    return results


# unpickle results from DB
def unpickle_db_results(results):
    import pickle
    unpickled_list = (pickle.loads(results, fix_imports=True,
                                   encoding="ASCII", errors="strict",
                                   buffers=None))
    print(unpickled_list)
    return(unpickled_list)


class ContaTags:

    def __init__(self, url):
        self.url = url
        self.arquivos = []
        self.tags = []
        self.Lista = []

    def run(self):

        # check if we enter a URL without the protocol
        from urllib.parse import urlparse

        global url        # переменную сделаем глобальной
        url = self.url                  # declared a variable
        if not urlparse(url).scheme:
            url = 'http://' + url

        url

        # add logging
        import logging
        # filemode='a' - append, добавление
        (logging.basicConfig(level=logging.INFO,
                             filename='tagcounter_log.log',
                             filemode='a',
                             format='%(asctime)s  - %(message)s'))

        logging.info(url)       # use declared url variable

        # download html content: request - response
        import urllib.request
        response = urllib.request.urlopen(url)  # use url variable
        webContent = response.read()

        # write to a file
        f = open('webpage.html', 'wb')
        f.write(webContent)
        f.close

        from bs4 import BeautifulSoup
        from html.parser import HTMLParser

        class MyHTMLParser(HTMLParser):
            def handle_starttag(self, tag, attrs):
                count.append(tag)

            def handle_endtag(self, tag):
                count.append(tag)

        import os

        parser = MyHTMLParser()

        for file in os.listdir(path=os.getcwd()):
            if file.endswith(".html"):
                self.arquivos.append(file)

                caminho = (os.getcwd() + "\\" + file)

                doc = open(caminho, "r", encoding="utf8")
                soup = BeautifulSoup(doc, 'html.parser')

                count = []
                parser.feed(soup.prettify())

                self.tags.append(count)

        from collections import Counter

        z = []

        for i, item in enumerate(self.tags):
            z.append(Counter(self.tags[i]))

        # print(z) # returns a list with a the collections.Counter Object

        # list with the collections.Counter Object to a dict
        tag_dict = dict(z[0])
        print(tag_dict)
        return tag_dict
