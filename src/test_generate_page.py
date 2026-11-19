import unittest

from generate_page import extract_title

class TestGeneratePage(unittest.TestCase):
    # extract_title

    def test_find_h1(self):
        my_md = "Something, something\n# Title"
        title = extract_title(my_md)
        self.assertEqual("Title", title)

    def test_raise_error_when_no_title(self):
        my_md = "Something, something\nNot a title"
        with self.assertRaises(ValueError):
            title = extract_title(my_md)

    def test_trail_spaces(self):
        my_md = "Something, something\n#    Title     "
        title = extract_title(my_md)
        self.assertEqual("Title", title)