import requests
import json

def submit(flag_queue):
    while 1:
        flag = flag_queue.get()
        rst = requests.post(url,data={"flag":flag}).text
        