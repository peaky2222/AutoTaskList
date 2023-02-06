# 有道云笔记自动登陆签到看广告
# by 妖火 id34976
import requests
import json
# server酱开关，填0不开启(默认)，填1只开启cookie失效通知，填2同时开启cookie失效通知和签到成功通知
server = '0'
# 填写server酱sckey,不开启server酱则不用填
#sckey = 'SCU155663T250c7c2cfb1ed174cfd9dfbb93f9edc4601166eb99dec'

#sckey2 = 'SCT10915TrbGLdfzI6Cwuy6HqOTS4JaW1'
# 填入有道云笔记账号对应cookie

config = {
    "multi": [
        {
            "cookie": "Hm_lvt_53c97531c41019c3315b44853946c2c9=1638368228,1638459176,1638459190,1638780273; Hm_lpvt_53c97531c41019c3315b44853946c2c9=1638780292; __yadk_uid=FDCVtBEw3oYZT2SZqscJJMs5D9S1LluP; _ga=GA1.2.512020070.1636185596; OUTFOX_SEARCH_USER_ID_NCOO=71044445.59344848; OUTFOX_SEARCH_USER_ID=\"-2121722484@10.108.160.131\"; P_INFO=17806275268|1638368253|1|youdaonote|00&99|null&null&null#shd&null#10#0|&0||17806275268; YNOTE_USER=1; _9755xjdesxxd_=32; gdxidpyhxdE=Ro45N0tdDYNqhEDjxsedxXB%5CQdeygUQjPxRBW9y6sLXqRVHM6GLau3j6iw4h%5CAnjo0AXxel6J3bpHh8MGwjGh74DfGkPdJS66BArB8PBalWNSE4N9NGMOU0lMdbKnPk%5CU7D%2Fx9it0dekiXpC%2FbhrLM%2F7%2FzISb3qIxJ41LufN%2F06lLAWY%3A1638369178472; YD00688109880970%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb9e66189919e86d07d83a88aa3d15b828a8fafb540aeb0fbbbb73df5f0aeaacd2af0fea7c3b92ab2ed81b8f95bfcb9fdd2ea6db29e98b4e27c8cf1a08ce55c93a983b8b570fc9196bbf45ab0bda985bc798cbdaba4f1349beabdb2cc6593a8fbd9c85ea6af848cf153878bb983b2688cb3a196f560e99ca3aeb563edb9aaa7d25383b2a9a7b264a392f9d7b38089e8feabca6091929899d480b3b2b88ff05ca1afb985d74df7a782d3cc37e2a3; YD00688109880970%3AWM_NI=r3OWzQ8g31kgrBXScpH%2FPkfPQwMW6d8OZZqRlcgd9sHceCr8Y6sQIoQx58EVfqLkrYEUwb3lHmouvT%2BDmM6i%2FgfFSYAngF3haN760tK82JKTSNXxQtqnxnmPcqwdTG5yN2I%3D; YD00688109880970%3AWM_TID=DPYe1GK9vfVAAEBBFVIq8388M876kLNN; hb_MA-9057-2B94435F5EF6_source=sitoi.gitee.io; Hm_lvt_30b679eb2c90c60ff8679ce4ca562fcc=1638368225,1638370163; Hm_lvt_daa6306fe91b10d0ed6b39c4b0a407cd=1638369594,1638369597,1638457670,1638459139; JSESSIONID=aaakLLY4yAyO4h9_Dob2x; hb_MA-B0D8-94CBE089C042_source=www.baidu.com; _gid=GA1.2.1954358563.1638780273; _gat=1; YNOTE_CSTK=3jWsOQSX; PUBLIC_SHARE_351e08a72378206f9dd64d2281e9b83b=; YNOTE_SESS=v2|wD5ehg6JcWP4OLzlhHPZ0eykMz5kLU50QBkLgBOMUfRPz0LPynfUA0qzO4QS0LeyRwFkf6yP4kM0lWn4QBPLTz0qKOLYEkLzE0; YNOTE_PERS=v2|urstoken||YNOTE||web||-1||1638780289543||218.201.114.130||1490316377@qq.com||64PLqL6Mzf0YWhHOE0LlMRJBk4pZO4YGROE0Lw4nfYMReL6MTFP4JLROmOLklhfq40eFn4Y5kfOERQL6LT4OLeLR; YNOTE_LOGIN=3||1638780289550",
            "acc": "17806275268",
        },
        {
            "cookie": "__yadk_uid=9tMGb8JnnxxDEq2Eg3Y5MblYyJ1sdEzx; OUTFOX_SEARCH_USER_ID_NCOO=1875144752.3719869; OUTFOX_SEARCH_USER_ID=\"-1155064617@10.108.160.133\"; JSESSIONID=aaaXsTIJCUMzFbjhrob2x; YNOTE_CSTK=vsMsDI-c; YNOTE_USER=1; _9755xjdesxxd_=32; YD00688109880970:WM_NI=Em3O1cDu/lEWVBQomfKaOazrFycIQAuROuiifCF/ml9eCbWTQVwYl9fy1GjcgMtH8IRAxlsMJv5MarAG6FiAkMEoR2nT6eXmTiVaVXyKsZ9IsshH1C9D56+h3wgt+mMYeTE=; YD00688109880970:WM_NIKE=9ca17ae2e6ffcda170e2e6eeacfb42f4a9f78ac868a58a8ba6c45b978e9ebbaa34f799fcd9f35bf58d8bb2ce2af0fea7c3b92a87b3fdb0b46988abe18dc85d969e9f90f06e89bf8182f97a86a7adaad44bb78e8196ec63a69d8ad0f068fbbb8d83d660938ab9baef33a6a7ffa8e969a593bca9bb43929fb88df2478aaafbaee47a8399faa7ec4ba9938b90d13aae8cfa86db6798b79a82d554bb95bdbbbc43b1ada8a9b449fb9cfbd7aa64f1a9a995aa678f87abb5c837e2a3; YD00688109880970:WM_TID=V3xs6ZQDbSlERQUAQUd698Ts5pQ+TQAf; YNOTE_SESS=v2|Mx9AI9aJcWJLRfJLkfg4RJFRHpLRMTuRJZhMUWhMpyRPBhLYfRMpuR64hHT40MYf0gSh4TzOfgB0z50MeFRLwF0qS64kEkMkl0; YNOTE_PERS=v2|urstoken||YNOTE||web||-1||1638779806538||218.201.114.130||peakyu2020@163.com||T4kLOfh46Z0UY64J4h4YE0Q46Mwy6Lk5ROGnfJLh4Jz0UfnMUf6LQ4ROWhflY6M6Z0JuP4guPLkfRTKhLTFOLPF0; NTES_YD_SESS=or0xcq3HGuTjr9rw4GEOrtVi0wDqRq3EUQnVsN5ksx2IceKDcQzbiWuhor6NZf8t6UVQWxiWzluNutChvCFyq4fiMVTUj4ruTd6cnkJgddCjbv1k4UjgNIwUq2UaimRvklhNlF7i9IyqaIkeKT5KFhwHGuh8RfJI4.3Y0BmBxwgkji8_jOK7ks4gMbhyD73ixoqA8OgljUtuisHXa6INNc1jIASPsw8p1sy.4P5pDIxqL; S_INFO=1638779830|0|0&60##|17156087896; P_INFO=17156087896|1638779830|1|youdaonote|00&99|null&null&null#shd&370200#10#0|&0||17156087896; YNOTE_LOGIN=5||1638779867884; gdxidpyhxdE=0Z7VZ8f6nd\\yjgTVN6VhWOOhMGEshnwE/8uSfmcgIGUc9T4q+jqpGuuCPQQg\\divDWisYGW8SBDiD\\bexlYJ1BTgAjl\\Hbf/ZVgewjtxxROzYtd4peysJ1BgPbSdVQMSObs8aOpiX/xK5U/9+XK4ZPTWiC9KR8S+jcvUXRAUp4pqQdPd:1638780830842; PUBLIC_SHARE_351e08a72378206f9dd64d2281e9b83b=",
            "acc": "17156087896",
        },
        {
            "cookie": "OUTFOX_SEARCH_USER_ID_NCOO=772033724.3204468;OUTFOX_SEARCH_USER_ID=\\\"-2021979893@10.105.137.204\\\";_9755xjdesxxd_=32;YD00688109880970%3AWM_TID=HY0bH%2B5zoUNABQEBFUKRUb4i7B1vAhM7;Hm_lvt_30b679eb2c90c60ff8679ce4ca562fcc=1653392740;__yadk_uid=oi0cO20UsZxCM0KY9XHu2A67zyBx5R8m;_ga=GA1.2.755125072.1653392741;hb_MA-B0D8-94CBE089C042_source=www.baidu.com;JSESSIONID=aaajxOrX8n0wH4rJp1Zcy;YNOTE_CSTK=dQp-rxXo;gdxidpyhxdE=cS8UsOg6fIinRH%2BUmZZGSGerhY%2F8Yq%2FlBzWdmW2X5hJaUlO9EnE%2F5KBSl0oY6KmMC3T%2BGXhMGBVCHe2g7l7RuM3L8KXXu12kxPlg8f51B3W4wGiT7UY0xKzXcSRyG2twByx1jCGyecgtRtgcD1KxB725pJy5%2Bx4UOpicalQsq55QT3M4%3A1655130873451;YD00688109880970%3AWM_NI=oAUN8lEBXanztzxsPucSCEOO6Iv5WGBB3EbbRO5%2BV1TVbF0f9z1JkrCTsDw5DbgixFp4GcCnpLY8rMbnQ0LWTUQ7BcSKX7nSQm24aat5KizASCqwHT%2B8B33gG9TJiBRIZnA%3D;YD00688109880970%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee9ab33eba94f7a5b77b81968ab7d44f969f8e83d85bba90a2b0ce65a194a4b5eb2af0fea7c3b92aad9f9bafbb68879e9882ed72b8a6b894d37fa18d8da6ce45f697bad6d64d829efda6e16a9291fbccd53b988aaea7b36efba6ffabea7a818cbda5f63f88bea98afb4eb4ec8984c266b49497d9f147a2b29fd1cf5d988b9fd8c169919598d8ed5993b3fed5e46bb8eb858af94b919dbf98cb60e9e88ed4b26d85e79cabec4a9297968fc437e2a3;YNOTE_SESS=v2|25kuAJ-xiVlmh4UWkfpB0gun4ezhfqK0kWhMP4PLez0OEkMJZ6MzA0UfhMQL0LkW0UWOfeBOfzl0lWnLgz0fOY0pykfJLPMUfR;YNOTE_PERS=v2|cqq||YNOTE||web||-1||1655129999180||120.224.221.2||qqAD76829FF393961A3245DC81E3B04B48||qLnMkEnfeyRYY0M6unLwS0wyPLPz0MJBRgZh4k5hfPuRwunHw4nLwLRqyhHJzhfeF0gukLpy6LPu0PLk4PShfTyR;YNOTE_LOGIN=7||1655129999189",
            "acc": "qq1490316377",
        },
        {
            "cookie": "OUTFOX_SEARCH_USER_ID_NCOO=1111028308.689955;OUTFOX_SEARCH_USER_ID=\"-1713297431@10.108.160.131\";__yadk_uid=KuPN0nsEj2mJKMYiYThBZED8yXFa1vhi;YNOTE_PERS=v2|urstoken||YNOTE||web||-1||1641652817444||119.167.70.231||peakyu2020@163.com||YW0HpBkfYE0kMkL6uP4Q40eFO4Ju6MpFRqS0MJBnflE0PK6LOGkfJyROGRM6ZOMp40Uf0Mez6Mkf0QFhMpz0fUM0;YNOTE_USER=1;_9755xjdesxxd_=32;YD00688109880970:WM_TID=1a4Hb8uH2L9EBVVBQEJv7DGnZL2/jINU;hb_MA-AF8F-B2A48FFDAF15_source=www.baidu.com;YNOTE_SESS=v2|DZRC4OXRtWUlO4TLh4U5ReyPLOlOfwS0YGnLzfRfJ40zG0HlGPLUM0J4k4OfP4UA0eBnLOm6Me4RJLOLquhM6LR6yP4OEOMg40;JSESSIONID=aaa8Xv_W6Srmka-Fs1Zcy;YNOTE_CSTK=XS8lCQYL;gdxidpyhxdE=V3GCw1gJli+Yy5KjCj8Q8GznsteldYN+EncHxpcK1\\ViJLPE+hg6BP9R8x/xAjNUV8pd+WCiPd4\\j570jfPLiQZDG5TQ2xRm77K8jpETItwEzAclQU8q7yj/T7zCjV46YJgQ\\SsdPMeql6V1oandrVt\\MSHabs+uutdCUN9PL/4h3r6x:1655132392154;YD00688109880970:WM_NI=w5poA9NsQB8jG1DwpuL8RTNYHySsuacKxNCPg/bfcA0KOuCDNQwoHbg1rdFTq40/AGgFUCLy+VRnmCUcgnBvu5ouUrmo/Wsl4PBOWCOHLlN2NUtoAvYLFYo4VoS5sNBdNXA=;YD00688109880970:WM_NIKE=9ca17ae2e6ffcda170e2e6eeb3eb3aaeebbca3cb67f8eb8fa3c84f878a8eb0c54faabba289d66daf9988d7cd2af0fea7c3b92ab5ebc090c4338ead9fa3bb6285ef8c98f37f90e89eb5cd538ca79d94f86ba195b8afc25ca5f1ae87e24bf4958196c2508e8fb990cb6aa5efbe85c560b3ec00d0c44da59a9ba4cf73e98a9e8ff04997bda98fc17eb7eba196d87aafb1e1b8f268f8908eb0d6498d98848dcd3a8e8bbc90c47e9b948abaee4096b19dd6f24682bc82b9c437e2a3;YNOTE_LOGIN=5||1655131545573",
            "acc": "17864231874",
        },
    ],
}

# 推送微信消息
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
                "content": "有道云:\n" + txt
            },
            "safe": 0,
            }
    requests.post(url="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token={}".format(access_token),data=json.dumps(data))
    pass



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
    multi = config.get("multi")
    msg = ''
    for i in multi:
        re = start(i["cookie"])
        msg = msg + i["acc"] +'\n'+ re +'\n\n'
    weChatPush(msg)
