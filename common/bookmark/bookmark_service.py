import requests

from common.bookmark.bookmark_context import Bookmark_Context

"""
HEAD: /bookmarks - check if service is up
GET: /bookmarks?data=list return list of elements
POST: /bookmarks {"name":"bookmark_name"} - create bookmark
PUT: /bookmarks {"name":"bookmark_name"} - update bookmark

HEAD: /bookmarks/{bookmark_name} - check if bookmark exists - will respond with 404 if try to reach a non-existent bookmark
//TBD for bookmark metadata
GET: /bookmarks/{bookmark_name} 
PUT: /bookmarks/{bookmark_name} 
POST: /bookmarks/{bookmark_name} 
DELETE: /bookmarks/{bookmark_name}

GET: /bookmarks/{bookmark_name}/state - get state
PUT/POST: /bookmarks/{bookmark_name}/state {"state":0} - update state

GET: /bookmarks/{bookmark_name}/bookmark?data=* - get all bookmarks
?top=10 - TBD
?top=-10 - TBD
?from=2018-12-10T13:45:00Z&to=2018-12-11T13:45:00Z - TBD
PUT: /bookmarks/{bookmark_name}/bookmark - update bookmark
POST: /bookmarks/{bookmark_name}/bookmark - overwrite all existing bookmarks

GET: /bookmarks/{bookmark_name}/failed - get failed bookmark
PUT: /bookmarks/{bookmark_name}/failed - update failed bookmark
POST: /bookmarks/{bookmark_name}/failed - overwrite all existing failed bookmarks
"""




class Bookmark_Service:
    dao = None;

    def __init__(self, config):
        self.dao = dao


    def get_context(self, bookmark_name):
        return Bookmark_Context(bookmark_name, self.dao)




