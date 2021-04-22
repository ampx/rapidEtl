class Bookmark_Context:
    bookmark_name = None;
    dao = None;

    def __init__(self, bookmark_name, dao):
        self.bookmark_name = bookmark_name
        self.dao = dao

    def get_bookmarks(self, starttime=None, endtime=None, top=1):
        return self.dao.get_bookmarks(self.bookmark_name, starttime, endtime, top)

    def update_bookmark(self, metrics):
        return self.dao.update_bookmarks(self.bookmark_name, metrics)

    def save_bookmark(self, metrics):
        return self.dao.update_bookmarks(self.bookmark_name, metrics)

    def create_bookmark(self, config):
        return self.dao.create_bookmark(self.bookmark_name, config)

    def bookmark_exists(self):
        return self.dao.bookmark_exists(self.bookmark_name)
