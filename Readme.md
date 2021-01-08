
<H1>Installation</H1>

```
#setup path for RapidEtl project
RAPIDETLPATH=/path/to/your/project/rapidEtl-0.0.0

#for now using libs from venv/
RAPIDETLLIBSPATH=$RAPIDETLPATH/venv/lib/python3.6/site-packages/:$RAPIDETLPATH/venv/share

export PYTHONPATH=$PYTHONPATH:$RAPIDETLPATH:$RAPIDETLLIBSPATH

```

<H1> setting up bookmark</H1>

need to figure out how to automaticly get this binary into common/reources:
https://drive.google.com/drive/folders/1L8ni2IIagJZerj8z2oQT1rNbSHRgqtur?usp=sharing

<H1> working with rapid etl</H1>
Create new bookmark - record bookmark can use either record id or record time or both

```
>> bookmark_service=service.get("service_unique_name", {"bookmarkname":"tool_bookmark"})
>> bookmark_service.create_bookmark("tool_bookmark", 254, "1994-12-31")
```

```
import common.services as service
from datetime import datetime

import common.services as service

#define unique name for this bookmark
bookmark_name = "unique_bookmark_name"
bookmark_service=service.get("service_unique_name", {"bookmarkname":bookmark_name})

mysql=service.get("mysql_service")

last_recordId=bookmark_service.get_last_record_id()
recent_recordId=mysql.sql("select max(id) from library")[0]

if last_recordId < recent_recordId:
    #perform needed calculations here
    #if processing is sucessful store more recent bookmark
    bookmark_service.insert_id(recent_recordId)






#time based bookmark
last_recordTime=bookmark_service.get_last_record_time()
recent_recordTime=mysql.sql("select max(publication_date) from library")[0]
if last_recordTime < recent_recordTime
    #perform needed calculations here
    #if processing is sucessful store more recent bookmark
    bookmark_service.insert_time(recent_recordTime)





#smarter bookmark with iterator & rollover
bookmark_name = "unique_bookmark_name"
bookmark_service=service.get("service_unique_name", {"bookmarkname":bookmark_name, "id_batch_size":1000, "rollover_id":9223372036854775807})

mysql=service.get("mysql_service")

last_recordId=bookmark_service.get_last_record_id()
#safe id query, this can help identify when id rolled over
recent_recordId=mysql.sql("select max(id) from library where publication_date=(select max(publication_date) from library)")[0]

process_start = datetime.now()
iterator = bookmark_service.id_iter(recent_recordId)
if iterator.hasNext():
    #loop to batch process data
    while iterator.hasNext():
        iterator.next()
        batch_start=iterator.getRangeStart()
        batch_end=iterator.getRangeEnd()
        #perform processing between ids batch_start and batch_end

    process_end = datetime.now()
    input_size=iterator.getRangeEnd() - last_recordId #optional value, assuming here that input size for processing is number of processed id
    processed_size=0 #optional value, user can define how to calculate the size post processed data
    bookmark_service.insert_bookmark(iterator.getRangeEnd(), None, input_size, processed_size, process_start, process_end)






bookmark_name = "unique_bookmark_name"
bookmark_service=service.get("service_unique_name", {"bookmarkname":bookmark_name, "second_batch_size":3600})

mysql=service.get("mysql_service")

last_recordTime=bookmark_service.get_last_record_time()
recent_recordTime=mysql.sql("select max(publication_date) from library")[0]

iterator = bookmark_service.time_iter(recent_recordTime)
if iterator.hasNext():
    #loop to batch process data
    while iterator.hasNext():
        iterator.next()
        batch_start=iterator.getRangeStart().mysqlString()
        batch_end=iterator.getRangeEnd().mysqlString()
        #perform processing between batch_start and batch_end times
        
    bookmark_service.insert_bookmark(None, iterator.getRangeEnd(), None, None, None, None)
    

```

configuration

```
{"service_name0": {
  "type": "mysql",
  "config": {"db":"database_name",
              "user":"user",
              "password":"",
              "host":"localhost",
              "auth_plugin":"mysql_native_password"}
},
"bookmark_name": {
  "type": "record_bookmark",
  "config": {"classpath":"/path/to/LakeToolsCommon/Jar"}
},
"mongodb_name": {
  "type": "mongodb",
  "config": {"db":"database_name",
              "user":"user",
              "password":"",
              "host":"localhost",
              "port":"",
              "options":{}}
},
"logger_name": {
  "type": "logger",
  "config": {"logger_path":"path/to/store/log/files"}
},
"spark_name": {
  "type": "spark",
  "config": {"master_ip":"",
             "master_port":"",
             "options":{}}
}
}
```
