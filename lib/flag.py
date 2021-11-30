from lib import request
import json

def submit(flag_queue,log,cfg):
    log.info('flag提交线程启动')
    #TODO 完善flag提交
    while 1:
        flag = flag_queue.get()
        cfg['flag']['submit']['data']['flag'] = flag
        cfg['flag']['submit']['params']['flag'] = flag
        rst = request.request(**cfg['flag']['submit']).text
        if cfg['flag']['success'] not in rst:
            log.warning('{}提交失败'.format(flag))