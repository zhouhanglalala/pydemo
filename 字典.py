
'''



info={"name":"xiaoqian","borntime":"1997"}#定义
print(info["borntime"])#查询

#查找字典里不存在的键
print(info["age"])#报错
print(info.get("age"))#None
print(info.get("age","没有的撒"))#没有的撒，可以设定默认值


#增
info={"name":"xiaoqian","borntime":"1997"}
sexinfo=input("请输入性别：")
info["sex"]=sexinfo
print(info)#{'name': 'xiaoqian', 'borntime': '1997', 'sex': 'nv'}
'''

# #删：del,clear
# info={"name":"xiaoqian","borntime":"1997","sex":"女"}
# print("删除前，%s" %info["sex"])
# del info["sex"]#删除整个键值对
# print("删除后，%s" %info)
# print("删除后，%s" %info["sex"])#报错
# del info #删除整个字典

# info={"name":"xiaoqian","borntime":"1997","sex":"女"}
# info.clear()#清空字典内容
# print(info)#{}

# #修改
#
# info={"name":"xiaoqian","borntime":"1997","sex":"女"}
# info["name"]="zhouhang"
# print(info)#{'name': 'zhouhang', 'borntime': '1997', 'sex': '女'}

#查：键和值的查询
# info={"name":"xiaoqian","borntime":"1997","sex":"女"}
# print(info.keys())#得到所有的键
# print(info.values()) #值
# print(info.items())#每个键值对是一个元组dict_items([('name', 'xiaoqian'), ('borntime', '1997'), ('sex', '女')])
#

# #遍历所有的值
# info={"name":"xiaoqian","borntime":"1997","sex":"女"}
# for key,value in info.items():#同时用两个值来for循环
#     print("key=%s,value=%s"%(key,value))
# for value in info.values():#正确
#     print(value)
# for value in info.values:#错误，就差括号
#     print(value)

#新函数：enumerate 枚举函数，同时拿到列表中的下标和内容
a=[1,3,6,8,5]
print(enumerate(a))#<enumerate object at 0x10acafe40>
for id,value in enumerate(a):
    print(id+1,value)
'''
1 1
2 3
3 6
4 8
5 5
'''