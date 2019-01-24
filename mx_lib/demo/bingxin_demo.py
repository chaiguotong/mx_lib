from mx_lib import mxBot
bx_bot = mxBot()
while True:
    bx_bot.motor(10,50)
    bx_bot.delay(2)
    bx_bot.stop()
    # bx_bot.delay(2)
    break
