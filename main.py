from lib import flag,maintain,monitor,logger,config,attacklib,request

from threading import Thread
from multiprocessing import Queue 

#日志记录
log = logger.log

#引入消息队列
flag_queue = Queue()
webshells = {}
exploits = {}
tasks = []
cfg = config.get_config()
#加载新的攻击方法
tasks.append(Thread(target=monitor.init,args=(exploits,log)))

#获取webshell、flag线程
tasks.append(Thread(target=attacklib.run,args=(cfg,exploits,webshells,flag_queue,log)))

#flag提交线程
tasks.append(Thread(target=flag.submit,args=(flag_queue,log,cfg)))

#webshell权限维持线程
tasks.append(Thread(target=maintain.maintain,args=(webshells,log)))



if __name__ == '__main__':
    for task in tasks:
        task.start()