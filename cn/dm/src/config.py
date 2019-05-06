#coding="utf-8"




def Config(key=""):
    # host = "qaapis02.dongmanmanhua.cn"
    # httphost = "https://qaapis02.dongmanmanhua.cn"

    host = "qaptsapis.dongmanmanhua.cn"
    httphost = "https://qaptsapis.dongmanmanhua.cn"

    # host = "apis.dongmanmanhua.cn"
    # httphost = "https://apis.dongmanmanhua.cn"


    config = {"headers":{"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                         "HOST":host,
                         "Accept-Language":"zh-CN"},
              "httphost":httphost,
              "baseparams":{"platform":"APP_IPHONE",
                             "serviceZone":"CHINA",
                             "language":"zh-hans",
                             "locale":"zh_CN",
                             }}
    if key:
        return config[key]
    else:
        return config
