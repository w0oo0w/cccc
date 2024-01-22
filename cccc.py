import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen
import re
import json
import random
import time
from time import sleep
from threading import Thread

success_count = 0
fail_count = 0
# total_count = 5000
total_count = 2000
random.seed(time.time())
proxy_list = []
article_list = []
cookie = list()
cookie.append({'cookie': 'HWWAFSESID=5955c8958d2eff99ebe; HWWAFSESTIME=1674003827591; uuid_tt_dd=10_19970426330-1674003834162-663687; dc_session_id=10_1674003834162.588556; c_pref=default; c_ref=default; c_first_ref=default; c_first_page=https://blog.csdn.net/agonie201218/category_11159108.html; c_dsid=11_1674003831841.752193; c_segment=7; c_page_id=default; log_Id_pv=1; dc_sid=d904cdc4d1e27b164d466b49ce26ae53; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1672103747,1672709220,1674003591; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1674003832; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac={"islogin":{"value":"0","scope":1},"isonline":{"value":"0","scope":1},"isvip":{"value":"0","scope":1}}; hide_login=1; firstDie=1; __gads=ID=7e9152aa51e379b0-225c7ef453d9005c:T=1674003833:RT=1674003833:S=ALNI_Mbw9ge8irY6APS86aicbuXLLsfevQ; __gpi=UID=00000ba65ce69ca7:T=1674003833:RT=1674003833:S=ALNI_MaQYXknz08npTV-1FoQSy43m-pCng; dc_tos=ronpmg; log_Id_view=1; FCNEC=[["AKsRol9hhb7AAKkpFUVh9orEA_puCUUJEyvsVNfDIWR2zrRVC6TkTKOqOYg2OFRY6l1PnyTv6t8eBRiAY_JhR5etoZwuYFt8V58onlj1V8dKBrwGbf7gzCNLE4EdsxgzrBav_uqJypPjun-DL-X255DPa3HAKV7qfw=="],null,[]]'})
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
    "Cookie": "uuid_tt_dd=10_19970426330-1679877991857-938020; dc_session_id=10_1679877991857.163373; c_pref=default; c_ref=default; c_first_ref=default; c_segment=4; dc_sid=1fc33ea9444e1d5d7efd6b9b0ae9e314; hide_login=1; Hm_lvt_6bcd52f51e9b3dce32bec4a3997715ac=1679877994; Hm_up_6bcd52f51e9b3dce32bec4a3997715ac=%7B%22islogin%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isonline%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%2C%22isvip%22%3A%7B%22value%22%3A%220%22%2C%22scope%22%3A1%7D%7D; firstDie=1; __bid_n=1867cf2bb20e0f083d4207; __gads=ID=e9539b07fa971427-2285edcfc3dc005f:T=1679877994:RT=1679877994:S=ALNI_MZxXZjgQpg3sQ0FeNAbxQoLTe9Dwg; __gpi=UID=00000be1eae1bccf:T=1679877994:RT=1679877994:S=ALNI_MaeL4H3MRg6YsUPJJy-Qo9ClLeUyA; https_waf_cookie=6ed283ea-7cf9-4b953e26802f66a62f6e95a2f89c8b61880b; c_first_page=https%3A//andyoung.blog.csdn.net/article/details/129746085%3Fspm%3D1001.2014.3001.5502; c_dsid=11_1679878004094.263767; c_page_id=default; log_Id_pv=2; Hm_lpvt_6bcd52f51e9b3dce32bec4a3997715ac=1679878005; dc_tos=rs5m5x; FPTOKEN=HyfICajDzRVg2L47+ke3Og8ByZ4A9B115OQYYHHxg3luutSnMpwy+29fmG/3v0WK829xbrS+82Iol6iGO8fGy3vrlduFcvyRoDFENlGH1c0/HBFlqwGN4+ji4TGIzHm7LIdbr+Zx1AKmRN9osyQLtLlgxqA/K2D4yTjyMIr4KVAX9UnIAaPv+IEdXr7wnclMLw7XZ48VG/DkMQk/3/Jy0oP4BroB3ntiMqurHnohZDpiFNfunxjeUl6p4ej2OMou1v2G24Z1xt3FkbdrcH+cwqHS9P5j/mdId+nnYVoyGxdK5/SkjzaI0uYY/epfXx7ZO4UiMrkF19LZdvG/sZ6GrHf4YzQ0/Qhd88kZTqh3e1o7kJwYDNui6y5kckLxlP4PSbxQNYUyeJfs3bfWOVFPXg==|oxIFHPjngqBvC3dXxkIB0PAGJku1v+EyXmE8djxrLwA=|10|6f637bd94909a0e29e2735895e8d1e08; log_Id_view=3; FCNEC=%5B%5B%22AKsRol_2O8QjXiPtqbgPz9LPysPui_EAM_mFowY0DKhpuu4ttau8Xq7qmfhw0L2QkJvho6_kHqQ2hAeaIJx2LpJol5H7f8uCH-Z1MiBhBrJjh8Y7AzAk5zcjqO1ideQNDjxyNG9kUWNTz6jcMUBCdW8ZIpfemRkoZQ%3D%3D%22%5D%2Cnull%2C%5B%5D%5D",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64;` rv:47.0) Gecko/20100101 Firefox/47.0"
}


def mapUrl(x):
    print("xxx")
    print(x)
    print(x['url'])
    return x['url']


def getList(url):  # 获取用户首页的文章列表
    proxy = {'http': proxy_list[random.randint(0, len(proxy_list)-1)]}
    resp = requests.request("GET", url, data=payload, headers=headers, proxies=proxy, cookies=cookie[random.randint(0, len(cookie)-1)])  # 发送请求
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
    for row in urlopen('https://sunny9577.github.io/proxy-scraper/proxies.txt').readlines():
        proxy_list.append(row)
        #item = json.loads(row)
        # if item['type'] == 'http' and item['anonymity'] == 'high_anonymous' and item['response_time'] < 20:
        #    proxy_list.append(item['host']+':'+str(item['port']))


def solve():

    global fail_count
    global success_count
    sleep(random.randint(0, 300))
    article = article_list[random.randint(0, len(article_list)-1)]
    proxy = {'http': proxy_list[random.randint(0, len(proxy_list)-1)]}
    header = {'User-Agent': User_Agent[random.randint(0, len(User_Agent)-1)],
              'referer': 'http://blog.csdn.net'}
    try:
        requests.get(article.replace('https', 'https'), headers=header, proxies=proxy,
                     cookies=cookie[random.randint(0, len(cookie)-1)], timeout=7)
        success_count = success_count + 1;
        print('ok ip:'+proxy['http'] + ' success_count:' + str(success_count) )

    except:
        fail_count = fail_count + 1
        print('no' + ' fail_count:' + str(fail_count))
        try:
            proxy_list.remove(proxy['http'])
        except:
            pass

article_list = []
article_list.append("https://blog.csdn.net/agonie201218/article/details/134954240")
article_list.append("https://blog.csdn.net/agonie201218/article/details/134803155")
article_list.append("https://blog.csdn.net/agonie201218/article/details/134954240")
article_list.append("https://blog.csdn.net/agonie201218/article/details/134803155")
article_list.append("https://blog.csdn.net/agonie201218/article/details/135013169")
article_list.append("https://blog.csdn.net/agonie201218/article/details/134738712")
article_list.append("https://blog.csdn.net/agonie201218/article/details/134205554")
article_list.append("https://blog.csdn.net/agonie201218/article/details/135019127")
article_list.append("https://blog.csdn.net/agonie201218/article/details/135128632")
article_list.append("https://blog.csdn.net/agonie201218/article/details/135111308")

get_proxy_list()
print('Done--get_proxy_list!')
solve()


#article_list = ['https://andyoung.blog.csdn.net/article/details/127647523', 'https://andyoung.blog.csdn.net/article/details/127643437', 'https://andyoung.blog.csdn.net/article/details/127632052', 'https://andyoung.blog.csdn.net/article/details/127631073', 'https://andyoung.blog.csdn.net/article/details/127646405', 'https://andyoung.blog.csdn.net/article/details/127615445', 'https://andyoung.blog.csdn.net/article/details/127545170', 'https://andyoung.blog.csdn.net/article/details/127531162', 'https://andyoung.blog.csdn.net/article/details/127617954', 'https://andyoung.blog.csdn.net/article/details/127610437', 'https://andyoung.blog.csdn.net/article/details/127604667', 'https://andyoung.blog.csdn.net/article/details/127604763', 'https://andyoung.blog.csdn.net/article/details/127604291', 'https://andyoung.blog.csdn.net/article/details/127530680', 'https://andyoung.blog.csdn.net/article/details/127529692', 'https://andyoung.blog.csdn.net/article/details/127569390', 'https://andyoung.blog.csdn.net/article/details/127529179', 'https://andyoung.blog.csdn.net/article/details/127545010', 'https://andyoung.blog.csdn.net/article/details/127530807', 'https://andyoung.blog.csdn.net/article/details/127528084', 'https://andyoung.blog.csdn.net/article/details/127527105', 'https://andyoung.blog.csdn.net/article/details/127526744', 'https://andyoung.blog.csdn.net/article/details/127491699', 'https://andyoung.blog.csdn.net/article/details/127490677', 'https://andyoung.blog.csdn.net/article/details/127488380', 'https://andyoung.blog.csdn.net/article/details/127487696', 'https://andyoung.blog.csdn.net/article/details/127487074', 'https://andyoung.blog.csdn.net/article/details/127472301', 'https://andyoung.blog.csdn.net/article/details/127471677', 'https://andyoung.blog.csdn.net/article/details/127471196', 'https://andyoung.blog.csdn.net/article/details/127471018', 'https://andyoung.blog.csdn.net/article/details/127447394', 'https://andyoung.blog.csdn.net/article/details/127446724', 'https://andyoung.blog.csdn.net/article/details/127428024', 'https://andyoung.blog.csdn.net/article/details/127427087', 'https://andyoung.blog.csdn.net/article/details/127425240', 'https://andyoung.blog.csdn.net/article/details/127407244', 'https://andyoung.blog.csdn.net/article/details/127405963', 'https://andyoung.blog.csdn.net/article/details/127405493', 'https://andyoung.blog.csdn.net/article/details/127321632', 'https://andyoung.blog.csdn.net/article/details/127320187', 'https://andyoung.blog.csdn.net/article/details/127319851', 'https://andyoung.blog.csdn.net/article/details/127318669', 'https://andyoung.blog.csdn.net/article/details/127305461', 'https://andyoung.blog.csdn.net/article/details/127287323', 'https://andyoung.blog.csdn.net/article/details/127248190', 'https://andyoung.blog.csdn.net/article/details/127222441', 'https://andyoung.blog.csdn.net/article/details/127222054', 'https://andyoung.blog.csdn.net/article/details/127221016', 'https://andyoung.blog.csdn.net/article/details/127209195', 'https://andyoung.blog.csdn.net/article/details/127208824', 'https://andyoung.blog.csdn.net/article/details/127206550', 'https://andyoung.blog.csdn.net/article/details/127185594', 'https://andyoung.blog.csdn.net/article/details/127183870', 'https://andyoung.blog.csdn.net/article/details/127121606', 'https://andyoung.blog.csdn.net/article/details/127119359', 'https://andyoung.blog.csdn.net/article/details/127117898', 'https://andyoung.blog.csdn.net/article/details/127088106', 'https://andyoung.blog.csdn.net/article/details/127047231', 'https://andyoung.blog.csdn.net/article/details/126966802', 'https://andyoung.blog.csdn.net/article/details/126847067', 'https://andyoung.blog.csdn.net/article/details/126832031', 'https://andyoung.blog.csdn.net/article/details/126707042', 'https://andyoung.blog.csdn.net/article/details/126667108', 'https://andyoung.blog.csdn.net/article/details/126636322', 'https://andyoung.blog.csdn.net/article/details/126607270', 'https://andyoung.blog.csdn.net/article/details/126608939', 'https://andyoung.blog.csdn.net/article/details/126603774', 'https://andyoung.blog.csdn.net/article/details/126608051', 'https://andyoung.blog.csdn.net/article/details/126602560', 'https://andyoung.blog.csdn.net/article/details/126602933', 'https://andyoung.blog.csdn.net/article/details/126608353', 'https://andyoung.blog.csdn.net/article/details/126598411', 'https://andyoung.blog.csdn.net/article/details/126583258', 'https://andyoung.blog.csdn.net/article/details/126581731', 'https://andyoung.blog.csdn.net/article/details/126566544', 'https://andyoung.blog.csdn.net/article/details/126566603', 'https://andyoung.blog.csdn.net/article/details/126547604', 'https://andyoung.blog.csdn.net/article/details/126547545', 'https://andyoung.blog.csdn.net/article/details/126493742', 'https://andyoung.blog.csdn.net/article/details/126438529', 'https://andyoung.blog.csdn.net/article/details/126437275', 'https://andyoung.blog.csdn.net/article/details/126436987', 'https://andyoung.blog.csdn.net/article/details/126171981', 'https://andyoung.blog.csdn.net/article/details/126416231', 'https://andyoung.blog.csdn.net/article/details/124485795', 'https://andyoung.blog.csdn.net/article/details/123954205', 'https://andyoung.blog.csdn.net/article/details/126394595', 'https://andyoung.blog.csdn.net/article/details/126394228', 'https://andyoung.blog.csdn.net/article/details/123747981', 'https://andyoung.blog.csdn.net/article/details/126362723', 'https://andyoung.blog.csdn.net/article/details/126362019', 'https://andyoung.blog.csdn.net/article/details/126359881', 'https://andyoung.blog.csdn.net/article/details/126359567', 'https://andyoung.blog.csdn.net/article/details/126347207', 'https://andyoung.blog.csdn.net/article/details/126347069', 'https://andyoung.blog.csdn.net/article/details/126345512', 'https://andyoung.blog.csdn.net/article/details/126344101', 'https://andyoung.blog.csdn.net/article/details/126311740', 'https://andyoung.blog.csdn.net/article/details/126337993']
article_list1 = getList("https://blog.csdn.net/community/home-api/v1/get-business-list?page=4&size=20&businessType=blog&orderby=&noMore=false&year=&month=&username=agonie201218")
sleep(random.randint(0, 10))
article_list2 = getList("https://blog.csdn.net/community/home-api/v1/get-business-list?page=5&size=20&businessType=blog&orderby=&noMore=false&year=&month=&username=agonie201218")
sleep(random.randint(0, 20))
article_list3 = getList("https://blog.csdn.net/community/home-api/v1/get-business-list?page=6&size=20&businessType=blog&orderby=&noMore=false&year=&month=&username=agonie201218")
sleep(random.randint(0, 30))
article_list4 = getList("https://blog.csdn.net/community/home-api/v1/get-business-list?page=7&size=20&businessType=blog&orderby=&noMore=false&year=&month=&username=agonie201218")
sleep(random.randint(0, 20))
article_list5 = getList("https://blog.csdn.net/community/home-api/v1/get-business-list?page=3&size=20&businessType=blog&orderby=&noMore=false&year=&month=&username=agonie201218")


for a in article_list1:
    article_list.append(a)
for a in article_list2:
    article_list.append(a)
for a in article_list3:
    article_list.append(a)
for a in article_list4:
    article_list.append(a)
for a in article_list5:
    article_list.append(a)
print('Done--get_article_list! '+ str(len(article_list)))



 


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
    global success_count
    global fail_count
    while True:
        solve()

        if len(proxy_list) < 10:
            get_proxy_list()
        if total_count < (success_count + fail_count):
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
