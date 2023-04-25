import unittest
from unittest.mock import patch, Mock
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

