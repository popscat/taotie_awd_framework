class WebBase():
    '''
    攻击类需要实现attack(ip:str)->tuple:
    一种是通过ssrf、任意文件读、sql注入拿到直接拿到flag，
    一种是通过文件上传、模版注入的方式达到的任意代码执行（php）和任意命令执行（shell）
    
    
    attack(ip):webshell,flag
    '''
    def attack(self,ip:str)->tuple:
        pass