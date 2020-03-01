import tkinter as tk
import http.client
import hashlib
import urllib
import random
import json
window = tk.Tk()
window.title("EasyTrans")
window.geometry("400x150")
window.iconbitmap(".\\f.ico")

var = tk.StringVar()

ent = tk.Entry(window,width=35)
ent.place(x=100,y=12)

lable = tk.Label(window,text="翻译结果")
lable.place(x=25,y=60)

ent2 = tk.Entry(window,width=35,textvariable=var)
ent2.place(x=100,y=60)

def trans():
    txt = ent.get()
    if txt == '':
        pass
    else: 
        appid = ''
        secretKey = ''

        httpClient = None
        myurl = '/api/trans/vip/translate'

        fromLang = 'auto'
        toLang = 'auto'
        salt = random.randint(32768, 65536)
        q = txt
        sign = appid + q + str(salt) + secretKey
        sign = hashlib.md5(sign.encode()).hexdigest()
        myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(
        salt) + '&sign=' + sign

        try:
            httpClient = http.client.HTTPConnection('api.fanyi.baidu.com')
            httpClient.request('GET', myurl)

            response = httpClient.getresponse()
            result_all = response.read().decode("utf-8")
            result = json.loads(result_all)

            var.set(result['trans_result'][0]['dst'])

        except Exception as e:
            print(e)
        finally:
            if httpClient:
                httpClient.close()
btn_trans = tk.Button(window,text="百度翻译",width=10, command=trans)
btn_trans.place(x=10,y=10)

window.mainloop()