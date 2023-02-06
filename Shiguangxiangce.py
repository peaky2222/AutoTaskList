# encoding:utf-8
import requests
import json
import hashlib
import requests as req
from datetime import datetime

from AutoConfig import config
#import Demjson

# 时光相册签到领空间
# 登录信息 账户，密码
# fork in github : https://github.com/ICE99125/everphoto_checkin

# config 用户登录信息
config_ = config.get("Shiguang")

# 推送信息
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
                "content": "时光相册签到信息：\n\n" + txt
            },
            "safe": 0,
            }
    requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token),data=json.dumps(data))
    pass




def handler(fn):
    def inner(*args, **kwargs):
        res = fn(*args, **kwargs)

        if res["status"]: 
            return [
                {
                    "h4": {
                        "content": f"账号: {res['account']}",
                    }
                },
                {
                    "txt": {
                        "content": res["message"],
                    },
                    "table": {
                        "content": [
                            ("今日获得", f"{res['reward']}M"),
                            ("明日获得", f"{res['tomorrow']}M"),
                            ("总共获得", f"{res['total']}M"),
                            ("连续签到", f"{res['continuity']}天"),
                        ]
                    },
                },
            ]
        else:
            # 登录失败 or 签到失败
            return [
                {
                    "h4": {
                        "content": f"账号: {res['account']}",
                    },
                    "txt": {
                        "content": res["message"],
                    },
                }
            ]

    return inner



# 日期字符串格式化
def dateTime_format(dt: str) -> str:
    try:
        dl = datetime.strptime(dt, "%Y-%m-%dT%H:%M:%S+08:00")

        return dl.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError as e:
        print(f"格式化日期时出错, 原因: {e}")


class Everphoto:
    # 登录地址
    LOGIN_URL = "https://web.everphoto.cn/api/auth"
    # 签到地址
    CHECKIN_URL = "https://openapi.everphoto.cn/sf/3/v4/PostCheckIn"

    def __init__(self, account: str, password: str) -> None:
        self.__account = account
        self.__password = password
        self.headers = {
            "user-agent": "EverPhoto/4.5.0 (Android;4050002;MuMu;23;dev)",
            "application": "tc.everphoto",
        }
        self.userInfo = {}

    # 获取 md5 加密后的密码
    def get_pwd_md5(self) -> str:
        salt = "tc.everphoto."
        pwd = salt + self.__password
        md5 = hashlib.md5(pwd.encode())
        return md5.hexdigest()

    # 登陆
    def login(self, country_code: str = "+86"):
        try:
            data = {
                "mobile": f"{country_code}{self.__account}",
                "password": self.get_pwd_md5(),
            }
            res = req.post(
                Everphoto.LOGIN_URL,
                data=data,
                headers=self.headers,
            ).json()

            if res.get("code") == 0:
                print(f"🎉 登录账号 {self.__account} 成功")
                
                data = res.get("data")

                self.headers.update({"authorization": f"Bearer {data['token']}"})
                self.userInfo.update({
                    "account": self.__account, # 账号
                    "name": data["user_profile"]["name"], # 用户名
                    "vip": data["user_profile"].get("vip_level"), # vip等级
                    "created": dateTime_format(data["user_profile"]["created_at"]), # 创建时间
                    "day": data["user_profile"]["days_from_created"], # 注册时长
                })
                return {
                    "status": True
                }
            else:
                raise Exception(res.get("message"))
        except Exception as e:
            print(f"😭 登录账号 {self.__account} 时出现错误, 原因: {e}")

            return {
                "status": False,
                "message": e,
            }

    # 签到
    def checkin(self):
        try:
            headers = {
                "content-type": "application/json",
                "host": "openapi.everphoto.cn",
                "connection": "Keep-Alive",
            }

            headers.update(self.headers)
            
            res = req.post(
                Everphoto.CHECKIN_URL,
                headers=headers,
            ).json()

            code = res.get('code')

            if code == 0:
                print(f"🎉 账号 {self.__account} 签到成功")

                data = res.get('data')

                if data.get("checkin_result") is True:
                    rwd = data["reward"] / (1024 * 1024)  # 今日获得
                    msg = "签到成功"
                else:
                    rwd = 0
                    msg = "今日已签到"

                return {
                    "status": True,
                    "reward": rwd,
                    "message": msg,
                    "continuity": data.get("continuity"), # 连续签到天数
                    "total": data.get("total_reward") / (1024 * 1024), # 总计获得
                    "tomorrow": data.get("tomorrow_reward") / (1024 * 1024), # 明日可获得
                }
            elif code == 20104:
                # 未登录
                raise Exception(res.get('message'))
            elif code == 30001:
                # 服务器内部错误?
                raise Exception(res.get('message'))
        except Exception as e:
            print(f"账号 {self.__account} 签到时出现错误, 原因: {e}")

            return {
                "status": False,
                "message": f"签到失败, 原因: {e}",
            }

    @handler
    def start(self):
        r = self.login()
        if r["status"]:
            res = self.checkin()
            
            result = {}
            result.update(self.userInfo)
            result.update(res)

            return result
        else:
            return {
                "status": False,
                "message": f"登录失败, 原因: {r['message']}",
                "account": self.__account,
            }

def main(*arg):
    multi = config_
    txt = ''
    msg_list = []
    for i in multi:
        b = Everphoto(i["account"], i['password'])
        res = b.start()
        msg_list.extend(res)
        

    for i in msg_list:
        if 'h4' in i:
            txt =txt + i['h4']['content']+ '\n'
        if 'txt' in i:
            txt =txt + i['txt']['content']+ '\n'
        if 'table' in i:
            for j in i['table']['content']:
                txt =txt + j[0]+':'+ j[1]+'\n'
    weChatPush(txt)
    print(txt)
      
   

if __name__ == '__main__':
  main()