#from py4j.java_gateway import JavaGateway

#gw = JavaGateway.launch_gateway(classpath="/home/eng-admin/IdeaProjects/LakeTools/LakeToolsCommon/target/LakeToolsCommon-1.0-SNAPSHOT.jar")

#bookmark_class=gw.jvm.service.bookmark.RecordBookmarkService

#gw.jvm.service.bookmark.RecordBookmarkService.setTest(True)
#gw.jvm.service.bookmark.RecordBookmarkService.setupBookmark("pyTest",77,None)

import common.services as services

mysql_service=services.get('local')

#mysql_service.sql('create table testTabl25 (col1 int not null)')

mysql_service.duplicate_update_subquery('table', 'select * from table 2', ['a','b'], ['c', 'd'],['e','f'])