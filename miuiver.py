import requests
import time
import random
from AutoConfig import config,weChatPush
config_ = config.get("Miuiver")

url = "https://miuiver.com/wp-admin/admin-ajax.php"
actokens = []

for i in config_:
    actokens.append(i["cookie"])

payload = 'action=epd_checkinepd_checkin'
headers = {
  'Host': 'miuiver.com',
  'Connection': 'keep-alive',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
  'X-Requested-With': 'XMLHttpRequest',
  'sec-ch-ua-mobile': '?1',
  'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Mobile Safari/537.36',
  'sec-ch-ua-platform': '"Android"',
  'Origin': 'https://miuiver.com',
  'Sec-Fetch-Site': 'same-origin',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://miuiver.com/user-profile/',
  'Accept-Language': 'zh-CN,zh;q=0.9',
  'Cookie': '',
  'Accept-Encoding': 'gzip, deflate',
  'Content-Length': '18'
}

#time.sleep(random.randint(300, 500))
for i in actokens:
    headers['Cookie'] = i
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
