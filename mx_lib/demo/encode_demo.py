from mx_lib import mxBot

mx_bot = mxBot()
speed = 10

while(1):
    left,right = mx_bot.getEncode()
    if(right < 1320 and left < 1320 ):
        mx_bot.motor(speed,speed)
    elif(left >= 1320 and right >= 1320):
        mx_bot.stop()
    print("left :",left)
    print("right :",right)
