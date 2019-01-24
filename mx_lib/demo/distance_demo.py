from mx_lib import mxBot

mx_bot = mxBot()

while(1):
    distance = mx_bot.ping(9)
    print(distance)