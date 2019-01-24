#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
from mx_lib import mxBot
chai_bot = mxBot()
fw_speed = 10
bc_speed = -5
while(1):
    
    if chai_bot.ping(8) >= 30:
        chai_bot.motor(fw_speed,fw_speed)
    elif chai_bot.ping(8) <= 15:
        chai_bot.motor(bc_speed,bc_speed)
    else:
        chai_bot.stop()
        chai_bot.turn(90,1)
    data = chai_bot.qrcode_rt()
    chai_bot.speak(data)
