from django.test import TestCase
from ..models import Quotes, Author
from datetime import date
from django.core.exceptions import ValidationError


# Testcases for model 'Quotes'

class AuthorModelTest(TestCase):
    def setUp(self):
        """Test ficture for testing 'Author' model"""
        self.author = Author.objects.create(name="Emily Dickinson", dateofbirth=date(1982, 12, 1))

    def test_author_creation(self):
        """Testcase for testing model creation"""
        self.assertEqual(self.author.name, "Emily Dickinson")
        self.assertEqual(self.author.dateofbirth, date(1982, 12, 1))

    def test_get_author(self):
        """Testcase for testing retrieving an Author instance"""
        self.assertEqual(str(self.author), "Emily Dickinson")

class QuotesModelTest(TestCase):
    def setUp(self):
        """Test ficture for testing 'Quotes' model"""
        self.author = Author.objects.create(name="Emily Dickinson", dateofbirth=date(1982, 12, 1))
        self.quote = Quotes.objects.create(text='Sample quote', author=self.author)

    def test_quote_creation(self):
        """Testcase for testing model creation"""
        self.assertEqual(self.quote.text, "Sample quote")
        self.assertEqual(self.quote.author, self.author)

    def test_get_quote(self):
        """Testcase for testing retrieving an Quotes instance"""
        self.assertEqual(str(self.quote), f'"Sample quote" - {self.author}')

    def test_clean_method(self):
        """Testing validation error on missing text field"""

        with self.assertRaises(ValidationError):
            quotes_wo_text = Quotes(author=self.author)
            quotes_wo_text.full_clean()
            
    def test_save_method(self):
        """Test instance getting saved without error and save method calling full_clean() method before saving"""
        quotes_wo_text = Quotes(text="Sample quotes", author=self.author)
        quotes_wo_text.save()

        #Test save method if fields are not valid
        with self.assertRaises(ValidationError):
            quotes_wo_text = Quotes(author=self.author)
            quotes_wo_text.save()














