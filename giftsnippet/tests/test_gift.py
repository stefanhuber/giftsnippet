import unittest
import giftsnippet


class TestGift(unittest.TestCase):

    def test_find_snippet_lines(self):
        lines = giftsnippet.find_snippet_lines('test_data/gift.txt')
        self.assertEqual(len(lines), 3)

    def test_find_and_read_first_snippet_line(self):
        lines = giftsnippet.find_snippet_lines('test_data/gift.txt')
        self.assertEqual(lines[0]['snippet_file'], "code/geltungsbereiche_03_01.py")
        self.assertEqual(lines[0]['snippet_filetype'], "py")

    def test_replace_line(self):
        test_file_content = "AA\nBB\nCC\nDD\nEE\n"
        test_file = 'test_data/test_file.txt'

        with open(test_file) as file:
            self.assertEqual(file.read(), test_file_content)

        giftsnippet.replace_lines(test_file, [1, 2], ["UVW\n", "XYZ\n"])

        with open(test_file) as file:
            for line_index, line in enumerate(file):
                if line_index == 1:
                    self.assertEqual(line, "UVW\n")
                elif line_index == 2:
                    self.assertEqual(line, "XYZ\n")

        giftsnippet.replace_lines(test_file, [1, 2], ["BB\n", "CC\n"])

        with open(test_file) as file:
            self.assertEqual(file.read(), test_file_content)

    def test_get_base_dir(self):
        self.assertEqual("test_data/code", giftsnippet.get_base_dir('test_data/code/blabla.py'))

    def test_process_gift_file(self):
        test_file = 'test_data/gift.txt'
        giftsnippet.process_gift_file(test_file)