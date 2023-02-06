# -*- coding: utf8 -*-

# coding=utf-8
import requests, time, json, configparser, random, os

# 模拟包头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
    'X-Requested-With': 'XMLHttpRequest'
}


# 获取当前的时间
def get_time():
    return time.strftime('%Y%m%d', time.localtime(time.time()))


# 帐号密码信息读取
def getUserInfo():
    try:
        usernames = ('Z20070031', )
        passwords = ('Qyf9999.', )
        emails = ('1490316377@qq.com', )

        #print('get userdata success')
        return list(zip(usernames, passwords, emails))

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

def fwalertPush(title,to,main):
    # https://fwalert.com/
    data = {
            "title": title,
            "from": to,
            "main": main,
            }
    c = requests.get(url="https://fwalert.com/775a3543-58aa-4e1d-98ad-f2c745e45c25",params=data)
    print(c.json)
pass

# 企业号推送
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




def process(userdata, email_address):
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
    print(userdata.get("username"))
    print(str(json.loads(save_res)['m']))
    session.close()

    if email_address:
        # 结束后发送邮件
        if json.loads(save_res)['m'] == '操作成功':
            #send_email("信息填报成功！", "账号：" + userdata.get("username") + "\n结果：" + str(json.loads(save_res)['m']),
            #           email_address)
            #if (userdata.get("username") == 'Z20070031'):
            weChatPush("信息填报成功！\n账号：" + userdata.get("username"))
            fwalertPush("疫情防控信息填报成功！","疫情防控通","疫情防控信息填报成功")
        else:
            #send_email("信息填报失败！可能是已经提交过了！",
            #           "账号：" + userdata.get("username") + "\n" + str(json.loads(save_res)['m']) + "\n请看今天第一个邮件或手动签到！",
            #           email_address)
            #if (userdata.get("username") == 'Z20070031'):
            weChatPush("信息填报失败！\n账号：" + userdata.get("username") + "\n请看今天第一条信息或手动签到！")
            fwalertPush("疫情防控信息填报失败！","疫情防控通","请看今天第一条信息或手动签到")




if __name__ == "__main__":
    # 获取用户信息
    userinfos = getUserInfo()
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    time.sleep(random.randint(300, 500))
    print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
    for user in userinfos:
        user_data = {
            'username': user[0],
            'password': user[1]
        }

        process(user_data, user[2])

