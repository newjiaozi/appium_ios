import requests
from .config import Config
import datetime,time
import hashlib
import base64
import rsa,binascii




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
    resp = requests.get(Config("httphost")+path,params=getExpiresMd5(path))
    resp_json = resp.json()
    # print(resp_json)
    evalue = resp_json["message"]["result"]["evalue"]
    keyName = resp_json["message"]["result"]["keyName"]
    nvalue = resp_json["message"]["result"]["nvalue"]
    sessionKey = resp_json["message"]["result"]["sessionKey"]
    return keyName,evalue,nvalue,sessionKey

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
    encpw = rsaEnc(ne[2], ne[1], ne[3], mobile=username, passwd=passwd)
    encnm = ne[0]
    plus = {"loginType":loginType,"encnm":encnm,"encpw":encpw,"v":1}
    plus.update(Config("baseparams"))
    resp = requests.post(Config("httphost")+path,headers=Config("headers"),data=plus,params= getExpiresMd5(path))
    return resp.json()["message"]["result"]["ses"]