
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

```
import common.services as service

#define unuque name for this bookmark
bookmark_name = "unique_bookmark_name"
bookmark_service=service.get("service_unique_name", {"bookmarkname":bookmark_name})



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
