#! -*- coding: UTF-8 -*-
from bs4 import BeautifulSoup
import requests
import urllib
import re
import os

BASE_DIR = os.path.dirname(__file__)


class PacktFreeLearningCrawler(object):


    def __init__(self, url=None):
        self.url = 'https://www.packtpub.com/packt/offers/free-learning' if not url else url
        self.soup = BeautifulSoup(urllib.urlopen(self.url).read(), 'html.parser')
        self.user, self.password = self._read_conf_file()
        self.create_session()

    def _read_conf_file(self):
        with open("{}/.packt_user.cfg".format(BASE_DIR)) as conf:
            return conf.readlines()[:2]

    def create_session(self):
        data = {'email': self.user.rstrip(),
                   'password': self.password.rstrip(),
                   'op': 'Login',
                   'form_build_id': 'form-a4d03c38ea8befcab94afc2cd4a7c8af',
                   'form_id': 'packt_user_login_form'
                  }
        self.session = requests.session()
        self.session.post('https://www.packtpub.com/register', data=data)

    def _clear_element(self, element):
        return re.sub("\s(\\.)*\s", "", element)

    def free_book_title(self):
        h2_title_book = self.soup.find_all("div", { "class" : "dotd-title" })[0].find('h2')
        return self._clear_element(h2_title_book.string)

    def all_books_user(self):
        try:
            html_user_ebooks = self.session.get('https://www.packtpub.com/account/my-ebooks').text
            my_ebooks = BeautifulSoup(html_user_ebooks, 'html.parser')
            books = my_ebooks.find(id='product-account-list').find_all('div', {'class': 'product-line unseen'})
            return [book['title'].replace(' [eBook]', "") for book in books]
        except:
            raise ValueError("Usuário/Senha incorretos")


    def link_free_book(self):
        clain_book_input = self.soup.find('div', {'class': 'dotd-main-book-form cf'})
        return clain_book_input.find('a', {'class': 'twelve-days-claim'})['href']

    def claim_free_book(self):
        if self.free_book_title() not in self.all_books_user():
            return self.session.get('https://www.packtpub.com/{link}'.format(link=self.link_free_book())).status_code
        return 200

if __name__ == '__main__':
    packt = PacktFreeLearningCrawler()
    if packt.claim_free_book() == 200:
        print "Livro já adicionado!"
    else:
        print "Erro ao adicionar o livro"