from py4j.java_gateway import JavaGateway

from common.util import util

class BookmarkService:

    BookmarkService_class = None;
    Time_class = None;

    def __init__(self, config):
        classpath = config['classpath']
        gw = JavaGateway.launch_gateway(classpath=classpath)
        self.BookmarkService_class = gw.jvm.service.bookmark.RecordBookmarkService
        self.Time_class = gw.jvm.model.util.time.Time

    def create_bookmark(self, bookmark_name, initial_id, initial_time):
        initial_time_str = None
        if initial_time is not None:
            initial_time_str = util.datetime_to_json(initial_time)
        self.BookmarkService_class.setupBookmark(bookmark_name, initial_id, initial_time_str)

    def get_last_record_time(self,bookmark_name):
        return util.datetime_from_json(self.BookmarkService_class.getLastBookmark(bookmark_name).
                       getLastRecordTime().toString())

    def get_last_record_id(self, bookmark_name):
        return util.datetime_from_json(self.BookmarkService_class.getLastBookmark(bookmark_name).getLastRecordId())

    def updateBookmark(self, bookmark=None, bookmark_name=None, id=None, time=None):
        if bookmark is not None:
            self.BookmarkService_class.updateBookmark(bookmark.bookmark_name, \
                                                      self.datetime_to_javaTime(bookmark.process_start_time), \
                                                      self.datetime_to_javaTime(bookmark.process_end_time), \
                                                      bookmark.input_size, \
                                                      bookmark.output_size, \
                                                      bookmark.record_id, \
                                                      self.datetime_to_javaTime(bookmark.record_time))
        else:
            self.BookmarkService_class.updateBookmark(bookmark_name, id, self.datetime_to_javaTime(time))

    def datetime_to_javaTime(self,datetime_obj):
        if datetime_obj is None:
            return None;
        else:
            return self.Time_class.parse(util.datetime_to_json(datetime_obj))

