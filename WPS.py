# -*- coding: utf8 -*-
#-*- codeing =utf-8 -*-
#@Time : 2021/2/8 10:42
#@File : wps签到领空间.py
#@Software : PyCharm
import requests
import json
import time
import random
from AutoConfig import config
config_ = config.get("Wps")

wps_sid=config_.get("wps_sid")


# 微信推送
def weChatPush(txt):
    Secret = "GuabRMpWYTIeIkk_Dc-sX5LJi59M_7JfCk9KJrtn8Bs"
    corpid = 'ww41560323f54f5b7b'
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'
    getr = requests.get(url=url.format(corpid, Secret))
    access_token = getr.json().get('access_token')
    data = {
            "touser": "@all",
            "msgtype": "text",
            "agentid": 1000003,
            "text": {
                "content": "WPS签到领空间\n" + txt
            },
            "safe": 0,
            }
    requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token),data=json.dumps(data))
pass

def wps():
    url="https://vip.wps.cn/sign/v2"
    headers={
        "Cookie":wps_sid,
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/46.0.2486.0 Safari/537.36 Edge/13.10586"
    }
    data={"platform":"8",
        "captcha_pos":"137.00431974731889, 36.00431593261568",
        "img_witdh":"275.164",
        "img_height":"69.184"
    }	
    data0={"platform":"8"}		
    yz_url="https://vip.wps.cn/checkcode/signin/captcha.png?platform=8&encode=0&img_witdh=275.164&img_height=69.184"

    req=requests.post(url=url,headers=headers,data=data0)
    if not ("msg" in req.text):		
        print("wps_sid无效")
        return "wps_sid无效"
    else:
        sus=json.loads(req.text)["result"]		
        print("免验证签到-->"+sus)		
        if sus == "error":
            for n in range(60):
                requests.get(url=yz_url,headers=headers)
                req=requests.post(url=url,headers=headers,data=data)
                sus=json.loads(req.text)["result"]
                #print(str(n+1)+"尝试验证签到-->"+sus)
                time.sleep(random.randint(0,5)/10)
                if sus=="ok":
                    sus="成功！"
                    break
            sus="失败，请手动签到！"
        print("最终签到结果-->"+sus)
        return "最终签到结果:"+sus

def main():
    s=wps()
    weChatPush(s)
    print(s)

if __name__ == '__main__':
    main()
