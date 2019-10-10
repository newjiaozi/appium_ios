import requests
import datetime,time
import hashlib
import base64
import rsa,binascii
import uuid
from cn.dm.src.logger import logger
import configparser


def getConfig(section,option):
    conf = configparser.ConfigParser()
    conf.read("config.ini")
    if conf.has_option(section,option):
        return conf.get(section,option)

def setConfig(section,option,value):
    conf = configparser.ConfigParser()
    conf.read("config.ini")
    if conf.has_section(section):
        pass
    else:
        conf.add_section(section)
    conf.set(section,option,value)
    conf.write(open("config.ini","r+"))

def Config(key,section="headers"):
    neo_ses = getConfig("session","neo_ses")
    host = getConfig(section,"host")
    httphost = getConfig(section,"httphost")
    phone_uuid = getConfig(section,"phone_uuid")
    mobile = getConfig(section,"mobile")
    passwd = getConfig(section,"passwd")
    email = getConfig(section,"email")
    loginType = getConfig(section,"loginType")
    env = getConfig(section,"env")
    userAgent = getConfig(section,"userAgent")

    config = {"headers":{"Content-Type":"application/x-www-form-urlencoded; charset=UTF-8",
                         "HOST":host,
                         "Accept-Language":"zh-CN",
                         # "x-Forwarded-For":"",
                         # "uuid":getUUID(),
                         "user-agent":userAgent
                         },
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
              "cookies":{"uuid":phone_uuid,"neo_ses":neo_ses},
              "env":env,
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


def getUUID():
    return "".join(str(uuid.uuid4()).split("-")).upper()


def getExpiresMd5(pathstr,skey="the_scret_key"):
    now30 = datetime.datetime.now() + datetime.timedelta(minutes=30)
    utime = str(int(time.mktime(now30.timetuple())))
    msg = utime+" "+pathstr+" "+skey
    m = hashlib.md5()
    m.update(msg.encode(encoding="utf-8"))
    msg_md5 = m.digest()
    msg_md5_base64 = base64.urlsafe_b64encode(msg_md5)
    msg_md5_base64_str = msg_md5_base64.decode("utf-8")
    msg_md5_base64_str = msg_md5_base64_str.replace("=", "")
    return {"md5":msg_md5_base64_str,"expires":utime}

def appRsakeyGet():
    path = "/app/rsakey/get"
    try:
        resp = requests.get(Config("httphost")+path,params=getExpiresMd5(path),headers=Config("headers"))
        resp_json = resp.json()
        evalue = resp_json["message"]["result"]["evalue"]
        keyName = resp_json["message"]["result"]["keyName"]
        nvalue = resp_json["message"]["result"]["nvalue"]
        sessionKey = resp_json["message"]["result"]["sessionKey"]
        logger.info(resp.url)
        return keyName,evalue,nvalue,sessionKey
    except Exception:
        logger.error("appRsakeyGet出现异常")
        logger.error(resp.url)
        logger.error(resp.text)
        logger.error(resp.headers)
        return False



def rsaEnc(rsa_n,rsa_e,sessionKey,mobile,passwd):
    rsa_e = rsa_e.lower()
    rsa_n = rsa_n.lower()
    key = rsa.PublicKey(int(rsa_e,16),int(rsa_n,16))
    message = chr(len(sessionKey))+sessionKey+chr(len(mobile))+mobile+chr(len(passwd))+passwd
    message = rsa.encrypt(message.encode(),key)
    message = binascii.b2a_hex(message)
    return message.decode()

def login(username,passwd,loginType="EMAIL"): ##PHONE_NUMBER
    path="/app/member/id/login"
    ne = appRsakeyGet()
    if ne:
        try:
            encpw = rsaEnc(ne[2], ne[1], ne[3], mobile=username, passwd=passwd)
            encnm = ne[0]
            plus = {"loginType":loginType,"encnm":encnm,"encpw":encpw,"v":1}
            plus.update(Config("baseparams"))
            resp = requests.post(Config("httphost")+path,headers=Config("headers"),data=plus,params= getExpiresMd5(path))
            resp_json = resp.json()
            logger.info(resp.url)
            neo_ses = resp_json["message"]["result"]["ses"]
            setConfig("session","neo_ses",neo_ses)
            return neo_ses,resp_json["message"]["result"]["idNo"]
        except Exception:
            logger.error("login出现异常")
            logger.error(resp.url)
            logger.error(resp.text)
            logger.error(resp.headers)
            return False
    else:
        return False

if __name__ == "__main__":
    # print(login("weixindogs@163.com","qwe123"))
    print(login(Config("mobile"), Config("passwd"), "PHONE_NUMBER")[0])