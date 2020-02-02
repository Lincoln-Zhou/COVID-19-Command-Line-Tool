# coding=utf-8


import requests
import re
from prettytable import PrettyTable
from datetime import datetime
from requests import exceptions


# 用户自定义区
deathrate = True # 若不需要显示死亡率，请将本行True改为False
# 以下自定义格式统一为'地区'，中间使用英文逗号间隔
area = ['武汉', '北京', '上海', '江苏'] # 在此处自定义要在结果中显示的城市/地区，注意请不要加“省”“市”字样
country = ['美国'] # 在此处自定义要在结果中显示的境外国家，注意目前仅支持已出现病例的国家


header = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'}  # Deceive Python request
metadata = requests.get('https://3g.dxy.cn/newh5/view/pneumonia', headers=header)
error = False
isnull = False
try:
    servertime = requests.get('https://lab.isaaclin.cn/nCoV/api/overall', headers=header, timeout=10)
except:
    error = True
    isnull = True
    print('抱歉，最近更新时刻数据不可用')
metadata.encoding = 'utf-8'
if error is not True:
    servertime.encoding = 'utf-8'
    updatetime = servertime.text
text = metadata.text  # Get target source code, 'text' is 'str' type
pattern1 = re.compile(r'(?<=countRemark":"","confirmedCount":)\d*\D+\d*\D+\d*\D+\d*')
ChinaRawData = pattern1.findall(text)
datalist = re.findall(r"\d+\.?\d*", ChinaRawData[0])
for element in area:
	search = element + '","confirmedCount":'
	pattern = re.compile(rf'(?<={search})\d*\D+\d*\D+\d*\D+\d*')
	RawData = pattern.findall(text)
	datalist.extend(re.findall(r"\d+\.?\d*", RawData[0]))
for element in country:
	search = element + '","provinceShortName":"","cityName":"","confirmedCount":'
	pattern = re.compile(rf'(?<={search})\d*\D+\d*\D+\d*\D+\d*')
	RawData = pattern.findall(text)
	datalist.extend(re.findall(r"\d+\.?\d*", RawData[0]))
pattern0 = re.compile(r'(?<=updateTime": )\d+\.?\d*')
if error is not True:
    time = pattern0.findall(updatetime)
    ftime = datetime.fromtimestamp(int(time[0]) / 1000).strftime('%Y-%m-%d %H:%M:%S')
print('新型冠状病毒当前数据')
if isnull is not True:
    print('最后更新于北京时间', ftime)
table = PrettyTable(['地点', '确诊', '疑似', '治愈', '死亡'])
table.add_row(['全国', datalist[0], datalist[1], datalist[2], datalist[3]])
i = 4
for element in area:
	table.add_row([element, datalist[i], datalist[i + 1], datalist[i + 2], datalist[i + 3]])
	i = i + 4
for element in country:
	table.add_row([element, datalist[i], datalist[i + 1], datalist[i + 2], datalist[i + 3]])
	i = i + 4
print(table)
if deathrate:
	print('当前死亡率:', "{:.5}".format(100 * int(datalist[3]) / int(datalist[0])), '%')

