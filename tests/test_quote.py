import unittest
from App.models import Quote

class TestQuote(unittest.TestCase):
    def setUp(self):
        """
        Set up method that will run before every Test
        """
        self.random_quote = Quote("Jessica Mwangi", "Hello World")

    def test_instance(self):
        self.assertTrue(isinstance(self.random_quote, Quote))

    def test_init(self):
        self.assertEqual(self.random_quote.author, "Jessica Mwangi")
        self.assertEqual(self.random_quote.quote,"Positive anything is better than negative nothing.")