#!/usr/bin/env python2
# -*- coding: utf-8 -*-
from aip import AipSpeech
import os,time
import urllib,requests,json

""" 你的 APPID AK SK """
APP_ID = '15237082'
API_KEY = 'BLYTwp1ex3Tcvd0vaNGpjG64'
SECRET_KEY = '4RfNN4l6s0GnrAjViEfMomZIpN5Vn0Gw'

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

msg = '你好啊,这里是乐博士'

# 语音合成
result  = client.synthesis(msg, 'zh', 1, {
    'vol': 15,
    'per': 4,
    'pit': 6
})

print(result)

if not isinstance(result, dict):
    with open('/home/intel/Music/chai.mp3', 'wb') as f:
        f.write(result)
# os.system("play  ~/Music/chai.mp3")



#################################################### 语音识别

# 读取文件
def get_file_content(filePath):
    with open(filePath, 'rb') as fp:
        return fp.read()

# 识别本地文件
data = client.asr(get_file_content('/home/intel/Desktop/test.wav'), 'wav', 16000, {
    'dev_pid': 1536,
})

for i in data:
    print '\t',i,': ',data[i]



