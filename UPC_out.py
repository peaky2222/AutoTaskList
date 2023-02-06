import requests
import time
import random
import datetime

url = "https://service.upc.edu.cn/site/apps/launch"
from AutoConfig import config
config_ = config.get("Upcout")

payload=config_[0].get("cookie")



today = datetime.datetime.now()
tomorrow = today + datetime.timedelta(days=1)
r_time = tomorrow.strftime("%Y-%m-%d")

payload = payload.replace("xxxx-xx-xx",r_time)
headers = {
  'Accept': 'application/json, text/plain, */*',
  'Accept-Encoding': 'gzip, deflate, br',
  'Accept-Language': 'zh,zh-CN;q=0.9,en-GB;q=0.8,en;q=0.7',
  'Connection': 'keep-alive',
  'Content-Length': '2004',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Cookie': 'PHPSESSID=js5fidtimfm5886lgo8ihuini3; vjuid=214964; vjvd=1518712af6566af834bd4a0c2f9a57b5; vt=179291249',
  'Host': 'service.upc.edu.cn',
  'Origin': 'https://service.upc.edu.cn',
  'Referer': 'https://service.upc.edu.cn/v2/matter/start?id=458',
  'Sec-Fetch-Dest': 'empty',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Site': 'same-origin',
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest'
}
a = random.randint(300, 500)
time.sleep(a)
response = requests.request("POST", url, headers=headers, data=payload)
print(response.text)
