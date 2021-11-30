# import yaml
# with open('../config.yml') as f:
#     cfg = yaml.load(f)


def get_config():
    cfg = {
        "roundtime":600,  #每轮间隔的时间，单位：秒
        "flag":{   #submit 直接传入request函数提交flag
            "submit":{
                "url":"http://47.93.116.52:20006/flag.php",
                "method":"GET",
                "headers":{
                    "cookie":"a=b",
                    "user-agent":""
                },
                "data":{
                    "flag":"${flag}",
                    "token":"token"
                },
                "params":{
                    "flag":"${flag}",
                    "token":"token"
                },
            },
            "savepath":"{ROOT}/result/flag.txt",
            "success":"success"
        },
        "attack":{
            "web1":"47.93.116.52:24443-24445",
        },
    }
    return cfg
    