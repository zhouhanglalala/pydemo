'''
#定义一个空的列表
list=[]
#一个有内容的列表，列表的字符类型可以不同
namelist=[0,"zhouhang","songguo"]
print(namelist[1])#zhouhang


#for循环执行列表的值
for name in namelist:
    print(name)#自动把列表的内容定义为name

print(len(namelist))
#while循环执行列表的值
lenth=len(namelist)
r=0
while r<lenth:
    print(namelist[r])
    print(r)
    r+=1
'''
'''
#增：列表名.append()
namelist=["肖倩","周行","松果"]
print("-------增加前，列表内容--------")
for name in namelist:
    print(name)

a=input("请输入姓名：")
namelist.append(a)    #在末尾追加元素
print("-------增加后，列表内容------")
for name in namelist:
    print(name)
'''
'''
#增加一个列表的数据：append,extend
a=[1,2,3]
b=[4,5,6]
a.append(b) #此时是将一个列表作为元素加入到a列表中
print(a)  #[1, 2, 3, [4, 5, 6]]
a.extend(b)  #是将一个列表的数据逐一的加入a列表中
print(a)
'''
'''
#增：insert制定表位置插入元素

a=[4,5,6,7]
a.insert(2,"xiao")  #第一个位置是索引，第二个位置是对象；
print(a)
'''
'''
#删：del，pop,remove
a=["天官赐福","魔道祖师","两不疑","咒术回战","镇魂街","鬼灭之刃"]
print("-------删除前，动漫列表--------")
for name in a:
    print(name)

#del a[4] #在指定位置删除元素
#a.pop() #删除末尾最后一个元素
a.remove("镇魂街") #删除指定内容，但仅仅删除第一个指定内容，并不会把重复的所有内容都删除
print("-------删除后，动漫列表------")
for name in a:
    print(name)
'''
'''
#改：
a=["天官赐福","魔道祖师","两不疑","咒术回战","镇魂街","鬼灭之刃"]
print("-------修改前，动漫列表--------")
for name in a:
    print(name)

a[1]="工作细胞" #修改指定位置的内容

print("-------修改后，动漫列表------")
for name in a:
    print(name)
'''
'''
#查：in,not in
a=["天官赐福","魔道祖师","两不疑","咒术回战","镇魂街","鬼灭之刃"]

b=input("请输入要查找的动漫名字：")
if b in a:
    print("在库里")
else:
    print("动漫库里没有您想找的动漫")
'''
'''
c=["周行","肖倩","松果","周行","周行","肖倩"]
print(c.index("周行",1,5)) #在指定位置上查找对象，如果有会返回对应索引
#print(c.index("小花",1,4)) #没有会报错
print(c.index("周行",1,3)) #区间范围，左闭右开，【1，3）

#统计次数
c=["周行","肖倩","松果","周行","周行","肖倩"]
print(c.count("松果"))

#排序和反转
a=[9,5,8,3,1]
a.reverse() #内容反转
print(a)
a.sort()#元素排序，升序
print(a)
a.sort(reverse=True)#降序，并且True大写
print(a)

#表的元素是表
a=[["西瓜","火龙果","芒果"],["萝卜","红薯","南瓜"],["鲜牛奶"],["玫瑰花","小野花"]]
print(a[1])#['萝卜', '红薯', '南瓜']
print(a[1][1])#红薯

#将8个老师随机分到3个办公室里
offices=[[],[],[]]
teachers=["a","b","c","d","e","f","g","h"]
import random
for teacher in teachers:
    index=random.randint(0,2)
    offices[index].append(teacher) #在几号办公室添加老师
print(offices)

#更加直观的看出来,for循环的层次运用
i=1
for office in offices:
    print("这是%d办公室，这里有%d个老师"%(i,len(office)))
    i+=1
    for teacher in office:
        print("%s"%teacher,end="\t")#end="\t"
    print("\n")
    print("-"*30)

'''










