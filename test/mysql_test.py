import common.services as services
import common.bookmark.model.record_bookmark as bookmark_model
from datetime import datetime

mysql_service=services.get('local')
bookmark_service=services.get('record_bookmark')
bookmark = bookmark_model
bookmark_name = 'bookmark_test4'
bookmark.bookmark_name=bookmark_name

bookmark_service.create_bookmark(bookmark_name, 34, datetime.now())
print(bookmark_service.get_last_record_time(bookmark_name))
print(bookmark_service.get_last_record_time(bookmark_name))
bookmark.record_id=35;
bookmark.record_time=datetime.now();
bookmark.input_size = 7.0;
bookmark.output_size = 9.0;
bookmark.process_start_time=datetime.now();
bookmark.process_end_time=datetime.now();
bookmark_service.updateBookmark(bookmark)
bookmark_service.updateBookmark(None, bookmark_name, 36, datetime.now())
