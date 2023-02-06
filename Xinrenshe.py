import requests

from AutoConfig import config
config_ = config.get("Xinren")

url = "https://xinrenclub.billowton.com/xrs-2.1.1/wx/sign/doSign"
actokens = []

for i in config_:
    actokens.append(i["cookie"])
    
payload = "{\"showAd\":0}"
headers = {
  'Host': 'xinrenclub.billowton.com',
  'xweb_xhr': '1',
  'actoken': '',
  'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF',
  'Content-Type': 'application/json;charset=utf-8',
  'Sec-Fetch-Site': 'cross-site',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://servicewechat.com/wxd5ca8ac35f47a799/67/page-frame.html',
  'Accept-Language': 'en-us,en',
  'Cookie': 'JSESSIONID=18208F88F946709B0DE2A5AB07D46B0C'
}

for i in actokens:
    headers['actoken'] = i
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)

