import unittest
from infohandler import InfoHandler

class TestInfoHandler(unittest.TestCase):
	def setUP(self):
		print("setup goes here")

	def test_hello_world(self):
		self.assertEqual("Hello world", "Hello world")
