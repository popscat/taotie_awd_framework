import os,time


def init(exploits : dict):
    def deal(path):
        return '.{}.{}'.format(*path[:-3].split('/'))
    while 1:
        loaded_attack = {}
        for webname in os.scandir(dir):
            if webname.is_dir():
                exploits.setdefault(webname.name,[])
                for attack_file in os.scandir(webname.path):
                    if not loaded_attack.get(attack_file.path):
                        loaded_attack[attack_file.path] = 1
                        exploits[webname].append(__import__(deal(attack_file)))
        time.sleep(3)

