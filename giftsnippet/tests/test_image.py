import unittest
import giftsnippet


class TestImage(unittest.TestCase):

    def test_get_data_uri_image(self):
        data_uri = giftsnippet.get_data_uri_image('test_data/image/IBM_PC_5150.jpg', 'jpg')
        self.assertRegex(data_uri, '^data\\\\:image/jpg;base64,[a-zA-Z0-9+/=\\\\]+$')
