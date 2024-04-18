from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Quotes, Author
from ..serializers import QuotesSerializer
from datetime import date
import json

# Initialize the APIClient app
client = Client()

class GetQuotesTest(TestCase):
    """ Tests 'QuotesListView' and 'QuotesRetrieveView' """

    def setUp(self):
        """ Testdata """

        # Create Authors
        self.author1 = Author.objects.create(name="Emily Dickinson", dateofbirth=date(1982, 12, 1))
        self.author2 = Author.objects.create(name="Alice Walker", dateofbirth=date(2021, 4, 9))

        # Create Quotes
        self.quote1 = Quotes.objects.create(text='Sample quote1', author=self.author1)
        self.quote2 = Quotes.objects.create(text='Sample quote2', author=self.author2)

    def test_list_all_quotes(self):
        """Testcase for listing all quotes"""

        #  Get response from API endpoint
        response = client.get(reverse('listQuotes'))

        # Test response data with data from database
        quotes = Quotes.objects.all()
        ser = QuotesSerializer(quotes, many=True)
        self.assertEqual(response.data, ser.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_empty_list_quotes(self):
        """Testcase for fetching lists when no quotes available"""

        # Delete all records
        Quotes.objects.all().delete()

        # Get response from API endpoint
        response = client.get(reverse('listQuotes'))

        # Test response data with data from database
        self.assertContains(response, "")
        
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_valid_single_quote(self):
        """Testcase for fetching single valid quote"""

        # Get response from API endpoint
        response = client.get(reverse('getSingleQuote', kwargs={'pk': self.quote1.pk}))

        # Test response data with data from database
        quote = Quotes.objects.get(pk=self.quote1.pk)
        ser = QuotesSerializer(quote)
        self.assertEqual(response.data, ser.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_quote(self):
        """Testcase for fetching single invalid quote"""

        response = client.get(reverse('getSingleQuote', kwargs={'pk': 300}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)


class CreateNewQuoteTest(TestCase):
    """ Tests 'QuotesCreateView'"""
    '''Inserting a new quote involves two cases:
            Inserting a valid quote
            Inserting an invalid quote'''
    
    def setUp(self):
        self.valid_payload = {
            "author": {
                        "name": "A. P. J. Abdul Kalam",
                        "dateofbirth": "1931-10-15"
                     },
            "text": "We should not give up and we should not allow the problem to defeat us.",
            "creation_date": "2024-04-17"
        }
        self.invalid_payload = {
            "author": {
                        "name": "A. P. J. Abdul Kalam",
                        "dateofbirth": "1931-10-15"
                     },
            "text": "",
            "creation_date": "2024-04-17"
        }

    def test_create_valid_quote(self):
        """Testcase for creating valid quote"""
        response = client.post(reverse('createQuote'), 
                               data=json.dumps(self.valid_payload),
                               content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_quote(self):
        """Testcase for creating invalid quote"""
        response = client.post(reverse('createQuote'),
                               data=json.dumps(self.invalid_payload),
                               content_type='application/json')    
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class UpdateQuoteTest(TestCase):
    """ Tests 'QuotesUpdateView'"""
    '''Updating quote involves two cases:
            Updating valid quote
            Updating an invalid quote'''
    
    def setUp(self):
        # Create sample author
        self.author1 = Author.objects.create(name="Emily Dickinson", dateofbirth=date(1982, 12, 1))
        # Create sample quotes
        self.quote1 = Quotes.objects.create(text='Sample quote1', author=self.author1)

        self.valid_payload = {
            "id": 4,
            "author": {
                    "id": 2,
                    "name": "A. P. J. Abdul Kalam",
                    "dateofbirth": "1931-10-15"
                     },
            "text": "We should not give up and we should not allow the problem to defeat us.",
            "creation_date": "2024-04-17"
        }
        self.invalid_payload = {
            "id": 4,
            "author": {
                    "id": 2,
                    "name": "A. P. J. Abdul Kalam",
                    "dateofbirth": "1931-10-15"
                     },
            "text": "",
            "creation_date": "2024-04-17"
        }

    def test_valid_update_quote(self):
        """Testcase for updating valid quote"""
        response = client.put(reverse('updateQuote', kwargs={'pk': self.quote1.pk}),
                              data=json.dumps(self.valid_payload),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_update_puppy(self):
        """Testcase for updating invalid quote"""
        response = client.put(reverse('updateQuote', kwargs={'pk': self.quote1.pk}),
                              data=json.dumps(self.invalid_payload),
                              content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        

class DeleteSinglePuppyTest(TestCase):
    """Testcase for deleting quote"""

    def setUp(self):
        # Create sample author
        self.author1 = Author.objects.create(name="Emily Dickinson", dateofbirth=date(1982, 12, 1))
        # Create sample quotes
        self.quote1 = Quotes.objects.create(text='Sample quote1', author=self.author1)

    def test_delete_single_quote(self):
        response = client.delete(reverse('deleteQuote', kwargs={'pk': self.quote1.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_delete_invalid_quote(self):
        response = client.delete(reverse('deleteQuote', kwargs={'pk': 300}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)



