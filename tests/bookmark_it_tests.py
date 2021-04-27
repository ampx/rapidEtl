import unittest
from datetime import datetime
import time

from common.bookmark.bookmark import Bookmark
from common.bookmark.bookmark_service import Bookmark_Service


def setup_unique_bookmark():
    bookmark_url = "http://localhost:8080/bookmarks"
    bs = Bookmark_Service({"bookmark_url": bookmark_url})
    return bs.get_context("bookmark_" + str(datetime.now())
                          .replace(" ", "_").replace(".","").replace(":","").replace("-",""))


class BookmarkItTest(unittest.TestCase):
    def test1_create(self):
        bookmark_context = setup_unique_bookmark()
        self.assertEqual(bookmark_context.bookmark_exists(), False)
        self.assertEqual(bookmark_context.create_bookmark({"retentionDays": 1}), True)
        self.assertEqual(bookmark_context.bookmark_exists(), True)

    def test2_bookmark_insert(self):
        bookmark_context = setup_unique_bookmark()
        bookmark_context.create_bookmark({"retentionDays": 1})
        bookmarks = [Bookmark(metrics={"metric0": "value0", "metric1": "value1"})]
        self.assertEqual(bookmark_context.save_bookmarks(bookmarks), True)

    def test3_fetch_most_recent(self):
        # create and insert bookmarks
        bookmark_context = setup_unique_bookmark()
        bookmark_context.create_bookmark({"retentionDays": 1})
        bookmarks = []
        bookmarks.append(Bookmark(metrics={"metric0": "value0", "metric1": "value1"}))
        time.sleep(5.0)
        bookmarks.append(Bookmark(metrics={"metric2": "value2", "metric3": "value3"}))
        bookmark_context.save_bookmarks(bookmarks)

        bookmarks = bookmark_context.get_bookmarks(top=1)
        bookmark = bookmarks.get(0)
        bookmark.replace(microsecond=0)
        last_bookmark_created = bookmarks.get(1)
        last_bookmark_created.replace(microsecond=0)
        self.assertEqual(bookmark.timestamp == last_bookmark_created.timestamp, True)
        self.assertEqual(bookmark.metrics == last_bookmark_created.metrics, True)

    def test3_fetch_oldest(self):
        # create and insert bookmarks
        bookmark_context = setup_unique_bookmark()
        bookmark_context.create_bookmark({"retentionDays": 1})
        bookmarks = []
        bookmarks.append(Bookmark(metrics={"metric0": "value0", "metric1": "value1"}))
        time.sleep(5.0)
        bookmarks.append(Bookmark(metrics={"metric2": "value2", "metric3": "value3"}))
        bookmark_context.save_bookmarks(bookmarks)

        bookmarks = bookmark_context.get_bookmarks(top=-11)
        bookmark = bookmarks.get(1)
        bookmark.replace(microsecond=0)
        first_bookmark_created = bookmarks.get(1)
        first_bookmark_created.replace(microsecond=0)
        self.assertEqual(bookmark.timestamp == first_bookmark_created.timestamp, True)
        self.assertEqual(bookmark.metrics == first_bookmark_created.metrics, True)


if __name__ == '__main__':
    unittest.main()
