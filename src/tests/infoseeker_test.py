import unittest
from services.infoseeker import InfoSeeker

class TestInfoSeeker(unittest.TestCase):
	def setUP(self):
		print("setup goes here")

	def test_hello_world(self):
		self.assertEqual("Hello world", "Hello world")
