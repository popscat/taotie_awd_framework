
import json

def submit(flag_queue):
    while 1:
        flag = flag_queue.get()
        rst = request.post(url=url,data={"flag":flag}).text
        