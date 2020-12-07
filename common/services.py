import common.datasource.mysql
import common.bookmark.record_bookmark_service
import json

from pathlib import Path

def get(service_name = None, service_config=None, services_config=None):

    if services_config is None:
        with open(str(Path(__file__).parent) + '/config.json') as f:
            services_config = json.load(f)

    service_config_default = services_config[service_name]['config']
    if service_config is None:
        service_config = service_config_default
    elif service_config_default is not None:
        for key in service_config_default.keys():
            if key not in service_config:
                service_config[key] = service_config_default[key]

    type = services_config[service_name]['type']
    if type == 'mysql':
        return common.datasource.mysql.MySqlSource(service_config)
    elif type == 'record_bookmark':
        return common.bookmark.record_bookmark_service.BookmarkService(service_config)
    elif type == 'mongodb':
        return common.datasource.mongodb.MongoDBSource(service_config)
