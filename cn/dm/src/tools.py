# coding="utf-8"

import requests
import base64,hashlib
import time,datetime
import rsa,binascii
from cn.dm.src.config import Config
import os
import json
import multiprocessing
import threading




oslinesep = os.linesep

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

def appHomeCard2(weekday):
    path ="/app/home/card2"
    payload = {"weekday":weekday,"v":3}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"))
    if resp.ok:
        result = {}
        resp_json = resp.json()
        # print(resp_json)
        ####处理更新页
        resulttmp = resp_json["message"]["result"]
        result["title"] = resulttmp["titleAndEpisodeList"].sort(key=lambda x:(x["mana",x["titleNo"]]),reverse=True)
        result["banner"] = resulttmp["noticeCard"]
        return result
    else:
        print(resp.text)

def appHome3(weekday):
    path ="/app/home3"
    payload = {"weekday":weekday,"v":3}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))

    resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"))
    if resp.ok:
        result = {}
        resp_json = resp.json()
        # print(resp_json)
        ####处理发现页bigbanner
        resulttmp = resp_json["message"]["result"]
        topBanner = resulttmp["topBanner"]["bannerList"]
        topBanner.sort(key=lambda x:x["bannerSeq"],reverse=True)
        result["bigbanner"] = topBanner
        ###咚漫推荐
        result["dongman"] = resulttmp["dongmanRecommendContentList"]
        ##barbanner
        result["barbanner"] = resulttmp["bannerPlacementList"]
        ##分类
        result["genre"] = resulttmp["genre"]
        ##主题
        result["theme"] = resulttmp["webtoon_collection_list"]
        ##排行榜，上升榜，新作榜，总榜
        result["uprank"] = resulttmp["ranking"]["titleWeeklyRanking"]
        result["newrank"] = resulttmp["ranking"]["titleNewRanking"]
        result["totalrank"] = resulttmp["ranking"]["titleTotalRanking"]
        ##新作登场
        result["new"] = resulttmp["homeNew"]
        ##佳作抢先看
        result["lead"] = resulttmp["leadUpLookList"]
        ##猜你喜欢
        result["like"] = resulttmp["recommend_map_list"]
        return result
    else:
        print(resp.text)

### 发现页的，新作
def appTitleList2():
    path ="/app/title/list2"
    payload = {"v":1}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"))
    if resp.ok:
        result = []
        resp_json = resp.json()
        # print(resp_json)
        resulttmp = resp_json["message"]["result"]
        tmp= resulttmp["titleList"]["titles"]
        result = list(filter(lambda x:x["newTitle"],tmp))

        genredict = appGenrelist2()
        for i in result:
            i["representGenre"]=genredict[i["representGenre"]]
        return result
    else:
        print(resp.text)

### 发现页的，排行
def appTitleRanking():
    path ="/app/title/ranking"
    payload = {"v":3,"rankingType":"ALL"}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"))
    if resp.ok:
        result = {}
        resp_json = resp.json()
        # print(resp_json)
        resulttmp = resp_json["message"]["result"]
        result["uprank"] = resulttmp["titleWeeklyRanking"]["rankList"]
        result["newrank"] = resulttmp["titleNewRanking"]["rankList"]
        result["totalrank"] = resulttmp["titleTotalRanking"]["rankList"]
        return result
    else:
        print(resp.text)

##获取genre  分类数据
def appGenrelist2():
    path ="/app/genreList2"
    payload = {"v":2}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"))
    if resp.ok:
        resp_json = resp.json()
        tmp = resp_json["message"]["result"]["genreList"]["genres"]
        dict1={}
        for i in tmp:
            dict1[i["code"]]=i["name"]
        # result["genre"] = dict1
        return dict1
    else:
        print(resp.text)



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

def login(username,passwd):
    path="/app/member/id/login"
    ne = appRsakeyGet()
    encpw = rsaEnc(ne[2], ne[1], ne[3], mobile=username, passwd=passwd)
    encnm = ne[0]
    plus = {"loginType":"PHONE_NUMBER","encnm":encnm,"encpw":encpw,"v":1}
    plus.update(Config("baseparams"))
    resp = requests.post(Config("httphost")+path,headers=Config("headers"),data=plus,params= getExpiresMd5(path))
    return resp.json()["message"]["result"]["ses"]

###返回三个titleName
def everyOneWatching(titleNoList=""):
    path="/app/myComics/everyoneWatching"
    if titleNoList:
        payload = {"respTitleCount":3,"titleNoList":titleNoList,"v":3}
    else:
        payload = {"respTitleCount":3,"v":3}

    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"))
    ranklist = resp.json()["message"]["result"]["ranklist"]
    titles = {}
    for i in ranklist:
        # titleName = i["webtoon"]["title"]
        # if titleName not in titles:
        titles[i["webtoon"]["title"]] = i["webtoon"]["titleNo"]
    return titles

def favouriteTitle():
    path="/app/favorite/totalList2"
    payload= {"v":3}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"))
    titles = resp.json()["message"]["result"]["titlelist"]["titles"]
    titleName = []
    for i in titles:
        titleName.append(i["title"])
    return titleName

def v1CommentOwnAll():
    path="/v1/comment/ownall"
    payload= {"limit":20,"pageNo":1,"flag":None,"_id":None}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    cookies={"NEO_SES":login("13683581996","qwe123")}
    resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"),cookies=cookies)
    commentObjectId=[]
    commentList= resp.json()["data"]["commentList"]
    for comment in commentList:
        commentObjectId.append(comment["objectId"])
    commentObjectId = list(set(commentObjectId))
    titleEpisodeinfo = appCommentTitleepisodeinfo2(commentObjectId)
    result=[]
    for comment in commentList:
        result.append(commentList["contents"])
    return result


def getGenreData(genre="all",status="all",sortby="人气"):
    genreDict = {"恋爱":"LOVE",
                 "少年":"BOY",
                 "古风":"ANCIENTCHINESE",
                 "奇幻":"FANTASY",
                 "搞笑": "COMEDY",
                 "校园": "CAMPUS",
                 "都市": "METROPOLIS",
                 "治愈": "HEALING",
                 "悬疑": "SUSPENSE",
                 "励志": "INSPIRATIONAL",
                 # "影视化":"FILMADAPTATION"
                 }
    statusDict = {"连载":"SERIES","完结":"TERMINATION"}
    sortList = ['人气','最新']
    path ="/app/title/list2"
    payload = {"v":1}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"))
    if resp.ok:
        result = []
        resp_json = resp.json()
        # print(resp_json)
        resulttmp = resp_json["message"]["result"]
        titles= resulttmp["titleList"]["titles"]
        genre = genre.strip().lower()
        status = status.strip().lower()
        sortby =  sortby.strip().lower()
        if genre == "all":
            if status == "all":
                if sortby == "人气":
                    titles.sort(key=lambda x:(x["mana"],x["titleNo"]),reverse=True)
                    print("ALL、ALL、人气:%s个" % len(titles))
                    for i in titles:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
                elif sortby == "最新":
                    titles.sort(key=lambda x:(x["lastEpisodeRegisterYmdt"],x["titleNo"]),reverse=True)
                    print("ALL、ALL、最新:%s个" % len(titles))
                    for i in titles:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
            elif status in statusDict:
                if sortby == "人气":
                    titles.sort(key=lambda x:(x["mana"],x["titleNo"]),reverse=True)
                    result = list(filter(lambda x:x["restTerminationStatus"]==statusDict[status],titles))
                    print("ALL、%s、人气:%s个" % (status,len(result)))
                    for i in result:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
                elif sortby == "最新":
                    titles.sort(key=lambda x:(x["lastEpisodeRegisterYmdt"],x["titleNo"]),reverse=True)
                    result = list(filter(lambda x:x["restTerminationStatus"]==statusDict[status],titles))
                    print("ALL、%s、最新:%s个" % (status,len(result)))
                    for i in result:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)

        elif genre in genreDict:
            if status == "all":
                if sortby == "人气":
                    titles.sort(key=lambda x:(x["mana"],x["titleNo"]),reverse=True)
                    result = list(filter(lambda x:genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],titles))
                    print("%s、ALL、人气:%s个" % (genre,len(result)))
                    for i in result:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
                elif sortby == "最新":
                    titles.sort(key=lambda x:(x["lastEpisodeRegisterYmdt"],x["titleNo"]),reverse=True)
                    result = list(filter(lambda x:genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],titles))
                    print("%s、ALL、最新:%s个" % (genre,len(result)))
                    for i in result:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
            elif status in statusDict:
                if sortby == "人气":
                    titles.sort(key=lambda x:(x["mana"],x["titleNo"]),reverse=True)
                    result = list(filter(lambda x:x["restTerminationStatus"]==statusDict[status],titles))
                    result = list(filter(lambda x:genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],result))
                    print("%s、%s、人气:%s个" % (genre,status,len(result)))
                    for i in result:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
                elif sortby == "最新":
                    titles.sort(key=lambda x:(x["lastEpisodeRegisterYmdt"],x["titleNo"]),reverse=True)
                    result = list(filter(lambda x:x["restTerminationStatus"]==statusDict[status],titles))
                    result = list(filter(lambda x:genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],result))
                    print("%s、%s、最新:%s个" % (genre,status,len(result)))
                    for i in result:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)

        elif genre == "影视化":
            if status == "all":
                if sortby == "人气":
                    titles.sort(key=lambda x:(x["mana"],x["titleNo"]),reverse=True)
                    result = list(filter(lambda x:x["filmAdaptation"],titles))
                    print("%s、ALL、人气:%s个" % (genre,len(result)))
                    for i in result:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
                elif sortby == "最新":
                    titles.sort(key=lambda x:(x["lastEpisodeRegisterYmdt"],x["titleNo"]),reverse=True)
                    result = list(filter(lambda x:x["filmAdaptation"],titles))
                    print("%s、ALL、最新:%s个" % (genre,len(result)))
                    for i in result:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
            elif status in statusDict:
                if sortby == "人气":
                    titles.sort(key=lambda x:(x["mana"],x["titleNo"]),reverse=True)
                    result = list(filter(lambda x:x["restTerminationStatus"]==statusDict[status],titles))
                    result = list(filter(lambda x:x["filmAdaptation"],result))
                    print("%s、%s、人气:%s个" % (genre,status,len(result)))
                    for i in result:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
                elif sortby == "最新":
                    titles.sort(key=lambda x:(x["lastEpisodeRegisterYmdt"],x["titleNo"]),reverse=True)
                    result = list(filter(lambda x:x["restTerminationStatus"]==statusDict[status],titles))
                    result = list(filter(lambda x:x["filmAdaptation"],result))
                    print("%s、%s、最新:%s个" % (genre,status,len(result)))
                    for i in result:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)


def appCommentTitleepisodeinfo2(telist):
    path="/app/comment/titleEpisodeInfo2"
    telist2Json = json.dumps(telist)
    payload = {"objectIdsJson":telist2Json}
    payload.update(Config("baseparams"))
    resp = requests.post(Config("httphost")+path,params=getExpiresMd5(path),data=payload,headers=Config("headers"))
    commentTitleEpisodeInfo = resp.json()["message"]["result"]["commentTitleEpisodeInfo"]
    return commentTitleEpisodeInfo





def appTitleList2oo(args):
    path ="/app/title/list2"
    payload = {"v":1}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    try:
        resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"))
        print(args, resp.status_code)
    except Exception as e:
        print(e.args)


def callBack(args):
    if args[1] != 200:
        print(args)

def multiProcess(target,pcount=10000,callback=callBack):
    pool = multiprocessing.Pool()
    for i in range(0,pcount):
        pool.apply_async(target,args=(i,),callback=callback)
    pool.close()
    start = datetime.datetime.now()
    print("multiprocessing start:%s " % start.strftime("%Y-%m-%d %H:%M:%S"))
    pool.join()
    end = datetime.datetime.now()
    print("multiprocessing end:%s " % end.strftime("%Y-%m-%d %H:%M:%S"))
    # print(type((end-start).total_seconds()))
    print("TPS: %.2f/s" % (pcount/(end-start).total_seconds()) )



def multiThread(target,pcount=1000):
    thread_list =[]
    for i in range(0,pcount):
        t = threading.Thread(target=target,args=(i,))
        thread_list.append(t)

    start = datetime.datetime.now()
    print("multiprocessing start:%s " % start.strftime("%Y-%m-%d %H:%M:%S"))
    for t in thread_list:
        t.start()
    for t in thread_list:
        t.join()
    end = datetime.datetime.now()
    print("multiprocessing end:%s " % end.strftime("%Y-%m-%d %H:%M:%S"))
    print("TPS: %.2f/s" % (pcount/(end-start).total_seconds()) )

if __name__=="__main__":
    # login("13683581996","qwe123")
    # genreDict = {"恋爱":"LOVE",
    #              "少年":"BOY",
    #              "古风":"ANCIENTCHINESE",
    #              "奇幻":"FANTASY",
    #              "搞笑": "COMEDY",
    #              "校园": "CAMPUS",
    #              "都市": "METROPOLIS",
    #              "治愈": "HEALING",
    #              "悬疑": "SUSPENSE",
    #              "励志": "INSPIRATIONAL",
    #              "影视化":"FILMADAPTATION"
    #              }
    # statusDict = {"连载":"SERIES","完结":"TERMINATION"}
    # sortList = ['人气','最新']
    #
    # getGenreData(
    #              genre="古风",
    #              status="完结",
    #              sortby="人气")
    # print(v1CommentOwnAll())
    multiThread(appTitleList2oo,pcount=55555555)

