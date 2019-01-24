from mx_lib import mxBot
chai_bot = mxBot()
speed = 10

while(1):
    left,right = chai_bot.getEncode()
    chai_bot.motor(10,10)
    print(left,right)
    