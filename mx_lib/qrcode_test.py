#!/usr/bin/env python 
# -*- coding: utf-8 -*- 
import os,sys
import cv2 
import pyzbar.pyzbar as pyzbar
import Image,ImageEnhance
from mx_lib import mxBot
import sys,time
reload(sys)  
sys.setdefaultencoding('utf8')  

mx_bot = mxBot()

cap = cv2.VideoCapture(2)

ret,frame = cap.read()
gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
cv2.imshow('frame',gray)
cv2.imwrite('qrcode.jpg',gray)
image = 'qrcode.jpg'
img = Image.open(image)    
barcodes = pyzbar.decode(img)
barcodeData = 0
for barcode in barcodes:
    barcodeData = barcode.data.decode("utf-8")
    print(barcodeData)
    
if len(barcodeData) >= 0:
    mx_bot.speak(str(barcodeData))
    print(len(barcodeData))
    print(barcodeData)
        
# mx_bot.speak("江城子")
        
    



