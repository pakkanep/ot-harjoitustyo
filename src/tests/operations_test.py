import unittest
from services.operations import Operations
from services.infoseeker import InfoSeeker

class TestOperations(unittest.TestCase):
    
    def setUp(self):
        self.operations = Operations()
        
    def test_handle_links(self):
        seen = set()
        url = "https://example.com"
        self.operations.handle_links(seen, url)
        self.assertEqual(len(seen), 0)
    

    def test_seek_all_pages(self):
        url = "https://example.com"
        self.operations.seek_all_pages(set(), url)
        self.assertTrue(True)
        
    def test_multi_thread(self):
        url = "https://example.com"
        self.operations.multi_thread(url, self.operations.handle_links, 3)
        self.assertTrue(True) 
        
    def test_start_query(self):
        self.operations.start_query()
        self.assertFalse(self.operations.successful_add_handles == 0)
        self.assertFalse(len(self.operations.links) == 0)
        self.assertTrue(True)
