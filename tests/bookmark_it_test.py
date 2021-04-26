import unittest
from datetime import datetime

from common.bookmark.bookmark_service import Bookmark_Service


class MyTestCase(unittest.TestCase):

    bookmark_url = "http://localhost:8080/bookmarks"
    bookmark_context = None
    bookmark_name = None

    def setup(self):
        bs = Bookmark_Service({"bookmark_url":self.bookmark_url})
        self.bookmark_context = bs.get_context()
        self.bookmark_name = "bookmark_" + str(datetime.now())

    def step1_create(self):
        self.assertEqual(self.bookmark_context.bookmark_exists(), False)
        self.assertEqual(self.bookmark_context.create_bookmark({"retentionDays":1}), True)
        self.assertEqual(self.bookmark_context.bookmark_exists(), True)

    def step2_insert_progress(self):
        self.assertEqual(self.bookmark_context.bookmark_exists(), False)
        self.assertEqual(self.bookmark_context.create_bookmark({"retentionDays":1}), True)
        self.assertEqual(self.bookmark_context.bookmark_exists(), True)

if __name__ == '__main__':
    unittest.main()
