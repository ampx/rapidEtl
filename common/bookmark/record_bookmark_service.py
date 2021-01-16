from py4j.java_gateway import JavaGateway

from common.util import util

class BookmarkService:
    bookmark_java_instance = None;
    Time_class = None;
    gw = None;

    def __init__(self, config):
        classpath = config.get('classpath')
        id_batch_size = config.get('id_batch_size')
        second_batch_size = config.get('second_batch_size')
        rollover_id = config.get('rollover_id')
        self.gw = JavaGateway.launch_gateway(classpath=classpath)
        self.bookmark_java_instance = self.gw.jvm.service.bookmark.RecordBookmarkService(config['bookmark_name'])
        self.bookmark_java_instance.setRangeSize(id_batch_size)
        self.bookmark_java_instance.setRolloverId(rollover_id)
        self.bookmark_java_instance.setRangeTimeSize(second_batch_size)
        self.Time_class = self.gw.jvm.model.util.time.Time

    def create_bookmark(self, bookmark_name, initial_id, initial_time):
        self.bookmark_java_instance.setupBookmark(bookmark_name, initial_id,
                                                                         self.datetime_to_javaTime(initial_time))

    def get_last_record_time(self):
        return util.datetime_from_json(self.bookmark_java_instance.getLastBookmark().
                       getLastRecordTime().toString())

    def get_last_record_id(self):
        return self.bookmark_java_instance.getLastBookmark().getLastRecordId()

    def insert_bookmark(self, id, time, input_size, processed_size, process_starttime, process_endtime):
        bookmark = self.gw.jvm.model.bookmark.RecordBookmark()
        bookmark.setLastRecordId(id)
        bookmark.setLastRecordTime(self.datetime_to_javaTime(time))
        bookmark.setInputSize(input_size)
        bookmark.setProcessedSize(processed_size)
        bookmark.setProcessStarttime(self.datetime_to_javaTime(process_starttime))
        bookmark.setProcessEndtime(self.datetime_to_javaTime(process_endtime))
        return self.bookmark_java_instance.updateBookmark(bookmark)

    def insert_time(self, time):
        bookmark = self.gw.jvm.model.bookmark.RecordBookmark()
        bookmark.setLastRecordTime(self.datetime_to_javaTime(time))
        return self.bookmark_java_instance.updateBookmark(bookmark)

    def insert_id(self, id):
        bookmark = self.gw.jvm.model.bookmark.RecordBookmark()
        bookmark.setLastRecordId(id)
        return self.bookmark_java_instance.updateBookmark(bookmark)

    def id_iter(self, maxId):
        return self.bookmark_java_instance.getIdIterator(maxId)

    def time_iter(self, datetime_obj):
        return self.bookmark_java_instance.getTimeIterator(self.datetime_to_javaTime(datetime_obj))

    def delete_bookmark(self, name):
        return self.bookmark_java_instance.deleteBookmark(name)

    def set_last_bookmark(self, last_id, last_time):
        bookmark = self.gw.jvm.model.bookmark.RecordBookmark()
        bookmark.setLastRecordId(last_id)
        bookmark.setLastRecordTime(self.datetime_to_javaTime(last_time))
        self.bookmark_java_instance.setLastBookmark(bookmark)

    def datetime_to_javaTime(self,datetime_obj):
        if datetime_obj is None:
            return None;
        else:
            return self.Time_class.parse(util.datetime_to_json(datetime_obj))

