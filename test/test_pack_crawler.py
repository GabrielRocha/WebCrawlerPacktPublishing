import unittest
from packt_crawler import PacktFreeLearningCrawler

class Test_pack_crawler(unittest.TestCase):

    def setUp(self):
        '''Inserir o usuario e senha cadastrados no packtpub '''
        self.pack = PacktFreeLearningCrawler('PACKT_Books.html')

    def test__read_conf_file(self):
        self.assertIn('gabriel.rocha.gbr@gmail.com\n',self.pack._read_conf_file())

    def test__clear_element(self):
        string = "\n\t\t\t\t\t\t\t\t\t\t\t\t\t\t\tHeroku Cookbook\t\t\t\t\t\t\t\t\t\t\t\t\t\t"
        clear_string = self.pack._clear_element(string)
        self.assertEquals(clear_string, "Heroku Cookbook")

    def test_free_book_title(self):
        self.assertEquals(self.pack.free_book_title(), "Heroku Cookbook")

    def test_all_books_user(self):
        self.assertIn("Heroku Cookbook", self.pack.all_books_user())

    def test_link_free_book(self):
        self.assertEquals(self.pack.link_free_book(), '/freelearning-claim/17695/21478')

    def test_claim_free_book(self):
        self.assertEqual(self.pack.claim_free_book(), 200)
