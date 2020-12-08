from py4j.java_gateway import JavaGateway

#gw = JavaGateway.launch_gateway(classpath="/home/eng-admin/IdeaProjects/LakeTools/LakeToolsCommon/target/LakeToolsCommon-1.0-SNAPSHOT.jar")
#gw = JavaGateway.launch_gateway(classpath="/home/eng-admin/common-services/tools:/home/eng-admin/common-services/tools/LakeToolsCommon-1.0-SNAPSHOT.jar")
#bookmark_class=gw.jvm.service.bookmark.RecordBookmarkService
#bookmark_class.setTest(True)
#bookmark_instance = bookmark_class.RecordBookmarkService("pythonTable")
#bookmark_instance = gw.jvm.service.bookmark.RecordBookmarkService("pythonTable")
#print(bookmark_instance.getLastBookmarkTime().toString())

#gw.jvm.service.bookmark.RecordBookmarkService.setTest(True)
#gw.jvm.service.bookmark.RecordBookmarkService.setupBookmark("pyTest",77,None)

import common.services as services
import dateutil.parser as dateparser

#mysql_service=services.get('local')

#mysql_service.sql('create table testTabl25 (col1 int not null)')

#mysql_service.duplicate_update_subquery('table', 'select * from table 2', ['a','b'], ['c', 'd'],['e','f'])




bookmark_name = "testBookmark34543"

bookmark_service = services.get("record_bookmark", {"bookmark_name":bookmark_name, "id_batch_size":7, "rollover_id":34})

bookmark_service.create_bookmark(bookmark_name, 0, None)
bookmark_service.insert_id(0)

iterator = bookmark_service.id_iter(34)
while iterator.hasNext():
    iterator.next()
    print('Start:' + str(iterator.getRangeStart()))
    print('End:' + str(iterator.getRangeEnd()))
    print('-----')
print('Inserting last range: ' + str(iterator.getRangeEnd()))
bookmark_service.insert_id(iterator.getRangeEnd())
print('**-----**')

iterator = bookmark_service.id_iter(34)
while iterator.hasNext():
    iterator.next()
    print('Start:' + str(iterator.getRangeStart()))
    print('End:' + str(iterator.getRangeEnd()))
    print('-----')
print('Inserting last range: ' + str(iterator.getRangeEnd()))
bookmark_service.insert_id(iterator.getRangeEnd())
print('**-----**')

iterator = bookmark_service.id_iter(2)
while iterator.hasNext():
    iterator.next()
    print('Start:' + str(iterator.getRangeStart()))
    print('End:' + str(iterator.getRangeEnd()))
    print('-----')
print('Inserting last range: ' + str(iterator.getRangeEnd()))
bookmark_service.insert_id(iterator.getRangeEnd())
print('**-----**')


iterator = bookmark_service.id_iter(7)
while iterator.hasNext():
    iterator.next()
    print('Start:' + str(iterator.getRangeStart()))
    print('End:' + str(iterator.getRangeEnd()))
    print('-----')
print('Inserting last range: ' + str(iterator.getRangeEnd()))
bookmark_service.insert_id(iterator.getRangeEnd())
print('**-----**')


from datetime import date, timedelta, datetime
from dateutil.parser import parse

bookmark_name = "testBookmark4435"

bookmark_service = services.get("record_bookmark", {"bookmark_name":bookmark_name, "second_batch_size":3500})

yesterday = date.today() - timedelta(days=1)
bookmark_service.create_bookmark(bookmark_name, None, yesterday)
bookmark_service.insert_time(yesterday)

print(bookmark_service.get_last_record_time())

iterator = bookmark_service.time_iter(datetime.now())
while iterator.hasNext():
    iterator.next()
    print('Start:' + iterator.getRangeStart().mysqlString())
    print('End:' + iterator.getRangeEnd().mysqlString())
    print('-----')

bookmark_service.insert_time(parse(iterator.getRangeEnd().toString()))