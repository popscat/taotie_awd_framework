from lib import flag,webshell,monitor,log,config,attack

from threading import Thread
from multiprocessing import Queue 



#引入消息队列
flag_queue = Queue()
webshell_queue = Queue()
exploits = {}


#flag提交线程
task1 = Thread(target = flag.submit,args=(flag_queue))

#webshell权限维持线程
task2 = Thread(target = webshell.maintain,args=(webshell_queue,))

#获取webshell、flag线程
task3 = Thread(target = attack.run,args=())

#加载新的攻击方法
task4 = Thread(target= monitor.init,args = exploits)
if __name__ == '__main__':
    task1.start()
    task2.start()
    task3.start()