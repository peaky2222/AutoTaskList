import requests

from AutoConfig import config
config_ = config.get("ikuun.eu")
url = "https://ikuuu.eu/user/checkin"
actokens = []

for i in config_:
    actokens.append(i["cookie"])
    
payload={}
headers = {
  'cookie': '',
  'origin': 'https://ikuuu.eu',
  'referer': 'https://ikuuu.eu/user',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
  'sec-ch-ua-platform': '"Windows"',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
  'x-requested-with': 'XMLHttpRequest',
  'accept': 'application/json, text/javascript, */*; q=0.01',
  'accept-language': 'zh,zh-CN;q=0.9,en-GB;q=0.8,en;q=0.7',
  'sec-ch-ua-mobile': '?0',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'Host': 'ikuuu.eu'
}

for i in actokens:
    headers['cookie'] = i
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
