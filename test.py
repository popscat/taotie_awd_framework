import yaml

cfg = {
    "roundtime":600,  #每轮间隔的时间，单位：秒
    "flag":{   #submit 直接传入request函数提交flag
        "submit":{
            "method":"POST",
            "header":{
                "cookie":"a=b",
                "user-agent":""
            },
            "data":{
                "flag":"${flag}",
                "token":"token"
            },
            "param":{
                "flag":"${flag}",
                "token":"token"
            },
        "savepath":"{ROOT}/result/flag.txt"

        }
    },
    "webshell":{   #
        "shell":[
            [
                '/var/www/html/.pops.php',
                'xxxx',
                'POST',
                'pops',
                1
            ],
            [
                '/var/www/html/.pops.php',
                'xxxx',
                'POST',
                'pops',
                1
            ],
            [
                '/var/www/html/.pops.php',
                'xxxx',
                'POST',
                'pops',
                1
            ],
        ],
        "savepath":"{ROOT}/result/flag.txt"

    },
    "attack":{
        "web1":"123.123.123.56-93:12-34",
        "web2":""
    },
}

with open('config.yml','w') as f:
    yaml.dump(cfg,f)


    