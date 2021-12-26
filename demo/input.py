# promt=input("please tell me your favorite car: ")
# print(f"\nLet me see if I can find you a {promt}.")

# message=input("请输入就餐人数： ")
# if int(message) > 8:
#     print("对不起，没有空余位置")
# else:
#     print("请就餐。")

# message=input("请输入一个数： ")
# if int(message) % 10 ==0:
#     print(f"{message} 是10的倍数。")
# if int(message) % 10 !=0:
#     print(f"{message} 不是10的倍数。")



# active=True
# while active:
#     message = input("请输入配料： ")
#     print(f"\n好的，我们会为pizza加上{message}.")
#     if message == "quit":
#         active=False


# active = True
# while active:
#     message = input("请输入配料： ")
#
#     if message == "quit":
#         active = False
#     else:
#         print(f"\n好的，我们会为pizza加上{message}.")

# active = True
# while active:
#     message = input("请输入查询年龄： ")
#     if message == "quit":
#         break
#
#     if int(message) < 3:
#         print("您好，不到三岁的儿童免费观影。")
#     if int(message) >=3 and int(message) <=12 :
#         print("您好，该年龄的儿童观影¥10。")
#     if int(message) > 12:
#         print(f"您好，年龄{message}的观众观影¥15")

# sandwich_orders=["hanghang","xiaoxiao","qianqian","zhouzhou","songsong","guoguo"]
# finished_sandwiches=[]
#
# while sandwich_orders:
#     now_sandwiches=sandwich_orders.pop()
#     print(f"I  made your {now_sandwiches} sandwich.")
#     finished_sandwiches.append(now_sandwiches)
# print(finished_sandwiches)

# sandwich_orders=["hanghang","pastrami","xiaoxiao","qianqian","pastrami","zhouzhou","songsong","guoguo","pastrami"]
# print("注意：牛肉pastrami卖完了。")
# #while sandwich_orders: #错误
# while "pastrami" in sandwich_orders:
#     sandwich_orders.remove("pastrami")
# for sandwich_order in sandwich_orders:sandwich_orders
#     print(sandwich_order.title())

# results={}
#
# active=True
# while active:
#     answer_1=input("If you could visit one place in the world,where would you go?\n")
#     answer_2 = input("What is your name?\n")
#     results[answer_2]=answer_1
#     repeat=input("you want another one answer the question? y/n\n")
#     if repeat=="n":
#         active=False
# for name,place in results.items():
#     print(f"{name.title()} want to go to {place.title()}.")

# def display_message(something):
#     print(f"我在这个章节学到了{something}.")
# display_message("函数")

# def make_shirt(shirt_scale="T",shirt_content="I LOVE YOU"):
#     print(f"需要的尺码为{shirt_scale.title()},字样为{shirt_content.title()}.")
# make_shirt()
# make_shirt("M")
# #大小无关紧要
# make_shirt(shirt_content="I hate YOU")
# make_shirt("M","超人")
# make_shirt(shirt_content="老婆",shirt_scale="s")


# def city_country(city, country):
#     message = f"{city},{country}"
#     return message
#
#
# print(city_country("beijing", "zhongguo"))
# print(city_country("shanghai", "zhongguo"))
# print(city_country("bali", "faguo"))

# def make_album(singer,album_name,song_num=None):
#     if song_num:
#         message=f"音乐人{singer.title()}创作了专辑{album_name.upper()},有歌曲{song_num}首。"
#     else:
#         message=f"音乐人{singer.title()}创作了专辑{album_name.upper()}"
#     return message
#
# print(make_album("许嵩","山水之间"))
# print(make_album("陈奕迅","红玫瑰","9"))
# print(make_album("韩红","青藏高原"))

# def make_album(singer, album_name):
#     message = {"歌手": singer, "专辑名称": album_name}  # 返回值为字典
#     return message
#
#
# while True:
#     print("输入q可以退出程序。")
#     ques_1 = input("请输入歌手的名字： ")
#     if ques_1 == "q":
#         break
#
#     ques_2 = input("请输入专辑名称： ")
#     print(make_album(ques_1, ques_2) )


# messages=["hello","sorry","see you","bye","night"]
# def show_messages():
#     print(messages)
#
# show_messages()

# messages=["hello","sorry","see you","bye","night"]
# sent_messages=[]
# messages_1=messages[:]
# while messages_1:
#     moving_message=messages_1.pop()
#     sent_messages.append(moving_message)
# def send_messages():
#     print(f"原列表：{messages}\n移动完的列表：{sent_messages}")
#
# send_messages()

def make_car(xinghao,chanshang,**something):
    #定义字典,让空字典something的键=函数
    #something[car_1]=xinghao #错误
    something["car_1"]=xinghao
    something["car_2"]=chanshang
    print(something)
make_car("xi","qianqian",color="blue",place="beijing")
make_car("xo","xiaoqian",color="green")


from car import *

