import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json
import random
import datetime
import time
from time import sleep
from threading import Thread

print(time.time())
random.seed(time.time())
count = 0
total_count = 2000
proxy_list = []
article_list = []
cookie = list()
cookie.append({'cookie': 'HWWAFSESID=5841b7352fe00c9fd8; HWWAFSESTIME=1674003689588; uuid_tt_dd=10_19970426330-1674003834162-663687; dc_session_id=10_1674003834162.588556; c_pref=default; c_first_ref=default; c_first_page=https://blog.csdn.net/agonie201218/category_11159108.html; c_segment=7; dc_sid=d904cdc4d1e27b164d466b49ce26ae53; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1672103747,1672709220,1674003591; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac={"islogin":{"value":"0","scope":1},"isonline":{"value":"0","scope":1},"isvip":{"value":"0","scope":1}}; hide_login=1; firstDie=1; __gads=ID=7e9152aa51e379b0-225c7ef453d9005c:T=1674003833:RT=1674003833:S=ALNI_Mbw9ge8irY6APS86aicbuXLLsfevQ; __gpi=UID=00000ba65ce69ca7:T=1674003833:RT=1674003833:S=ALNI_MaQYXknz08npTV-1FoQSy43m-pCng; c_dsid=11_1674003841952.496591; FCNEC=[["AKsRol-yTjolYz_VlBMfzudC5UCFNmnLEpsFXW7o8TAVwVvUhaUWHvdwJf6-e__7Ni9ioF4V4uMEb3I0J1yVw7NN5J17Ci7LRPNZTjQ1ATrjTXCU06Czp8yPnNJm4DmOJLRDdpBtgeLuteXtfjl2sre8CNN9WQsW3w=="],null,[]]'})
User_Agent = [
    "Mozilla/5.0 (iPod; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "Mozilla/5.0 (iPhone; U; CPU iPhone OS 4_3_2 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Version/5.0.2 Mobile/8H7 Safari/6533.18.5",
    "MQQBrowser/25 (Linux; U; 2.3.3; zh-cn; HTC Desire S Build/GRI40;480*800)",
    "Mozilla/5.0 (Linux; U; Android 2.3.3; zh-cn; HTC_DesireS_S510e Build/GRI40) AppleWebKit/533.1 (KHTML, like Gecko) Version/4.0 Mobile Safari/533.1",
    "Mozilla/5.0 (SymbianOS/9.3; U; Series60/3.2 NokiaE75-1 /110.48.125 Profile/MIDP-2.1 Configuration/CLDC-1.1 ) AppleWebKit/413 (KHTML, like Gecko) Safari/413",
    "Mozilla/5.0 (iPad; U; CPU OS 4_3_3 like Mac OS X; zh-cn) AppleWebKit/533.17.9 (KHTML, like Gecko) Mobile/8J2",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_7_2) AppleWebKit/534.51.22 (KHTML, like Gecko) Version/5.1.1 Safari/534.51.22",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (iPhone; CPU iPhone OS 5_0 like Mac OS X) AppleWebKit/534.46 (KHTML, like Gecko) Version/5.1 Mobile/9A5313e Safari/7534.48.3",
    "Mozilla/5.0 (Windows NT 6.1) AppleWebKit/535.1 (KHTML, like Gecko) Chrome/14.0.835.202 Safari/535.1",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows Phone OS 7.5; Trident/5.0; IEMobile/9.0; SAMSUNG; OMNIA7)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; XBLWP7; ZuneWP7)",
    "Mozilla/5.0 (Windows NT 5.2) AppleWebKit/534.30 (KHTML, like Gecko) Chrome/12.0.742.122 Safari/534.30",
    "Mozilla/5.0 (Windows NT 5.1; rv:5.0) Gecko/20100101 Firefox/5.0",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.2; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.2; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/4.0 (compatible; MSIE 60; Windows NT 5.1; SV1; .NET CLR 2.0.50727)",
    "Mozilla/5.0 (compatible; MSIE 9.0; Windows NT 6.1; Trident/5.0; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)",
    "Opera/9.80 (Windows NT 5.1; U; zh-cn) Presto/2.9.168 Version/11.50",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1)",
    "Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.04506.648; .NET CLR 3.5.21022; .NET4.0E; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C)",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; zh-CN) AppleWebKit/533.21.1 (KHTML, like Gecko) Version/5.0.5 Safari/533.21.1",
    "Mozilla/5.0 (Windows; U; Windows NT 5.1; ) AppleWebKit/534.12 (KHTML, like Gecko) Maxthon/3.0 Safari/534.12",
    "Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; TheWorld)"
]

payload = ""
# 请求头
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Cookie": "l=AurqcPuigwQdnQv7WvAfCoR1OlrRQW7h; isg=BHp6mNB79CHqYXpVEiRteXyyyKNcg8YEwjgLqoRvCI3ddxqxbLtOFUBGwwOrZ3ad; thw=cn; cna=VsJQERAypn0CATrXFEIahcz8; t=0eed37629fe7ef5ec0b8ecb6cd3a3577; tracknick=tb830309_22; _cc_=UtASsssmfA%3D%3D; tg=0; ubn=p; ucn=unzbyun; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=981798063989731689; hng=CN%7Czh-CN%7CCNY%7C156; um=0712F33290AB8A6D01951C8161A2DF2CDC7C5278664EE3E02F8F6195B27229B88A7470FD7B89F7FACD43AD3E795C914CC2A8BEB1FA88729A3A74257D8EE4FBBC; enc=1UeyOeN0l7Fkx0yPu7l6BuiPkT%2BdSxE0EqUM26jcSMdi1LtYaZbjQCMj5dKU3P0qfGwJn8QqYXc6oJugH%2FhFRA%3D%3D; ali_ab=58.215.20.66.1516409089271.6; mt=ci%3D-1_1; cookie2=104f8fc9c13eb24c296768a50cabdd6e; _tb_token_=ee7e1e1e7dbe7; v=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64;` rv:47.0) Gecko/20100101 Firefox/47.0"
}


def mapUrl(x):
    print("xxx")
    print(x)
    print(x['url'])
    return x['url']


def getList(url):  # 获取用户首页的文章列表
    resp = requests.request("GET", url, data=payload, headers=headers)  # 发送请求
    # resp.encoding = resp.apparent_encoding  # 设置解码方式
    json = resp.json()
    list = json['data']['list']
    # print(json['data']['list'])

    # new_urls = map(mapUrl, json['data']['list'])
    # print(new_urls)
    # html_source = resp.text
    # # 通过正则表达式，从获取的HTML代码中提取出链接
    # urls = re.findall("https://[^>\";\']*\d", html_source)
    new_urls = []
    for url in list:
        new_urls.append(url['url'])
    print(new_urls)
    return new_urls


def get_proxy_list():
    for row in urlopen('http://proxylist.fatezero.org/proxy.list').readlines():
        item = json.loads(row)
        if item['type'] == 'http' and item['anonymity'] == 'high_anonymous' and item['response_time'] < 7:
            proxy_list.append(item['host']+':'+str(item['port']))


def solve():

    global count
    sleep(random.randint(0, 600))
    article = article_list[random.randint(0, len(article_list)-1)]
    proxy = {'http': proxy_list[random.randint(0, len(proxy_list)-1)]}
    header = {'User-Agent': User_Agent[random.randint(0, len(User_Agent)-1)],
              'referer': 'https://blog.csdn.net'}
    try:
        requests.get(article.replace('https', 'https'), headers=header, proxies=proxy,
                     cookies=cookie[random.randint(0, len(cookie)-1)], timeout=7)
        count = count + 1
        print('ok ip:'+proxy['http'] + ', count:' + str(count))
    except:
        print('no')
        try:
            proxy_list.remove(proxy['http'])
        except:
            pass


# article_list = getList(
#     "https://blog.csdn.net/community/home-api/v1/get-business-list?page=2&size=100&businessType=blog&noMore=false&username=agonie201218")
article_list = ['https://andyoung.blog.csdn.net/article/details/127647523', 'https://andyoung.blog.csdn.net/article/details/127643437', 'https://andyoung.blog.csdn.net/article/details/127632052', 'https://andyoung.blog.csdn.net/article/details/127631073', 'https://andyoung.blog.csdn.net/article/details/127646405', 'https://andyoung.blog.csdn.net/article/details/127615445', 'https://andyoung.blog.csdn.net/article/details/127545170', 'https://andyoung.blog.csdn.net/article/details/127531162', 'https://andyoung.blog.csdn.net/article/details/127617954', 'https://andyoung.blog.csdn.net/article/details/127610437', 'https://andyoung.blog.csdn.net/article/details/127604667', 'https://andyoung.blog.csdn.net/article/details/127604763', 'https://andyoung.blog.csdn.net/article/details/127604291', 'https://andyoung.blog.csdn.net/article/details/127530680', 'https://andyoung.blog.csdn.net/article/details/127529692', 'https://andyoung.blog.csdn.net/article/details/127569390', 'https://andyoung.blog.csdn.net/article/details/127529179', 'https://andyoung.blog.csdn.net/article/details/127545010', 'https://andyoung.blog.csdn.net/article/details/127530807', 'https://andyoung.blog.csdn.net/article/details/127528084', 'https://andyoung.blog.csdn.net/article/details/127527105', 'https://andyoung.blog.csdn.net/article/details/127526744', 'https://andyoung.blog.csdn.net/article/details/127491699', 'https://andyoung.blog.csdn.net/article/details/127490677', 'https://andyoung.blog.csdn.net/article/details/127488380', 'https://andyoung.blog.csdn.net/article/details/127487696', 'https://andyoung.blog.csdn.net/article/details/127487074', 'https://andyoung.blog.csdn.net/article/details/127472301', 'https://andyoung.blog.csdn.net/article/details/127471677', 'https://andyoung.blog.csdn.net/article/details/127471196', 'https://andyoung.blog.csdn.net/article/details/127471018', 'https://andyoung.blog.csdn.net/article/details/127447394', 'https://andyoung.blog.csdn.net/article/details/127446724', 'https://andyoung.blog.csdn.net/article/details/127428024', 'https://andyoung.blog.csdn.net/article/details/127427087', 'https://andyoung.blog.csdn.net/article/details/127425240', 'https://andyoung.blog.csdn.net/article/details/127407244', 'https://andyoung.blog.csdn.net/article/details/127405963', 'https://andyoung.blog.csdn.net/article/details/127405493', 'https://andyoung.blog.csdn.net/article/details/127321632', 'https://andyoung.blog.csdn.net/article/details/127320187', 'https://andyoung.blog.csdn.net/article/details/127319851', 'https://andyoung.blog.csdn.net/article/details/127318669', 'https://andyoung.blog.csdn.net/article/details/127305461', 'https://andyoung.blog.csdn.net/article/details/127287323', 'https://andyoung.blog.csdn.net/article/details/127248190', 'https://andyoung.blog.csdn.net/article/details/127222441', 'https://andyoung.blog.csdn.net/article/details/127222054', 'https://andyoung.blog.csdn.net/article/details/127221016', 'https://andyoung.blog.csdn.net/article/details/127209195', 'https://andyoung.blog.csdn.net/article/details/127208824', 'https://andyoung.blog.csdn.net/article/details/127206550', 'https://andyoung.blog.csdn.net/article/details/127185594', 'https://andyoung.blog.csdn.net/article/details/127183870', 'https://andyoung.blog.csdn.net/article/details/127121606', 'https://andyoung.blog.csdn.net/article/details/127119359', 'https://andyoung.blog.csdn.net/article/details/127117898', 'https://andyoung.blog.csdn.net/article/details/127088106', 'https://andyoung.blog.csdn.net/article/details/127047231', 'https://andyoung.blog.csdn.net/article/details/126966802', 'https://andyoung.blog.csdn.net/article/details/126847067', 'https://andyoung.blog.csdn.net/article/details/126832031', 'https://andyoung.blog.csdn.net/article/details/126707042', 'https://andyoung.blog.csdn.net/article/details/126667108', 'https://andyoung.blog.csdn.net/article/details/126636322', 'https://andyoung.blog.csdn.net/article/details/126607270', 'https://andyoung.blog.csdn.net/article/details/126608939', 'https://andyoung.blog.csdn.net/article/details/126603774', 'https://andyoung.blog.csdn.net/article/details/126608051', 'https://andyoung.blog.csdn.net/article/details/126602560', 'https://andyoung.blog.csdn.net/article/details/126602933', 'https://andyoung.blog.csdn.net/article/details/126608353', 'https://andyoung.blog.csdn.net/article/details/126598411', 'https://andyoung.blog.csdn.net/article/details/126583258', 'https://andyoung.blog.csdn.net/article/details/126581731', 'https://andyoung.blog.csdn.net/article/details/126566544', 'https://andyoung.blog.csdn.net/article/details/126566603', 'https://andyoung.blog.csdn.net/article/details/126547604', 'https://andyoung.blog.csdn.net/article/details/126547545', 'https://andyoung.blog.csdn.net/article/details/126493742', 'https://andyoung.blog.csdn.net/article/details/126438529', 'https://andyoung.blog.csdn.net/article/details/126437275', 'https://andyoung.blog.csdn.net/article/details/126436987', 'https://andyoung.blog.csdn.net/article/details/126171981', 'https://andyoung.blog.csdn.net/article/details/126416231', 'https://andyoung.blog.csdn.net/article/details/124485795', 'https://andyoung.blog.csdn.net/article/details/123954205', 'https://andyoung.blog.csdn.net/article/details/126394595', 'https://andyoung.blog.csdn.net/article/details/126394228', 'https://andyoung.blog.csdn.net/article/details/123747981', 'https://andyoung.blog.csdn.net/article/details/126362723', 'https://andyoung.blog.csdn.net/article/details/126362019', 'https://andyoung.blog.csdn.net/article/details/126359881', 'https://andyoung.blog.csdn.net/article/details/126359567', 'https://andyoung.blog.csdn.net/article/details/126347207', 'https://andyoung.blog.csdn.net/article/details/126347069', 'https://andyoung.blog.csdn.net/article/details/126345512', 'https://andyoung.blog.csdn.net/article/details/126344101', 'https://andyoung.blog.csdn.net/article/details/126311740', 'https://andyoung.blog.csdn.net/article/details/126337993']

get_proxy_list()
print('Done--get_proxy_list!')


article_list.append("https://blog.csdn.net/agonie201218/article/details/129746085")
article_list.append("https://blog.csdn.net/agonie201218/article/details/129839233")
article_list.append("https://blog.csdn.net/agonie201218/article/details/129871312")
article_list.append("https://blog.csdn.net/agonie201218/article/details/129944178")

article_list.append("https://blog.csdn.net/agonie201218/article/details/129396503")
article_list.append("https://blog.csdn.net/agonie201218/article/details/129416204")
article_list.append("https://blog.csdn.net/agonie201218/article/details/129621152")
article_list.append("https://blog.csdn.net/agonie201218/article/details/129724757")

# f = open('output.out', 'w')
# print(proxy_list, file=f)
# f.close()
# get_article_list()
# print('Done--get_article_list!')
# f=open('output2.out','w')
# print(article_list,file=f)
# f.close()


def do():
    global total_count
    global count
    while count >= 0:
        solve()

        if len(proxy_list) < 10:
            get_proxy_list()
        if total_count < count:
            break


mission = list()  # 多线程跑的快
nums = 50
for i in range(nums):
    mission.append(Thread(target=do))
for i in range(nums):
    # mission[i].setDaemon(True)
    mission[i].start()
for i in range(nums):
    mission[i].join()

# https://zhuanlan.zhihu.com/p/68628325?from_voters_page=true
