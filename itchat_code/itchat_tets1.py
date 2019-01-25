import itchat
import time
itchat.auto_login(enableCmdQR=2,hotReload=True)
friends = itchat.get_friends(update = True)

itchat.send('hello',toUserName='filehelper')

# find_name = '薄冰心'

# for i in friends:
#     if find_name == i["RemarkName"]:
#         print(i)

# #该函数获取各个变量
# def get_var(var):
#     variable = []
#     for i in friends:
#         value = i[var]
#         variable.append(value)
#     return variable

# NickName = get_var("NickName")
# # # Sex = get_var('Sex')
# # # Province = get_var('Province')
# City = get_var('City')
# # # Signature = get_var('Signature')
# rmkname = get_var("RemarkName")
# userid = get_var("UserName")

# from pandas import DataFrame

# data = {
#     'name':rmkname,
#     'ID':userid,
#     'NickName':NickName,
#     'city':City
# }

# open('chai','w').write(str(data))


# frame = DataFrame(data)
# frame.to_csv('chai.csv', index=True)

# # print(data)



# while(1):
#     itchat.send("hello ！",toUserName="@e4bc054191cab32227ead412a9ba7c73c955f2b8cdb810bb24dfc483ee83a151")
#     time.sleep(0.5)

    # chai_nkn = i["NickName"]
    # chai_rmk = i["RemarkName"]
    # print(chai_nkn + '==>' + chai_rmk)



# print(friends[])
