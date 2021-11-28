class WebBase:
    '''
    WEBctf题目基类，其他EXP需继承此类并实现下面几个方法
    总得攻击类型分为三种，需要通过定义类属性做出区分
    一种是通过ssrf、任意文件读、sql注入拿到直接拿到flag，
    一种是通过文件上传、模版注入的方式达到的任意代码执行（php）和任意命令执行（shell）
    
    
    attack(ip):webshell
    '''
    def __init__(self,IPs):
        self.IPs=IPs

    def run(self):
        pass
    def save_flag(self,flag):
        pass