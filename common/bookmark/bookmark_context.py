from common.bookmark.bookmark_state import Bookmark_State


class Bookmark_Context:
    bookmark_name = None;
    dao = None;

    def __init__(self, bookmark_name, dao):
        self.bookmark_name = bookmark_name
        self.dao = dao

    def create_bookmark(self, config):
        return self.dao.create_bookmark(self.bookmark_name, config)

    def bookmark_exists(self):
        return self.dao.bookmark_exists(self.bookmark_name)

    def get_bookmarks(self, starttime=None, endtime=None, top=1):
        return self.dao.get_bookmarks(self.bookmark_name, starttime, endtime, top)

    def update_bookmarks(self, bookmarks):
        return self.dao.update_bookmarks(self.bookmark_name, bookmarks)

    def save_bookmarks(self, bookmarks):
        return self.dao.save_bookmarks(self.bookmark_name, bookmarks)

    def update_failed(self, bookmarks):
        return self.dao.update_failed(self.bookmark_name, bookmarks)

    def save_failed(self, bookmarks):
        return self.dao.update_failed(self.bookmark_name, bookmarks)

    def lock(self):
        return self.dao.lock(self.bookmark_name, Bookmark_State.LOCKED)

    def unlock(self):
        return self.dao.unlock(self.bookmark_name, Bookmark_State.UNLOCKED)

    def mark_failed(self):
        return self.dao.mark_failed(self.bookmark_name, Bookmark_State.FAILED)

    def get_state(self):
        return self.dao.get_state(self.bookmark_name)