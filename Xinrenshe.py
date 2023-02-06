import requests

url = "https://xinrenclub.billowton.com/xrs-2.1.1/wx/sign/doSign"

actokens = ['96903244168e7a8631f6262e837d31a020175349601211600','794b3dfbde6bff961b731768266ae96803175349601312132','22dcda062b74726686948f75f89a4999d2175349601411458','74c2f5c1609f15253847e21c66ca545547174867935911449',]

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


url = "https://vipapi.wps.cn/wps_clock/v2"

payload='double=0&p=any9M6s%2Fli8P2uFzi%2FcefUKL8jnoJKFtqyaGAjVFOygR%2FUxUKdwT3pcZtsWlRJGo9BAsobpaVkS92%2Boae%2FhUdpuDfw1s17HdmTqx6dhDOVnkYtuTIS9S3BCFJxG5t6GnvY1cOj%2BGtAMkMAJOHck%2FgxEO%2BywdeMO37Yhfx7RkVEQ%3D&v=11.1.0.12763'
headers = {
  'Host': 'vipapi.wps.cn',
  'user-agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.138 Safari/537.36 MicroMessenger/7.0.4.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat/WMPF',
  'Content-Type': 'application/x-www-form-urlencoded',
  'Sec-Fetch-Site': 'cross-site',
  'Sec-Fetch-Mode': 'cors',
  'Sec-Fetch-Dest': 'empty',
  'Referer': 'https://vip.wps.cn/spa/2021/wps-sign/?position=2020_vip_massing',
  'Accept-Language': 'en-us,en',
  'Origin': 'https://vip.wps.cn',
  'Cookie': 'wps_sid=V02ST1Ut4jyj2S9Y8hqknR9A1D4n9Ow00a1aa49d00435d4e79; wpsua=V1BTVUEvMS4wIChwYy1vZmZpY2U6MTEuMS4wLjEyNzYzOyB3aW5kb3dzOjEwLjAgV09XNjQ7IGFkZDU5ZWZjYTMxZDkyNGYwYTU1OWQ0OGY4YzZlYjVhOlVFVkJTekl3TWpJPSk='
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
