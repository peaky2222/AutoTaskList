import requests,json
# 微信推送
def weChatPush(txt):
    Secret = "GuaXXXXXXXXXXXXXXXXXXXn8Bs"
    corpid = 'wXXXXXXXXXXXXXXXXXf54f5b7b'
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

config = {
    # 时光相册登录信息
    "Shiguang": [
        {
            "account": "17XXXXXXXXX",
            "password": "XXXXXXXX",
            "push": "",  
        },
        
        # {
        #     "account": "123",
        #     "password": "123",
        #     "push": "pushplus",
        # },
    ],
    # 天翼云盘
    "Tianyi": [
        {
            "account": "17XXXXXXXXX",
            "password": "XXXXXXX.",
        },
        # {
        #     "account": "123",
        #     "password": "123",
        #     "push": "pushplus",
        # },
    ],
    # Upc
    "Upcup": [
        {
            "account": "Z2XXXXXXX",
            "password": "XXXXXXX.",
        },
        # {
        #     "account": "123",
        #     "password": "123",
        #     "push": "pushplus",
        # },
    ],
    # 信人社cookie
    "Xinren": [

        {
            "cookie": '96903244168XXXXXXXX020175349601211600',
        },
        {
            "cookie": '794b3dfbde6bff961b7317XXXXXXXe96803175349601312132',
        },
        {
            "cookie": '22dcda062b74726686XXXXXXXX2175349601411458',
        },
        {
            "cookie": '74c2f5c1609f1525XXXXXXXX5547174867935911449',
        },
        # {
        #     "account": "123",
        #     "password": "123",
        #     "push": "pushplus",
        # },
    ],
    # 有道云笔记
    "Youdao": [
        {
            "cookie": "Hm_lvt_53c97531c41019c3315b44853946c2c9=1638368228,16384591XXXXXXXX1638780273; Hm_lpvt_53c97531c41019c3315b44853946c2c9=1638780292; __yadk_uid=FDCVtBEw3oYZT2SZqscJJMs5D9S1LluP; _ga=GA1.2.512020070.1636185596; OUTFOX_SEARCH_USER_ID_NCOO=71044445.59344848; OUTFOX_SEARCH_USER_ID=\"-2121722484@10.108.160.131\"; P_INFO=17806275268|1638368253|1|youdaonote|00&99|null&null&null#shd&null#10#0|&0||17806275268; YNOTE_USER=1; _9755xjdesxxd_=32; gdxidpyhxdE=Ro45N0tdDYNqhEDjxsedxXB%5CQdeygUQjPxRBW9y6sLXqRVHM6GLau3j6iw4h%5CAnjo0AXxel6J3bpHh8MGwjGh74DfGkPdJS66BArB8PBalWNSE4N9NGMOU0lMdbKnPk%5CU7D%2Fx9it0dekiXpC%2FbhrLM%2F7%2FzISb3qIxJ41LufN%2F06lLAWY%3A1638369178472; YD00688109880970%3AWM_NIKE=9ca17ae2e6ffcda170e2e6eeb9e66189919e86d07d83a88aa3d15b828a8fafb540aeb0fbbbb73df5f0aeaacd2af0fea7c3b92ab2ed81b8f95bfcb9fdd2ea6db29e98b4e27c8cf1a08ce55c93a983b8b570fc9196bbf45ab0bda985bc798cbdaba4f1349beabdb2cc6593a8fbd9c85ea6af848cf153878bb983b2688cb3a196f560e99ca3aeb563edb9aaa7d25383b2a9a7b264a392f9d7b38089e8feabca6091929899d480b3b2b88ff05ca1afb985d74df7a782d3cc37e2a3; YD00688109880970%3AWM_NI=r3OWzQ8g31kgrBXScpH%2FPkfPQwMW6d8OZZqRlcgd9sHceCr8Y6sQIoQx58EVfqLkrYEUwb3lHmouvT%2BDmM6i%2FgfFSYAngF3haN760tK82JKTSNXxQtqnxnmPcqwdTG5yN2I%3D; YD00688109880970%3AWM_TID=DPYe1GK9vfVAAEBBFVIq8388M876kLNN; hb_MA-9057-2B94435F5EF6_source=sitoi.gitee.io; Hm_lvt_30b679eb2c90c60ff8679ce4ca562fcc=1638368225,1638370163; Hm_lvt_daa6306fe91b10d0ed6b39c4b0a407cd=1638369594,1638369597,1638457670,1638459139; JSESSIONID=aaakLLY4yAyO4h9_Dob2x; hb_MA-B0D8-94CBE089C042_source=www.baidu.com; _gid=GA1.2.1954358563.1638780273; _gat=1; YNOTE_CSTK=3jWsOQSX; PUBLIC_SHARE_351e08a72378206f9dd64d2281e9b83b=; YNOTE_SESS=v2|wD5ehg6JcWP4OLzlhHPZ0eykMz5kLU50QBkLgBOMUfRPz0LPynfUA0qzO4QS0LeyRwFkf6yP4kM0lWn4QBPLTz0qKOLYEkLzE0; YNOTE_PERS=v2|urstoken||YNOTE||web||-1||1638780289543||218.201.114.130||1490316377@qq.com||64PLqL6Mzf0YWhHOE0LlMRJBk4pZO4YGROE0Lw4nfYMReL6MTFP4JLROmOLklhfq40eFn4Y5kfOERQL6LT4OLeLR; YNOTE_LOGIN=3||1638780289550",
            "acc": "17XXXXXXX8",
        },
        {
            "cookie": "__yadk_uid=9tMGb8JnnxxDEq2Eg3Y5MblYyJ1sdEzx; OUTFOX_SEARCH_UXXXXXXXXX1875144752.3719869; OUTFOX_SEARCH_USER_ID=\"-1155064617@10.108.160.133\"; JSESSIONID=aaaXsTIJCUMzFbjhrob2x; YNOTE_CSTK=vsMsDI-c; YNOTE_USER=1; _9755xjdesxxd_=32; YD00688109880970:WM_NI=Em3O1cDu/lEWVBQomfKaOazrFycIQAuROuiifCF/ml9eCbWTQVwYl9fy1GjcgMtH8IRAxlsMJv5MarAG6FiAkMEoR2nT6eXmTiVaVXyKsZ9IsshH1C9D56+h3wgt+mMYeTE=; YD00688109880970:WM_NIKE=9ca17ae2e6ffcda170e2e6eeacfb42f4a9f78ac868a58a8ba6c45b978e9ebbaa34f799fcd9f35bf58d8bb2ce2af0fea7c3b92a87b3fdb0b46988abe18dc85d969e9f90f06e89bf8182f97a86a7adaad44bb78e8196ec63a69d8ad0f068fbbb8d83d660938ab9baef33a6a7ffa8e969a593bca9bb43929fb88df2478aaafbaee47a8399faa7ec4ba9938b90d13aae8cfa86db6798b79a82d554bb95bdbbbc43b1ada8a9b449fb9cfbd7aa64f1a9a995aa678f87abb5c837e2a3; YD00688109880970:WM_TID=V3xs6ZQDbSlERQUAQUd698Ts5pQ+TQAf; YNOTE_SESS=v2|Mx9AI9aJcWJLRfJLkfg4RJFRHpLRMTuRJZhMUWhMpyRPBhLYfRMpuR64hHT40MYf0gSh4TzOfgB0z50MeFRLwF0qS64kEkMkl0; YNOTE_PERS=v2|urstoken||YNOTE||web||-1||1638779806538||218.201.114.130||peakyu2020@163.com||T4kLOfh46Z0UY64J4h4YE0Q46Mwy6Lk5ROGnfJLh4Jz0UfnMUf6LQ4ROWhflY6M6Z0JuP4guPLkfRTKhLTFOLPF0; NTES_YD_SESS=or0xcq3HGuTjr9rw4GEOrtVi0wDqRq3EUQnVsN5ksx2IceKDcQzbiWuhor6NZf8t6UVQWxiWzluNutChvCFyq4fiMVTUj4ruTd6cnkJgddCjbv1k4UjgNIwUq2UaimRvklhNlF7i9IyqaIkeKT5KFhwHGuh8RfJI4.3Y0BmBxwgkji8_jOK7ks4gMbhyD73ixoqA8OgljUtuisHXa6INNc1jIASPsw8p1sy.4P5pDIxqL; S_INFO=1638779830|0|0&60##|17156087896; P_INFO=17156087896|1638779830|1|youdaonote|00&99|null&null&null#shd&370200#10#0|&0||17156087896; YNOTE_LOGIN=5||1638779867884; gdxidpyhxdE=0Z7VZ8f6nd\\yjgTVN6VhWOOhMGEshnwE/8uSfmcgIGUc9T4q+jqpGuuCPQQg\\divDWisYGW8SBDiD\\bexlYJ1BTgAjl\\Hbf/ZVgewjtxxROzYtd4peysJ1BgPbSdVQMSObs8aOpiX/xK5U/9+XK4ZPTWiC9KR8S+jcvUXRAUp4pqQdPd:1638780830842; PUBLIC_SHARE_351e08a72378206f9dd64d2281e9b83b=",
            "acc": "17XXXXXX96",
        },
        
    ],
    # WPS签到
    "Wps": [
        {
            "wps_sid": "wps_sid=V02SecXXXXXXXXXX00aaefe2000435d4e79",
        },
        # {
        #     "account": "123",
        #     "password": "123",
        #     "push": "pushplus",
        # },
    ],
    # Upcout payload='data=%7B%22app_id%22%3A%22458%22%2C%22node_id%22%3A%22%22%2C%22form_data%22%3A%7B%221259%22%3A%7B%22User_4%22%3A%22%E9%BD%90%E7%8E%89%E5%B3%B0%22%2C%22User_6%22%3A%22%E9%9D%92%E5%B2%9B%E8%BD%AF%E4%BB%B6%E5%AD%A6%E9%99%A2%E3%80%81%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6%E4%B8%8E%E6%8A%80%E6%9C%AF%E5%AD%A6%E9%99%A2%22%2C%22User_8%22%3A%22Z20070031%22%2C%22User_10%22%3A%22%E7%94%B5%E5%AD%90%E4%BF%A1%E6%81%AF-%E8%AE%A1%E7%AE%97%E6%9C%BA%E6%8A%80%E6%9C%AF%22%2C%22User_14%22%3A%2217806275268%22%2C%22User_55%22%3A%22%E6%B1%89%E6%97%8F%22%2C%22User_60%22%3A%22%E7%A0%942004%E7%8F%AD%22%2C%22Input_16%22%3A%22%E6%AD%A5%E8%A1%8C%22%2C%22Input_18%22%3A%2214769994368%22%2C%22Input_22%22%3A%22%E5%A4%96%E5%87%BA%E5%89%AA%E5%8F%91%22%2C%22Input_26%22%3A%22%E5%A4%96%E5%87%BA%22%2C%22Input_28%22%3A%22%E6%A1%82%E6%B5%B7%E6%BA%90%22%2C%22Input_30%22%3A%2217864231874%22%2C%22Calendar_20%22%3A%22xxxx-xx-xxT16%3A00%3A00.000Z%22%2C%22Checkbox_34%22%3A%5B%7B%22value%22%3A%221%22%2C%22name%22%3A%22%E6%9C%AC%E4%BA%BA%E4%B8%A5%E6%A0%BC%E6%8C%89%E7%85%A7%E8%AF%B7%E5%81%87%E5%A4%96%E5%87%BA%E8%A6%81%E6%B1%82%E5%81%9A%E5%A5%BD%E7%96%AB%E6%83%85%E9%98%B2%E6%8E%A7%E5%B7%A5%E4%BD%9C%EF%BC%8C%E4%B8%80%E5%8D%A1%E9%80%9A%2F%E8%BA%AB%E4%BB%BD%E8%AF%81%E7%A1%AE%E4%BF%9D%E6%9C%AC%E4%BA%BA%E4%BD%BF%E7%94%A8%EF%BC%8C%E6%89%80%E5%88%B0%E5%9C%B0%E7%82%B9%E3%80%81%E4%BA%A4%E9%80%9A%E6%96%B9%E5%BC%8F%E3%80%81%E8%BF%94%E6%A0%A1%E6%97%B6%E9%97%B4%E7%AD%89%E5%9D%87%E4%B8%8E%E8%AF%B7%E5%81%87%E6%89%80%E5%A1%AB%E5%86%99%E4%BF%A1%E6%81%AF%E4%B8%80%E8%87%B4%EF%BC%8C%E5%9C%A8%E5%A4%96%E5%87%BA%E6%9C%9F%E9%97%B4%E9%9A%8F%E6%97%B6%E4%B8%8E%E8%BE%85%E5%AF%BC%E5%91%98%E4%BF%9D%E6%8C%81%E8%81%94%E7%B3%BB%EF%BC%8C%E6%B3%A8%E9%87%8D%E4%BA%BA%E8%BA%AB%E5%AE%89%E5%85%A8%E3%80%81%E8%B4%A2%E4%BA%A7%E5%AE%89%E5%85%A8%EF%BC%8C%E8%8B%A5%E5%8F%91%E7%94%9F%E4%BA%8B%E6%95%85%EF%BC%8C%E8%B4%A3%E4%BB%BB%E8%87%AA%E8%B4%9F%E3%80%82%22%7D%5D%2C%22Validate_62%22%3A%22true%22%7D%7D%2C%22userview%22%3A1%7D&step=0&agent_uid=&starter_depart_id=61460'
    "Upcout": [
        {
            "cookie": data=%7B%22app_id%22%3A%22458%22XXXXXXXXXXX%B0%22%2C%22User_6%22%3A%22%E9%9D%92%E5%B2%9B%E8%BD%AF%E4%BB%B6%E5%AD%A6%E9%99%A2%E3%80%81%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6%E4%B8%8E%E6%8A%80%E6%9C%AF%E5%AD%A6%E9%99%A2%22%2C%22User_8%22%3A%22Z20070031%22%2C%22User_10%22%3A%22%E7%94%B5%E5%AD%90%E4%BF%A1%E6%81%AF-%E8%AE%A1%E7%AE%97%E6%9C%BA%E6%8A%80%E6%9C%AF%22%2C%22User_14%22%3A%2217806275268%22%2C%22User_55%22%3A%22%E6%B1%89%E6%97%8F%22%2C%22User_60%22%3A%22%E7%A0%942004%E7%8F%AD%22%2C%22Input_16%22%3A%22%E6%AD%A5%E8%A1%8C%22%2C%22Input_18%22%3A%2214769994368%22%2C%22Input_22%22%3A%22%E5%A4%96%E5%87%BA%E5%89%AA%E5%8F%91%22%2C%22Input_26%22%3A%22%E5%A4%96%E5%87%BA%22%2C%22Input_28%22%3A%22%E6%A1%82%E6%B5%B7%E6%BA%90%22%2C%22Input_30%22%3A%2217864231874%22%2C%22Calendar_20%22%3A%22xxxx-xx-xxT16%3A00%3A00.000Z%22%2C%22Checkbox_34%22%3A%5B%7B%22value%22%3A%221%22%2C%22name%22%3A%22%E6%9C%AC%E4%BA%BA%E4%B8%A5%E6%A0%BC%E6%8C%89%E7%85%A7%E8%AF%B7%E5%81%87%E5%A4%96%E5%87%BA%E8%A6%81%E6%B1%82%E5%81%9A%E5%A5%BD%E7%96%AB%E6%83%85%E9%98%B2%E6%8E%A7%E5%B7%A5%E4%BD%9C%EF%BC%8C%E4%B8%80%E5%8D%A1%E9%80%9A%2F%E8%BA%AB%E4%BB%BD%E8%AF%81%E7%A1%AE%E4%BF%9D%E6%9C%AC%E4%BA%BA%E4%BD%BF%E7%94%A8%EF%BC%8C%E6%89%80%E5%88%B0%E5%9C%B0%E7%82%B9%E3%80%81%E4%BA%A4%E9%80%9A%E6%96%B9%E5%BC%8F%E3%80%81%E8%BF%94%E6%A0%A1%E6%97%B6%E9%97%B4%E7%AD%89%E5%9D%87%E4%B8%8E%E8%AF%B7%E5%81%87%E6%89%80%E5%A1%AB%E5%86%99%E4%BF%A1%E6%81%AF%E4%B8%80%E8%87%B4%EF%BC%8C%E5%9C%A8%E5%A4%96%E5%87%BA%E6%9C%9F%E9%97%B4%E9%9A%8F%E6%97%B6%E4%B8%8E%E8%BE%85%E5%AF%BC%E5%91%98%E4%BF%9D%E6%8C%81%E8%81%94%E7%B3%BB%EF%BC%8C%E6%B3%A8%E9%87%8D%E4%BA%BA%E8%BA%AB%E5%AE%89%E5%85%A8%E3%80%81%E8%B4%A2%E4%BA%A7%E5%AE%89%E5%85%A8%EF%BC%8C%E8%8B%A5%E5%8F%91%E7%94%9F%E4%BA%8B%E6%95%85%EF%BC%8C%E8%B4%A3%E4%BB%BB%E8%87%AA%E8%B4%9F%E3%80%82%22%7D%5D%2C%22Validate_62%22%3A%22true%22%7D%7D%2C%22userview%22%3A1%7D&step=0&agent_uid=&starter_depart_id=61460',
            
        },
        # {
        #     "account": "123",
        #     "password": "123",
        #     "push": "pushplus",
        # },
    ],
    # Ikuun.eu cookie
    "ikuun.eu": [

        {
            "cookie": '96903244168XXXXXXXX020175349601211600',
        },
        {
            "cookie": '794b3dfbde6bff961b7317XXXXXXXe96803175349601312132',
        },
        {
            "cookie": '22dcda062b74726686XXXXXXXX2175349601411458',
        },
        {
            "cookie": '74c2f5c1609f1525XXXXXXXX5547174867935911449',
        },
        # {
        #     "account": "123",
        #     "password": "123",
        #     "push": "pushplus",
        # },
    ],
    # 信人社cookie
    "Keyan": [

        {
            "cookie": '96903244168XXXXXXXX020175349601211600',
        },
        {
            "cookie": '794b3dfbde6bff961b7317XXXXXXXe96803175349601312132',
        },
        {
            "cookie": '22dcda062b74726686XXXXXXXX2175349601411458',
        },
        {
            "cookie": '74c2f5c1609f1525XXXXXXXX5547174867935911449',
        },
        # {
        #     "account": "123",
        #     "password": "123",
        #     "push": "pushplus",
        # },
    ],
    # Miuivercookie
    "Miuiver": [

        {
            "cookie": '96903244168XXXXXXXX020175349601211600',
        },
        {
            "cookie": '794b3dfbde6bff961b7317XXXXXXXe96803175349601312132',
        },
        {
            "cookie": '22dcda062b74726686XXXXXXXX2175349601411458',
        },
        {
            "cookie": '74c2f5c1609f1525XXXXXXXX5547174867935911449',
        },
        # {
        #     "account": "123",
        #     "password": "123",
        #     "push": "pushplus",
        # },
    ],
}
