# -*- coding: utf8 -*-

# coding=utf-8
import requests,  json, configparser,  os
import time, random
from AutoConfig import config
config_ = config.get("Upcup")


# 模拟包头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


# 获取当前的时间
def get_time():
    return time.strftime('%Y%m%d', time.localtime(time.time()))
def getUserInfo(multi):
    try:
        usernames = []
        passwords = []
        
        for i in multi:
            usernames.append(i["account"])
            passwords.append(i['password'])
        
        #print('get userdata success')
        return list(zip(usernames, passwords))

    except Exception as e:
        print('get userdata failed\n %s' % e)
        return None


# 登录并获取old_info
def login(userdata):
    login_url = "https://app.upc.edu.cn/uc/wap/login/check"
    session = requests.session()
    response = session.post(login_url, headers=headers, data=userdata, timeout=20)
    response.encoding = "UTF-8"
    # print(response.text,'\n')
    info_url = "https://app.upc.edu.cn/ncov/wap/default/index"
    html_info = session.get(info_url, headers=headers, timeout=20)
    html_info.encoding = "UTF-8"
    return session, html_info.text


# 企业号推送
def weChatPush(txt):
    Secret = "GuabRMpWYTIeIkkXXXXXXXXXX7JfCk9KJrtn8Bs"
    corpid = 'wwXXXXXXXXXXXX60323f54f5b7b'
    url = 'https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={}&corpsecret={}'
    getr = requests.get(url=url.format(corpid, Secret))
    access_token = getr.json().get('access_token')
    data = {
        "touser": "@all",
        "msgtype": "text",
        "agentid": 1000003,
        "text": {
            "content": "疫情防控通\n" + txt
        },
        "safe": 0,
    }
    requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token),
                  data=json.dumps(data))

    pass


def save_info(session, info):
    save_url = "https://app.upc.edu.cn/ncov/wap/default/save"
    save_response = session.post(url=save_url, data=info, headers=headers, timeout=20)
    save_response.encoding = "UTF-8"
    return save_response.text




def process(userdata):
    # 登录返回old_info
    session, html = login(userdata)
    # print(html)
    old_info = json.loads(html)['d']['oldInfo']

    # 获取当前日期
    today_date = get_time()

    # 重构old_info
    old_info['date'] = today_date
    # print(old_info)

    # 提交信息，对应的接口为save
    save_res = save_info(session, old_info)
    session.close()





if __name__ == "__main__":
    # 获取用户信息
    multi = config_
    userinfos = getUserInfo(multi)
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(random.randint(300, 500))
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    for user in userinfos:
        user_data = {
            'username': user[0],
            'password': user[1]
        }

        process(user_data)

    
