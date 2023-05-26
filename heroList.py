import os
import re

import pymysql
import requests
#hero_list
url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2808294"
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"}
req = requests.get(url,headers = headers)
json1 = req.json()
heroIdList = []
for x in json1["hero"]:
    heroIdList.append(x["heroId"])
herosInfoList = []
for x in heroIdList:
    url1 = f"https://game.gtimg.cn/images/lol/act/img/js/hero/{x}.js?ts=2808295"
    req2 = requests.get(url1,headers = headers)
    json2 = req2.json()
    #初始化一个英雄信息存放列表
    heroInfoList = []
    hero = json2["hero"]
    heroname = hero["name"]
    heroInfoList.append(heroname)
    #英雄价格
    goldPrice = hero["goldPrice"]
    heroInfoList.append(goldPrice)
    #护甲值
    armor = hero["armor"]
    heroInfoList.append(armor)
    #护甲成长值
    armorperlevel = hero["armorperlevel"]
    heroInfoList.append(armorperlevel)
    #攻击伤害
    attackdamage = hero["attackdamage"]
    heroInfoList.append(attackdamage)
    #攻击成长伤害
    attackdamageperlevel = hero["attackdamageperlevel"]
    heroInfoList.append(attackdamageperlevel)
    #攻击范围
    attackrange = hero["attackrange"]
    heroInfoList.append(attackrange)
    #攻击速度
    attackspeed = hero["attackspeed"]
    heroInfoList.append(attackspeed)
    #攻速成长值
    attackspeedperlevel = hero["attackspeedperlevel"]
    heroInfoList.append(attackspeedperlevel)
    #伤害模式
    damageType = hero["damageType"]
    heroInfoList.append(damageType)
    #难易度
    difficulty = hero["difficulty"]
    heroInfoList.append(difficulty)
    #初始血量
    hp = hero["hp"]
    heroInfoList.append(hp)
    #成长血量值
    hpperlevel = hero["hpperlevel"]
    heroInfoList.append(hpperlevel)
    #回复
    hpregen = hero["hpregen"]
    heroInfoList.append(hpregen)
    #成长回复值
    hpregenperlevel = hero["hpregenperlevel"]
    heroInfoList.append(hpregenperlevel)
    #移速
    mobility = hero["mobility"]
    heroInfoList.append(mobility)
    #蓝量
    mp = hero["mp"]
    heroInfoList.append(mp)
    #成长蓝量值
    mpperlevel = hero["mpperlevel"]
    heroInfoList.append(mpperlevel)
    #蓝量回复
    mpregen = hero["mpregen"]
    heroInfoList.append(mpregen)
    #蓝量回复等级
    mpregenperlevel = hero["mpregenperlevel"]
    heroInfoList.append(mpregenperlevel)
    #将每一个英雄的信息存放在列表中
    herosInfoList.append(heroInfoList)
#获取链接
con = pymysql.Connect(host="localhost",database="lol",user="root",passwd="",charset="utf8")
#获取游标
cursor = con.cursor()
#处输入数据
cursor.executemany("insert into hero_info values (null,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",herosInfoList)
#提交数据
con.commit()
cursor.close()
con.close()