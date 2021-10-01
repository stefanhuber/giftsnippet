import unittest
import giftsnippet


class TestHighlight(unittest.TestCase):

    def test_get_data_uri(self):
        data_uri_1 = giftsnippet.get_data_uri_snippet('test_data/code/geltungsbereiche_03_01.py')
        data_uri_2 = giftsnippet.get_data_uri_snippet('test_data/code/geltungsbereiche_03_02.py')
        self.assertRegex(data_uri_1, '^data\\\\:image/png;base64,[a-zA-Z0-9+/=\\\\]+$')
        self.assertRegex(data_uri_2, '^data\\\\:image/png;base64,[a-zA-Z0-9+/=\\\\]+$')
