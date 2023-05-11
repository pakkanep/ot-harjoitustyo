import unittest
from unittest.mock import patch, MagicMock
from services.infoseeker import InfoSeeker
from bs4 import BeautifulSoup


class TestInfoSeeker(unittest.TestCase):

    def setUp(self):
        self.seeker = InfoSeeker()

    def test_reset_all(self):
        self.seeker.amount_ads = 10
        self.seeker.amount_pages = 2
        self.seeker.interruptvalue = True
        self.seeker.links.add("link")
        self.seeker.successful_add_handles = 40
        self.seeker.information_dict["Java"] = 0
        self.seeker.reset_all()

        self.assertEqual(self.seeker.links, set())
        self.assertEqual(self.seeker.interruptvalue, False)
        self.assertEqual(self.seeker.amount_ads, 0)
        self.assertEqual(self.seeker.amount_pages, 0)
        self.assertEqual(self.seeker.successful_add_handles, 0)
        self.assertEqual(self.seeker.information_dict, {
            "Java": 1,
            "Python": 1,
            "C++": 1,
            "Go": 1,
            "Rust": 1,
            "Javascript": 1,
            "PHP": 1,
            "C#": 1,
            "Ruby": 1,
            "C": 1,
            "SQL": 1,
            "PostgreSQL": 1,
            "TypeScript": 1,
            "Kotlin": 1,
            "Scala": 1,
            "React": 1,
            "Node.js": 1,
            ".NET": 1
        })


    def test_search_instances(self):
        text = """We are looking for a Java developer who knows Java programming 
            language and is familiar with Java frameworks like Spring and Hibernate.
        """
        expected_result = {
            "Java": 2,
            "Python": 1,
            "C++": 1,
            "Go": 1,
            "Rust": 1,
            "Javascript": 1,
            "PHP": 1,
            "C#": 1,
            "Ruby": 1,
            "C": 1,
            "SQL": 1,
            "PostgreSQL": 1,
            "TypeScript": 1,
            "Kotlin": 1,
            "Scala": 1,
            "React": 1,
            "Node.js": 1,
            ".NET": 1
        }
        self.seeker.search_instances(text)
        result = self.seeker.information_dict
        self.assertEqual(result, expected_result)


    @patch('requests.get')
    def test_search_amount_of_ads(self, mock_get):
        mock_response = """
            <html><body><div class="m-b-10-on-all text--body 
            text--left text--center-desk"><b>10</b> hakutulosta</div></body></html>
        """
        mock_get.return_value.text = mock_response
        expected_result = 10
        url = 'http://example.com'
        result = self.seeker.search_amount_of_ads(url)
        self.assertEqual(result, expected_result)


    def test_search_amount_of_pages(self,):
        # valid URL
        url = "https://duunitori.fi/tyopaikat/ala/ohjelmointi-ja-ohjelmistokehitys?sivu="
        result = self.seeker.search_amount_of_pages(url)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, int)

"""     
    def test_seek_all_pages(self):
        pass

    def test_handle(self):
        pass
"""
