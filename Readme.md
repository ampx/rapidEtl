
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
<H2> bookmark service </H2>
Create new bookmark - record bookmark can use either record id or record time or both

```
>> import common.services as service
>> from datetime import datetime
>> bookmark_service=service.get("service_unique_name", {"bookmark_name":"tool_bookmark"})
>> bookmark_service.create_bookmark("tool_bookmark", 254, datetime.strptime("1994-12-31", "%Y-%m-%d"))
```

```python
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
```

time based bookmark

```python
last_recordTime=bookmark_service.get_last_record_time()
recent_recordTime=mysql.sql("select max(publication_date) from library")[0]
if last_recordTime < recent_recordTime
    #perform needed calculations here
    #if processing is sucessful store more recent bookmark
    bookmark_service.insert_time(recent_recordTime)
```

smarter bookmark with iterator & rollover

```python
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
```

time iterator bookmark

```python
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

<H2> Template Script for batch processing mysql data</H2>

```python
import argparse
from datetime import datetime

#get logger

parser=argparse.ArgumentParser()
parser.add_argument("-days_back", help="")
parser.add_argument("-start_time", help="")
parser.add_argument("-end_time", help="")
parser.add_argument("-batch_seconds", help="")
parser.add_argument("-start_id", help="")
parser.add_argument("-end_id", help="")
parser.add_argument("-batch_ids", help="")

args = vars(parser.parse_args())
days_back=start_time=end_time=batch_seconds=batch_ids=start_id=end_id=None
if args["days_back"] is not None:
    days_back = int(args["days_back"])
    start_time=(datetime.now() - datetime.timedelta(days=days_back)).replace(hour=0, minute=0, second=0, microsecond=0)
    end_time=(datetime.now() - datetime.timedelta(days=days_back)).replace(hour=23, minute=59, second=59, microsecond=999)
elif args["start_time"] is not None:
    start_time=datetime.strptime(args["start_time"], "%m-%d-%Y %H:%M:%S")
    if args["end_time"] is not None:
        end_time=datetime.strptime(args["end_time"], "%m-%d-%Y %H:%M:%S")
    else:
        end_time=datetime.now()

if args["batch_seconds"] is not None:
    batch_seconds=int(args["batch_seconds"])

if args["start_id"] is not None:
    start_id=int(args["start_id"])
if args["end_id"] is not None:
    end_id=int(args["end_id"])

if args["batch_ids"] is not None:
    batch_ids=int(args["batch_ids"])

mysql_service_name="mysql_service_name"
bookmark_service_name = "bookmark_service_name"
bookmark_name = "bookmark_name"
rollover_id=9223372036854775807#assuming signed bigint
mysql=service.get(mysql_service_name)
bookmark_service=service.get(bookmark_service_name, {"bookmarkname":bookmark_name, "id_batch_size":batch_ids, "second_batch_size":batch_seconds "rollover_id":rollover_id})

def time_processor(time_str_start, time_str_end):
    #define here time based processing

def id_processor(id_start, time end):
    #define here id based processing

if start_time is not None:#process using start_time & end_time
    bookmark_service.set_last_bookmark(None, start_time)
    iterator = bookmark_service.time_iter(end_id)
    if iterator.hasNext():
    #loop to batch process data
    while iterator.hasNext():
        iterator.next()
        batch_start=iterator.getRangeStart().mysqlString()
        batch_end=iterator.getRangeEnd().mysqlString()
        #perform processing between batch_start and batch_end times
        time_processor(batch_start, batch_end)
elif start_id is not None:#processing using user defined id range
    bookmark_service.set_last_bookmark(start_id, None)
    iterator = bookmark_service.id_iter(end_id)
    if iterator.hasNext():
        #loop to batch process data
        while iterator.hasNext():
            iterator.next()
            batch_start=iterator.getRangeStart()
            batch_end=iterator.getRangeEnd()
            id_processor(batch_start, batch_end)
        if batch_end < end_id:
            batch_start=batch_end
            batch_end=end_id
            id_processor(batch_start, batch_end)
else:#default processing using last bookmarked location 
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
            id_processor(batch_start, batch_end)

        process_end = datetime.now()
        input_size=iterator.getRangeEnd() - last_recordId #optional value, assuming here that input size for processing is number of processed id
        processed_size=0 #optional value, user can define how to calculate the size post processed data
        bookmark_service.insert_bookmark(iterator.getRangeEnd(), None, input_size, processed_size, process_start, process_end)
```

<H2> MongoDB </H2>

```python
query='{"_id": "apples", "qty": 5"}'
collection="collection_name"
df = get_df(query, collection)
df.head()
```

configuration

```json
{
    "service_name0": {
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
