class WebBase:
    '''
    WEB ctf题目基类，其他EXP需继承此类并实现下面几个方法
    get_ip
    attack
    save_flag
    '''
    def __init__(self,IPs):
        self.IPs = IPs

    def run(self):
        self.attack()

    def save_flag(self,flag):
        pass