from py4j.java_gateway import JavaGateway

from common.util import util

class BookmarkService:
    bookmark_java_instance = None;
    Time_class = None;
    gw = None;

    def __init__(self, config):
        self.gw = JavaGateway.launch_gateway(classpath=config['classpath'])
        self.bookmark_java_instance = self.gw.jvm.service.bookmark.RecordBookmarkService(
            config['bookmark_name'],config['filepath'],config['filepattern'])
        self.Time_class = self.gw.jvm.model.util.time.Time

    def get_fresh_files(self):
        return self.bookmark_java_instance.getFreshFiles()

    def filter_complete_files(self, file_list):
        return self.bookmark_java_instance.filterCompleteFiles(file_list)

    def insert_bookmark(self, name, input_size, processed_size, process_starttime, process_endtime):
        bookmark = self.gw.jvm.model.bookmark.FileBookmark()
        bookmark.setFilename(name)
        bookmark.setInputSize(input_size)
        bookmark.setProcessedSize(processed_size)
        bookmark.setProcessStarttime(self.datetime_to_javaTime(process_starttime))
        bookmark.setProcessEndtime(self.datetime_to_javaTime(process_endtime))
        return self.bookmark_java_instance.updateBookmark(bookmark)

    def insert_filename(self, name):
        return self.insert_bookmark(name);

    def delete_bookmark(self, name):
        return self.bookmark_java_instance.deleteBookmark(name)

    def datetime_to_javaTime(self,datetime_obj):
        if datetime_obj is None:
            return None;
        else:
            return self.Time_class.parse(util.datetime_to_json(datetime_obj))