from common.bookmark.bookmark import Bookmark
from common.bookmark.bookmark_service import Bookmark_Service
import time

def create_context(bookmark_name):
    bookmark_url = "http://localhost:8080/bookmarks"
    bs = Bookmark_Service({"bookmark_url": bookmark_url})
    return bs.get_context(bookmark_name)

f = open("result.csv", "a")
bookmark_name = "load0"
interations = 1000000
bookmark_context = create_context(bookmark_name)
bookmark_context.create_bookmark(None)
f.write("name,iteration,write_time,read_time" + "\n")
for i in range(interations):
    writen_bookmark = Bookmark(metrics={"metric0": "value0", "metric1": "value1"})
    writen_bookmarks = [writen_bookmark]

    start_time = time.time()
    bookmark_context.update_bookmarks(writen_bookmarks)
    write_time = start_time - time.time()

    start_time = time.time()
    read_bookmark = bookmark_context.get_bookmarks(top=1)[0]
    read_time = start_time - time.time()
    #equate the resoluion of python internal and stored

    if writen_bookmark.metrics == read_bookmark.metrics:
        f.write(bookmark_name + "," + str(i) + "," + str(write_time) + "," + str(read_time) + "\n")
    else:
        f.write(bookmark_name + "," + str(i) + "," + str(-1) + "," + str(-1) + "\n")
        print("issues processing:" + str(writen_bookmark.toDict()))
f.close()
