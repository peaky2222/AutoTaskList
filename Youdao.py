# 有道云笔记自动登陆签到看广告
# by 妖火 id34976
import requests
import json
# server酱开关，填0不开启(默认)，填1只开启cookie失效通知，填2同时开启cookie失效通知和签到成功通知
server = '0'

import time
import random
from AutoConfig import config,weChatPush
config_ = config.get("Youdao")





def start(cookie):
  c = ''
  ad = 0
  payload = 'yaohuo:id34976'
  headers = {'Cookie': cookie}
  r = requests.get('http://note.youdao.com/login/acc/pe/getsess?product=YNOTE', headers=headers)
  for key, value in r.cookies.items():
    c += key + '=' + value + ';'
  headers = {'Cookie': c}
  re = requests.request("POST", "https://note.youdao.com/yws/api/daupromotion?method=sync", headers=headers, data = payload)
  if 'error' not in re.text:
    res = requests.request("POST", "https://note.youdao.com/yws/mapi/user?method=checkin", headers=headers, data = payload)
    for _ in range(3):
      resp = requests.request("POST", "https://note.youdao.com/yws/mapi/user?method=adRandomPrompt", headers=headers, data = payload)
      ad += resp.json()['space'] // 1048576
    #print(re.text,res.text, resp.text)
    if 'reward' in re.text:
      sync = re.json()['rewardSpace'] // 1048576
      checkin = res.json()['space'] // 1048576
      space = str(sync + checkin + ad)
      #print('恭喜获得空间：' + space + 'M')
      desp='签到获得空间：' + space + 'M'
    return desp
    #if server == '2':
        #requests.get('https://sc.ftqq.com/' + sckey + '.send?text=有道云笔记签到成功共获得空间' + space + 'M')
        #requests.get('https://sctapi.ftqq.com/' + sckey2 + '.send?title=有道云笔记签到成功共获得空间' + space + 'M&desp=来源:有道云笔记签到-17806275268')
  else:
    errorInfo='=有道云笔记签到cookie失效请更新'
    return errorInfo
    #if server != '0':
      #requests.get('https://sctapi.ftqq.com/' + sckey2 + '.send?title=有道云笔记签到成功共获得空间' + space + 'M&desp=来源:有道云笔记签到-17806275268')
      #requests.get('https://sc.ftqq.com/' + sckey + '.send?text=有道云笔记签到cookie失效请更新-17806275268')


if __name__ == '__main__':
    multi = config_
    msg = ''
    time.sleep(random.randint(300, 500))
    for i in multi:
        re = start(i["cookie"])
        msg = msg + i["acc"] +'\n'+ re +'\n\n'
    weChatPush(msg)
