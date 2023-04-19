import requests
from AutoConfig import config
config_ = config.get("Keyan")

url = "https://www.ablesci.com/user/sign"
actokens = []

for i in config_:
    actokens.append(i["cookie"])

payload = {}
headers = {
  'Accept': 'application/json, text/javascript, */*; q=0.01',
  'Accept-language': 'zh,zh-CN;q=0.9,en-GB;q=0.8,en;q=0.7',
  'Cookie': '',
  'Referer': 'https://www.ablesci.com/',
  'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102"',
  'sec-ch-ua-mobile': '?0',
  'sec-ch-ua-platform': '"Windows"',
  'sec-fetch-dest': 'empty',
  'sec-fetch-mode': 'cors',
  'sec-fetch-site': 'same-origin',
  'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
  'X-Requested-With': 'XMLHttpRequest',
  'Host': 'www.ablesci.com',
  'Connection': 'keep-alive'
}


for i in actokens:
    headers['Cookie'] = i
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
