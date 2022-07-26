import requests  # 提示，此库并非Python3自带，安装方法请见下文
import re
from tkinter import *
import time
import _thread

payload = ""
# 请求头
headers = {
    "Accept": "*/*",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
    "Cookie": "l=AurqcPuigwQdnQv7WvAfCoR1OlrRQW7h; isg=BHp6mNB79CHqYXpVEiRteXyyyKNcg8YEwjgLqoRvCI3ddxqxbLtOFUBGwwOrZ3ad; thw=cn; cna=VsJQERAypn0CATrXFEIahcz8; t=0eed37629fe7ef5ec0b8ecb6cd3a3577; tracknick=tb830309_22; _cc_=UtASsssmfA%3D%3D; tg=0; ubn=p; ucn=unzbyun; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; miid=981798063989731689; hng=CN%7Czh-CN%7CCNY%7C156; um=0712F33290AB8A6D01951C8161A2DF2CDC7C5278664EE3E02F8F6195B27229B88A7470FD7B89F7FACD43AD3E795C914CC2A8BEB1FA88729A3A74257D8EE4FBBC; enc=1UeyOeN0l7Fkx0yPu7l6BuiPkT%2BdSxE0EqUM26jcSMdi1LtYaZbjQCMj5dKU3P0qfGwJn8QqYXc6oJugH%2FhFRA%3D%3D; ali_ab=58.215.20.66.1516409089271.6; mt=ci%3D-1_1; cookie2=104f8fc9c13eb24c296768a50cabdd6e; _tb_token_=ee7e1e1e7dbe7; v=0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64;` rv:47.0) Gecko/20100101 Firefox/47.0"
}


def getList(url):  # 获取用户首页的文章列表
    resp = requests.request("GET", url, data=payload, headers=headers)  # 发送请求
    resp.encoding = resp.apparent_encoding  # 设置解码方式
    html_source = resp.text
    # 通过正则表达式，从获取的HTML代码中提取出链接
    urls = re.findall("https://[^>\";\']*\d", html_source)
    new_urls = []
    for url in urls:
        if 'details' in url:
            if url not in new_urls:
                new_urls.append(url)
    return new_urls


def submit():  # 当点击确定时
    _thread.start_new_thread(window_loop, ())
    # 由于在执行时会出现窗体停止刷新的情况，需要另一个线程辅助窗体刷新
    urls = getList(Entry1.get())

    while True:
        console.insert(1.0, '\n============================')
        for url in urls:
            win.update()
            requests.request("GET", url, data=payload, headers=headers)  # 发送请求
            win.update()
            # 在窗体的文本框内插入请求链接及状态
            console.insert(1.0, "\n{Process} " + str(url) + ' [Finish]\n')
            win.update()
            time.sleep(1)
        time.sleep(60)


def window_loop():  # 辅助窗体刷新的线程
    while True:
        win.update()  # 刷新窗体
        time.sleep(0.1)


win = Tk()
win.title('CSDN刷访问量工具')
win.geometry('300x344+100+100')

Label1 = Label(win, text='请输入个人博客主页链接:', font=('黑体', 12),
               anchor=W).place(y=13, x=15, width=234, height=20)

Entry1 = Entry(win, font=('等线', 11), width=70)
Entry1.place(y=40, x=15, width=196, height=26)

Button1 = Button(win, text='Go!', font=('等线', 11), command=submit).place(
    y=38, x=218, width=65, height=28)

console = Text(win, font=('等线', 11))
console.place(y=82, x=15, width=268, height=241)
console.insert(1.0, '欢迎使用‘增加CSDN访问量’实用工具')

win.mainloop()
