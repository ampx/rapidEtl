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
        import common.datasource.mysql as mysql
        return mysql.MySqlSource(service_config)
    elif type == 'record_bookmark':
        import common.bookmark.record_bookmark_service as record_bookmark_service
        return record_bookmark_service.BookmarkService(service_config)
    elif type == '':
        import common.bookmark.file_bookmark_service as file_bookmark_service
        return file_bookmark_service.BookmarkService(service_config)
    elif type == 'mongodb':
        import common.datasource.mongodb as mongodb
        return mongodb.MongoDBSource(service_config)
    elif type == 'spark':
        import common.datasource.spark as spark
        return spark.SparkSource(service_config)
    elif type == 'logger':
        import common.util.logger as logger
        return logger.Logger(service_config)
    elif type == 'bookmark':
        import common.bookmark.bookmark_service as bookmark_service
        return bookmark_service.Bookmark_Service(service_config)
