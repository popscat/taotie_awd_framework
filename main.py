from lib import flag,webshell,monitor,log,config,attack,request

from threading import Thread
from multiprocessing import Queue 



#引入消息队列
flag_queue = Queue()
webshells = []
exploits = {}

tasks = []
#flag提交线程
tasks.append(Thread(target=flag.submit,args=(flag_queue,)))

#webshell权限维持线程
tasks.append(Thread(target=webshell.maintain,args=(webshells,)))

#获取webshell、flag线程
tasks.append(Thread(target=attack.run,args=()))

#加载新的攻击方法
tasks.append(Thread(target=monitor.init,args=(exploits,)))
if __name__ == '__main__':
    for task in tasks:
        task.start()