import unittest
from unittest.mock import patch, MagicMock
from services.infoseeker import InfoSeeker


class TestInfoSeeker(unittest.TestCase):

    def setUp(self):
        self.seeker = InfoSeeker()

    def test_reset_all(self):
        self.seeker.amount_ads = 10
        self.seeker.amount_pages = 20
        self.seeker.successful_page_handles = 30
        self.seeker.successful_add_handles = 40
        self.seeker.information_dict["Java"] = 0
        self.seeker.reset_all()

        self.assertEqual(self.seeker.amount_ads, 0)
        self.assertEqual(self.seeker.amount_pages, 0)
        self.assertEqual(self.seeker.successful_page_handles, 0)
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
        text = "We are looking for a Java developer who knows Java programming language and is familiar with Java frameworks like Spring and Hibernate."
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
    def test_search_links(self, mock_get):
        url = 'https://duunitori.fi'
        mock_response = MagicMock()
        mock_response.text = """
        <html><body><a class="job-box__hover gtm-search-result" 
        href="/job/123">Job 1</a><a class="job-box__hover gtm-search-result" 
        href="/job/456">Job 2</a></body></html>
        """
        mock_get.return_value = mock_response
        self.seeker.handle = MagicMock()
        self.seeker.search_links(url)
        self.seeker.handle.assert_any_call('https://duunitori.fi/job/123')
        self.seeker.handle.assert_any_call('https://duunitori.fi/job/456')


"""
    def test_search_amount_of_ads(self):
        pass

    def test_search_amount_of_pages(self):
        pass

    def test_seek_all_pages(self):
        pass

    def test_handle(self):
        pass

    def test_start(self):
        pass
"""

