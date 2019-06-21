#coding="utf-8"

from faker import Faker

f=Faker()
def Config(key=""):
    host = "qaapis02.dongmanmanhua.cn"
    httphost = "https://qaptsapis.dongmanmanhua.cn"
    mobile="13683581996"
    passwd="qwe123"
    email = "weixindogs@163.com"
    loginType="EMAIL"

    # host = "qaptsapis.dongmanmanhua.cn"
    # httphost = "https://qaptsapis.dongmanmanhua.cn"
    # httphost = "http://10.40.129.212:8883"

    # host = "apis.dongmanmanhua.cn"
    # httphost = "https://apis.dongmanmanhua.cn"


    config = {"headers":{"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                         "HOST":host,
                         "Accept-Language":"zh-CN",
                         "x-Forwarded-For":getIpv4()},
              "httphost":httphost,
              "baseparams":{"platform":"APP_IPHONE",
                             "serviceZone":"CHINA",
                             "language":"zh-hans",
                             "locale":"zh_CN",
                             },
              "mobile":mobile,
              "passwd":passwd,
              "email":email,
              "loginType":loginType,

              "qamysql":{"host":"rm-2ze984p4ljnijqtg1.mysql.rds.aliyuncs.com",
               "port":3306,
               "user":"rmtroot",
               "passwd":"dmdb2050mCn",
               "db":"webtoon",
               },

              }

    if key:
        return config[key]
    else:
        return config

def getIpv4():
    return f.ipv4()