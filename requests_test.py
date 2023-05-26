import pymysql
import requests
import os
import lxml
from lxml import etree
#定义一个变量接收请求地址
url = "https://game.gtimg.cn/images/lol/act/img/js/heroList/hero_list.js?ts=2808294"
#带上一个请求头，告诉服务器我是一个什么样的浏览器
headers = {"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36 Edg/113.0.1774.50"}
#请求该网站、导入requests库、安装：pip install 库名
#第一个需要参数
rep = requests.get(url,headers = headers)
json = rep.json()
hero = json['hero']
heroId = []
for i in hero:
    heroId.append(int(i["heroId"]))
heroImg = []
for i in heroId:
    url = f"https://game.gtimg.cn/images/lol/act/img/js/hero/{i}.js?ts=2808297"
    hero = requests.get(url,headers=headers)
    a= hero.json()
    for j in a['skins']:
        # print(j)
        heroName = j['heroName']
        name = j["name"]
        os.makedirs(f"lol/{heroName}",exist_ok=True)
        mainImg = j['mainImg']
        if (name in "/"):
            name = str(name).replace("/"," ")
        if(mainImg != "" ):
            mainCon = requests.get(mainImg)
            try:
                with open(f"lol/{heroName}/{name}.jpg","wb") as f:
                    f.write(mainCon.content)
            except OSError:
                pass
            continue


