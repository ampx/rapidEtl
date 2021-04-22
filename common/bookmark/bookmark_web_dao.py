import requests

from common.bookmark import bookmark
from common.bookmark.bookmark import Bookmark
from util import util

class Bookmark_Web_Dao:
    bookmark_url = "http://localhost:8080/bookmarks"

    def __init__(self, bookmark_url):
        self.bookmark_url = bookmark_url
        if self.bookmark_status() is False:
            raise ConnectionError("failed to connect to bookmark server")

    def bookmark_status(self):
        if requests.get(self.bookmark_url).status_code == 200:
            return True
        else:
            return False

    def bookmark_exists(self, bookmark_name):
        if requests.get(self.bookmark_url + "/" + bookmark_name).status_code == 200:
            return True
        else:
            return False


    def create_bookmark(self, bookmark_name, config):
        response = requests.put(self.bookmark_url, json={"name": bookmark_name, "config": config},
                                headers={'content-type': 'application/json'}).json()
        if 'success' in response:
            return response['success']
        else:
            return False

    def get_bookmarks(self, bookmark_name, starttime, endtime, top):
        params = {}
        if starttime is not None:
            params['from'] = util.datetime_to_json(starttime)
        if endtime is not None:
            params['endtime'] = util.datetime_to_json(endtime)
        if top is not None:
            params['top'] = top
        if len(params) > 0:
            response = requests.get(self.bookmark_url + "/" + bookmark_name + "/bookmark?data=*", params=params).json()
        else:
            response = requests.get(self.bookmark_url + "/" + bookmark_name + "/bookmark?data=*", params=params).json()
        return response

    def save_bookmark(self, bookmark_name, metrics):
        bookmark_list = []
        bookmark_list.append(Bookmark(metrics).toDict())
        url = self.bookmark_url + "/" + bookmark_name + "/bookmark"
        try:
            response = requests.post(url, json=bookmark_list,
                                     headers={'content-type': 'application/json'}).json()

            if 'success' in response:
                return response['success']
            else:
                return False
        except BaseException as error:
            raise TypeError(self.manual_update_post(bookmark_list, url)) from error


    def update_bookmark(self, bookmark_name, metrics):
        bookmark_list = []
        bookmark_list.append(Bookmark(metrics).toDict())
        url = self.bookmark_url + "/" + bookmark_name + "/bookmark"
        try:
            response = requests.put(url, json=bookmark_list,
                                     headers={'content-type': 'application/json'}).json()
            if 'success' in response:
                return response['success']
            else:
                return False
        except BaseException as error:
            raise TypeError(self.manual_update_put(bookmark_list, url)) from error

    def save_failed(self, bookmark_name, metrics):
        bookmark_list = []
        bookmark_list.append(Bookmark(metrics).toDict())
        url = self.bookmark_url + "/" + bookmark_name + "/failed"
        try:
            response = requests.post(url, json=bookmark_list,
                                     headers={'content-type': 'application/json'}).json()

            if 'success' in response:
                return response['success']
            else:
                return False
        except BaseException as error:
            raise TypeError(self.manual_update_post(bookmark_list, url)) from error


    def update_failed(self, bookmark_name, metrics):
        bookmark_list = []
        bookmark_list.append(Bookmark(metrics).toDict())
        url = self.bookmark_url + "/" + bookmark_name + "/failed"
        try:
            response = requests.put(url, json=bookmark_list,
                                     headers={'content-type': 'application/json'}).json()
            if 'success' in response:
                return response['success']
            else:
                return False
        except BaseException as error:
            raise TypeError(self.manual_update_put(bookmark_list, url)) from error

    def lock(self, bookmark_name):
        url = self.bookmark_url + "/" + bookmark_name + "/state"
        message = {"state":bookmark.locked}
        try:
            response = requests.put(url, json=,
                                    headers={'content-type': 'application/json'}).json()
            if 'success' in response:
                return response['success']
            else:
                return False
        except BaseException as error:
            raise TypeError(self.manual_update_put(message, url)) from error

    def unlock(self, bookmark_name):
        url = self.bookmark_url + "/" + bookmark_name + "/state"
        message = {"state":bookmark.unlocked}
        try:
            response = requests.put(url, json=,
                                    headers={'content-type': 'application/json'}).json()
            if 'success' in response:
                return response['success']
            else:
                return False
        except BaseException as error:
            raise TypeError(self.manual_update_put(message, url)) from error

    def mark_failed(self, bookmark_name):
        url = self.bookmark_url + "/" + bookmark_name + "/state"
        message = {"state":bookmark.failed}
        try:
            response = requests.put(url, json=,
                                    headers={'content-type': 'application/json'}).json()
            if 'success' in response:
                return response['success']
            else:
                return False
        except BaseException as error:
            raise TypeError(self.manual_update_put(message, url)) from error

    def manual_update_post(self, body, url):
        return "curl -d '" + str(body) + "' -H 'Content-Type: application/json' -X POST " + url

    def manual_update_put(self, body, url):
        return "curl -d '" + str(body) + "' -H 'Content-Type: application/json' -X POST " + url

    def manual_unlock(self, bookmark_name):
        return None