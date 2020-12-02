from datetime import datetime

def datetime_to_json(datetime_obj):
    return datetime_obj.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

def datetime_from_json(datetime_str):
    return datetime.strptime(datetime_str, "%Y-%m-%dT%H:%M:%S.%fZ")