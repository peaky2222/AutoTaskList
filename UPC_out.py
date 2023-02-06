import requests
import time
import random
import datetime

url = "https://service.upc.edu.cn/site/apps/launch"

payload='data=%7B%22app_id%22%3A%22458%22%2C%22node_id%22%3A%22%22%2C%22form_data%22%3A%7B%221259%22%3A%7B%22User_4%22%3A%22%E9%BD%90%E7%8E%89%E5%B3%B0%22%2C%22User_6%22%3A%22%E9%9D%92%E5%B2%9B%E8%BD%AF%E4%BB%B6%E5%AD%A6%E9%99%A2%E3%80%81%E8%AE%A1%E7%AE%97%E6%9C%BA%E7%A7%91%E5%AD%A6%E4%B8%8E%E6%8A%80%E6%9C%AF%E5%AD%A6%E9%99%A2%22%2C%22User_8%22%3A%22Z20070031%22%2C%22User_10%22%3A%22%E7%94%B5%E5%AD%90%E4%BF%A1%E6%81%AF-%E8%AE%A1%E7%AE%97%E6%9C%BA%E6%8A%80%E6%9C%AF%22%2C%22User_14%22%3A%2217806275268%22%2C%22User_55%22%3A%22%E6%B1%89%E6%97%8F%22%2C%22User_60%22%3A%22%E7%A0%942004%E7%8F%AD%22%2C%22Input_16%22%3A%22%E6%AD%A5%E8%A1%8C%22%2C%22Input_18%22%3A%2214769994368%22%2C%22Input_22%22%3A%22%E5%A4%96%E5%87%BA%E5%89%AA%E5%8F%91%22%2C%22Input_26%22%3A%22%E5%A4%96%E5%87%BA%22%2C%22Input_28%22%3A%22%E6%A1%82%E6%B5%B7%E6%BA%90%22%2C%22Input_30%22%3A%2217864231874%22%2C%22Calendar_20%22%3A%22xxxx-xx-xxT16%3A00%3A00.000Z%22%2C%22Checkbox_34%22%3A%5B%7B%22value%22%3A%221%22%2C%22name%22%3A%22%E6%9C%AC%E4%BA%BA%E4%B8%A5%E6%A0%BC%E6%8C%89%E7%85%A7%E8%AF%B7%E5%81%87%E5%A4%96%E5%87%BA%E8%A6%81%E6%B1%82%E5%81%9A%E5%A5%BD%E7%96%AB%E6%83%85%E9%98%B2%E6%8E%A7%E5%B7%A5%E4%BD%9C%EF%BC%8C%E4%B8%80%E5%8D%A1%E9%80%9A%2F%E8%BA%AB%E4%BB%BD%E8%AF%81%E7%A1%AE%E4%BF%9D%E6%9C%AC%E4%BA%BA%E4%BD%BF%E7%94%A8%EF%BC%8C%E6%89%80%E5%88%B0%E5%9C%B0%E7%82%B9%E3%80%81%E4%BA%A4%E9%80%9A%E6%96%B9%E5%BC%8F%E3%80%81%E8%BF%94%E6%A0%A1%E6%97%B6%E9%97%B4%E7%AD%89%E5%9D%87%E4%B8%8E%E8%AF%B7%E5%81%87%E6%89%80%E5%A1%AB%E5%86%99%E4%BF%A1%E6%81%AF%E4%B8%80%E8%87%B4%EF%BC%8C%E5%9C%A8%E5%A4%96%E5%87%BA%E6%9C%9F%E9%97%B4%E9%9A%8F%E6%97%B6%E4%B8%8E%E8%BE%85%E5%AF%BC%E5%91%98%E4%BF%9D%E6%8C%81%E8%81%94%E7%B3%BB%EF%BC%8C%E6%B3%A8%E9%87%8D%E4%BA%BA%E8%BA%AB%E5%AE%89%E5%85%A8%E3%80%81%E8%B4%A2%E4%BA%A7%E5%AE%89%E5%85%A8%EF%BC%8C%E8%8B%A5%E5%8F%91%E7%94%9F%E4%BA%8B%E6%95%85%EF%BC%8C%E8%B4%A3%E4%BB%BB%E8%87%AA%E8%B4%9F%E3%80%82%22%7D%5D%2C%22Validate_62%22%3A%22true%22%7D%7D%2C%22userview%22%3A1%7D&step=0&agent_uid=&starter_depart_id=61460'
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
