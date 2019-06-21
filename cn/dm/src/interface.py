# coding="utf-8"

import requests
import base64,hashlib
import time,datetime
from cn.dm.src.config import Config
import os
import json
import multiprocessing
import threading
import faker
from cn.dm.src.login import login
import pymysql
import redis


oslinesep = os.linesep
fake = faker.Faker()

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
        # print(resp.text)
        # print(resp_json)
        ####处理更新页
        resulttmp = resp_json["message"]["result"]
        # print(resulttmp)
        if weekday == "COMPLETE":
            resulttmp["titleAndEpisodeList"].sort(key=lambda x: x["titleNo"], reverse=True)
            result["title"] = resulttmp["titleAndEpisodeList"]

        else:
            resulttmp["titleAndEpisodeList"].sort(key=lambda x:(x["mana"],x["titleNo"]),reverse=True)
            result["title"] = resulttmp["titleAndEpisodeList"]
            resulttmp["noticeCard"].sort(key=lambda x:int(x["exposurePosition"]))
            result["banner"] = resulttmp["noticeCard"]
        telist = []
        for i in result["title"]:
            rg = i["representGenre"]
            i["representGenre"]= genrelist[rg]
            telist.append("%s-%s" % (i["titleNo"], i["episodeNo"]))
        result["titleEpisodeNos"] = telist
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

### 发现页的，
# [{
# titleNo: 1262,
# language: "SIMPLIFIED_CHINESE",
# viewer: "SCROLL",
# title: "QA 13",
# writingAuthorName: "1-antiboss",
# pictureAuthorName: "1-antiboss",
# representGenre: "ANCIENTCHINESE",
# restTerminationStatus: "SERIES",
# restNotice: "",
# newTitle: false,
# hotTitle: false,
# ageGradeNotice: false,
# theme: "white",
# registerYmdt: 1523968575000,
# genreNewNo: 7,
# filmAdaptation: false,
# coinType: 0,
# defaultPrice: 0,
# thumbnail: "/88c7c38c-81d4-4455-b9c2-1bf0ed53864f.png",
# thumbnailIpad: "/43d1885d-daf6-448b-8c39-a32136a41f24.jpg",
# bgNewMobile: "/b1fa954c-952e-4913-9c46-c9dfc6f995b1.jpg",
# bgNewIpad: "/8158663d-33b9-4686-9f42-060a21653560.jpg",
# wideThumbnail: "/533898b7-ca3f-4072-91a0-cc7726d3d694.jpg",
# starScoreAverage: 0,
# readCount: 2976,
# favoriteCount: 0,
# mana: 0,
# rankingMana: 0,
# lastEpisodeRegisterYmdt: 1524050394000,
# groupName: "1-antiboss",
# synopsis: "QA 13",
# shortSynopsis: "QA 13",
# likeitCount: 0,
# latestEpisodeNo: 0,
# subGenre: [],
# weekday: [],
# totalServiceEpisodeCount: 5,
# serviceStatus: "SERVICE",
# titleWeekday: {},
# titleForSeo: "qa-13"
# }]

def appTitleList2(all=True):
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
        if all:
            return tmp
        else:
            result = list(filter(lambda x:x["newTitle"],tmp))
            genredict = appGenrelist2(False)
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
###
#[
# {
# color: "FF337F",
# index: 1,
# code: "LOVE",
# name: "恋爱"
# },
# {
# color: "046AFA",
# index: 2,
# code: "BOY",
# name: "少年"
# }]
def appGenrelist2(all=True):
    path ="/app/genreList2"
    payload = {"v":2}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"))
    if resp.ok:
        resp_json = resp.json()
        tmp = resp_json["message"]["result"]["genreList"]["genres"]
        if all:
            return tmp
        else:
            dict1={}
            for i in tmp:
                dict1[i["code"]]=i["name"]
            # result["genre"] = dict1
            return dict1
    else:
        print(resp.text)





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
    cookies={"NEO_SES":neo_ses}
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
                    if status == "完结":
                        titles.sort(key=lambda x:(x["likeitCount"],x["titleNo"]),reverse=True)
                        result = list(filter(lambda x:x["restTerminationStatus"]==statusDict[status],titles))
                        print("ALL、%s、人气:%s个" % (status,len(result)))
                        for i in result:
                            print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
                    else:
                        titles.sort(key=lambda x: (x["mana"], x["titleNo"]), reverse=True)
                        result = list(filter(lambda x: x["restTerminationStatus"] == statusDict[status], titles))
                        print("ALL、%s、人气:%s个" % (status, len(result)))
                        for i in result:
                            print(i['title'], i["subGenre"], i['restTerminationStatus'], i["mana"], i["titleNo"],
                                  "%s" % oslinesep)
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
                    result = list(filter(lambda x:genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"] ,titles))
                    print("%s、ALL、人气:%s个" % (genre,len(result)))
                    for i in result:
                        print(i['title'],i["representGenre"],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
                elif sortby == "最新":
                    titles.sort(key=lambda x:(x["lastEpisodeRegisterYmdt"],x["titleNo"]),reverse=True)
                    result = list(filter(lambda x:genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],titles))
                    print("%s、ALL、最新:%s个" % (genre,len(result)))
                    for i in result:
                        print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
            elif status in statusDict:
                if sortby == "人气":
                    if status == "完结":
                        titles.sort(key=lambda x:(x["likeitCount"],x["titleNo"]),reverse=True)
                        result = list(filter(lambda x:x["restTerminationStatus"]==statusDict[status],titles))
                        result = list(filter(lambda x:genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],result))
                        print("%s、%s、人气:%s个" % (genre,status,len(result)))
                        for i in result:
                            print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
                    else:
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
                    if status == "完结":
                        titles.sort(key=lambda x:(x["likeitCount"],x["titleNo"]),reverse=True)
                        result = list(filter(lambda x:x["restTerminationStatus"]==statusDict[status],titles))
                        result = list(filter(lambda x:x["filmAdaptation"],result))
                        print("%s、%s、人气:%s个" % (genre,status,len(result)))
                        for i in result:
                            print(i['title'],i["subGenre"],i['restTerminationStatus'],i["mana"],i["titleNo"],"%s" % oslinesep)
                    else:
                        titles.sort(key=lambda x:(x["mana"],x["titleNo"]),reverse=True)
                        result = list(filter(lambda x:x["restTerminationStatus"]==statusDict[status],titles))
                        result = list(filter(lambda x:genreDict[genre] in x["subGenre"] or genreDict[genre] == x["representGenre"],result))
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


def appMyFavorite2():
    path ="/app/myFavorite2"
    payload = {"v":3,"sortOrder":"UPDATE"}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    cookies={"NEO_SES":neo_ses}
    try:
        resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"),cookies=cookies)
        titleEpisodeList = resp["message"]["result"]["titleAndEpisodeList"]
        telist=[]
        for i in titleEpisodeList:
            telist.append("%s-%s" % (i["titleNo"],i["episodeNo"]))
        return telist,titleEpisodeList

    except Exception as e:
        print(e.args)

def v1TitleLikeAndCount(titleEpisodeNos):
    path ="/v1/title/likeAndCount"
    payload = {"titleEpisodeNos":titleEpisodeNos}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    cookies={"NEO_SES":neo_ses}
    try:
        resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"),cookies=cookies)
        data = resp["data"]
        return data

    except Exception as e:
        print(e.args)

def appFavouriteTotalList2():
    path="/app/favorite/totalList2"
    payload = {"v":3}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    cookies={"NEO_SES":neo_ses}
    try:
        resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"),cookies=cookies)
        return resp["data"][0]["like"],resp["data"][0]["count"]
    except Exception as e:
        print(e.args)



def appGetHotWordNew():
    path = "/app/getHotWordNew"
    payload = {}
    payload.update(Config("baseparams"))
    payload.update(getExpiresMd5(path))
    cookies={"NEO_SES":neo_ses}
    try:
        resp = requests.get(Config("httphost")+path,params=payload,headers=Config("headers"),cookies=cookies)
        return resp["message"]["result"]["getHotWordNew"]
    except Exception as e:
        print(e.args)



def v1Comment(titleNo,episodeNo,text=""):
    path = "/v1/comment"
    titleNo = str(titleNo)
    episodeNo = str(episodeNo)
    text = str(text)
    objectId = "w_"+titleNo+"_"+episodeNo
    time_now = datetime.datetime.now()
    otherStyleTime = time_now.strftime("%Y-%m-%d %H:%M:%S")
    contents = text+"自动生成评论"+str(otherStyleTime)
    payload = {"categoryId":"",
               "categoryImage":"",
               "contents":contents,
               "episodeNo":episodeNo,
               "imageNo":"",
               "objectId":objectId,
               "titleNo":titleNo}
    payload.update(Config("baseparams"))
    cookies={"NEO_SES":neo_ses}
    try:
        resp = requests.post(Config("httphost")+path,params=getExpiresMd5(path),data=payload,headers=Config("headers"),cookies=cookies)
        print(resp.text)
        return resp.json()["code"]
    except Exception as e:
        print(e.args)


def initDataFromDB():
    ms = Config("qamysql")
    conn = pymysql.connect(ms['host'],ms['user'],ms['passwd'],ms['db'],ms["port"])
    cursor = conn.cursor()
    return conn,cursor

def getTitleFromMysql(platform,cursor):
    ## 获取所有title
    querySql = 'select title.title_no as tn,title.display_platform as dp from  title where title.language_code="SIMPLIFIED_CHINESE" and title.service_status_code = "SERVICE";'
    cursor.execute(querySql)
    title_platforms = cursor.fetchall()
    titles = []
    for tg in title_platforms: ##能被3整除pc可以访问，被5整除mweb可以访问7，和11，应该是app
        if tg[1] % platform == 0:
            titles.append(tg[0])
    # for genre,name,title in title_groups:
    #     print(genre,name,title)
    return titles

## 获取所有title对应的episode
def getEpisodeFromMysql(cursor,title):
    # print(title)
    ## 获取所有episode
    querySql = 'select episode_no from episode where service_status_code = "SERVICE" and title_no = %s'
    cursor.execute(querySql % title)
    episodes = cursor.fetchall()
    # print(episodes)
    newepisodes = []
    for e in episodes:
        newepisodes.append(e[0])
    # for etitle,eno in episodes:
    #     print(etitle.lower(),eno)
    # print(newepisodes)
    return newepisodes


def getAllTitleEpisode(platform):
    conn,cursor = initDataFromDB()
    title_episode = {}
    titles = getTitleFromMysql(platform,cursor)
    for title in titles:
        episodes = getEpisodeFromMysql(cursor,title)
        title_episode[title] = episodes
    conn.close()
    cursor.close()
    return title_episode


def deleteRedis(neo_id):
    # curTime = time.localtime()
    # str_timeB = str(curTime.tm_year)+str(curTime.tm_mon)+str(curTime.tm_mday)
    r = redis.Redis(host='r-2ze7889e17a315d4.redis.rds.aliyuncs.com', port=6379, password='dmred2017qUsa', db="0",decode_responses=True)
    pattern = "comment_frequency_*_%s" % neo_id
    k = r.keys(pattern=pattern)
    if k:
        r.delete(*k)
        print("redis删除成功 %s" % k)
    else:
        print("没有匹配到需要删除的redis")


def likeIt(titleNo,episodeNo,like=True):
    "https://qaapis02.dongmanmanhua.cn/v1/title/1288/episode/1/like?md5=hjORhXHriOgH0t2U3x6lXg&expires=1561087385855"
    path = "/v1/title/%s/episode/%s/like" % (titleNo,episodeNo)
    if like:
        flag = "like"
    else:
        print("取消点赞%s-%s" % (titleNo,episode))
        flag = "cancelLike"
    # titleNo = str(titleNo)
    # episodeNo = str(episodeNo)

    payload = {"flag":flag}
    payload.update(Config("baseparams"))
    cookies={"NEO_SES":neo_ses}
    try:
        resp = requests.post(Config("httphost")+path,params=getExpiresMd5(path),data=payload,headers=Config("headers"),cookies=cookies)
        print(resp.text)
        return resp.json()["code"]
    except Exception as e:
        print(e.args)



neo_ses = login(Config("email"),Config("passwd"),Config('loginType'))
list2data = appTitleList2()
genrelist = appGenrelist2(False)

if __name__=="__main__":
    # login("13683581996","1988oooo")
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
    #              genre="all",
    #              status="all",
    #              sortby="人气")
    # print(v1CommentOwnAll())
    # multiThread(appTitleList2oo,pcount=1000)
    # res =appHomeCard2("SUNDAY")
    # for i in res["title"]:
    #     print(i["title"],i["titleNo"],i["lastEpisodeRegisterYmdt"],i['mana'],i["updateKey"],i["likeitCount"])

    title_episode = getAllTitleEpisode(11)
    for title,episodes in title_episode.items():
        for episode in episodes:
            for i in range(0,1):
                code = v1Comment(title,episode,text=i)
                if code == 10005:
                    deleteRedis("3f92b1d0-0331-11e9-9c05-00163e06a3f6")
                likecode = likeIt(title,episode)
                if likecode == 10010:
                    likeIt(title, episode,like=False)
                    likeIt(title, episode)


