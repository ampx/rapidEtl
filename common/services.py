import common.datasource.mysql
import common.bookmark.record_bookmark_service
import json

from pathlib import Path

def get(service_name):
    with open(str(Path(__file__).parent) + '/config.json') as f:
        config = json.load(f)

    type = config[service_name]['type']
    config = config[service_name]['config']
    if type == 'mysql':
        return common.datasource.mysql.MySqlSource(config)
    elif type == 'record_bookmark':
        return common.bookmark.record_bookmark_service.BookmarkService(config)
