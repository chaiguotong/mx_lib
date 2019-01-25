import itchat
itchat.auto_login(enableCmdQR=2)


# @itchat.msg_register(itchat.content.TEXT)
# def print_content(msg):
#     print(msg.fromUserName)

user_id = itchat.get_friends(update=True)[0:1]
print((user_id[0].UserName))



# f = "/home/intel/Desktop/timg.jpg"
# itchat.send_image(f,toUserName='filehelper')

# itchat.run()


