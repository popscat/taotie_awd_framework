import os,time


def init(exploits : dict ,log):
    def deal(path):  #加载指定文件的攻击类
        l = path[:-3].split('/')
        #attack/web1/a.py  attack.web1.a
        return eval('__import__("{}").{}.{}()'.format('.'.join(l),'.'.join(l[1:]),l[-1]))
    loaded_attack = {}
    while 1:
        for webname in os.scandir('attack'):
            if webname.name != '__pycache__' and webname.is_dir():
                exploits.setdefault(webname.name,[])
                for attack_file in os.scandir(webname.path):
                    if attack_file.name != '__pycache__' and not loaded_attack.get(attack_file.path):
                        log.info('新的攻击方法已添加{}'.format(attack_file.path))
                        loaded_attack[attack_file.path] = 1
                        exploits[webname.name].append(deal(attack_file.path))
        time.sleep(3)
