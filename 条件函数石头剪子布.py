''''
#条件判断语句:缩进、冒号,结束可以直接用elif，即elif和else可以一起使用，也可以单独使用；

age=55
if age>=18 and age<30:
    print('都市丽人')
elif age>=30 and age<80:
    print('成熟妇人')
else:
    print('甜美萝莉')

xingbie=9#性别为1，男生
danshen=0#单身为1，单身
if xingbie==1:
    print('男生')
    if danshen==1:
        print('咱俩凑合一下吧？')
    else:
        print('给我介绍一个呗')
else:
    print('一定要好好找男朋友哦～')

#引入随机库
import random
d=random.randint(90,100)#randint整数型
print(d)
'''
#石头剪刀布
#输入数字
a=int(input())

if a==0:
    print('您的输入为：石头（0）')
elif a==1:
    print('您的输入为：剪刀（1）')
elif a ==2:
    print('您的输入为：布（2）')
#引入随机库
import random
b=random.randint(0,2)

if b==0:
    print('系统随机生成数字为：石头（0）')
elif b==1:
    print('系统随机生成数字为：剪刀（1）')
else:
    print('系统随机生成数字为：布（2）')
#比较
if a==0 and b == 1:
    print('您赢啦:)')
elif a==0 and b == 2:
    print('hh你输啦:(')
elif b == a:
    print('平局啦')
elif a==1 and b == 0:
    print('hh您输啦:(')
elif a == 1 and b == 2:
    print('您赢啦:)')
elif a == 2 and b == 0:
    print('您赢啦:)')
elif a == 2 and b == 1:
    print('hh您输啦:(')



'''

if a==0:
    print('您的输入为：石头（0）')
    if b == 1:
        print('您赢啦:)')
    elif b == 2:
        print('hh你输啦:(')
    elif b == a:
        print('平局啦')
elif a==1:
    print('您的输入为：剪刀（1）')
    if b == 0:
       print('hh您输啦:(')
    elif b==2:
       print('您赢啦:)')
    elif b == a:
        print('平局啦')
elif a == 2:
    print('您的输入为：布（2）')
    if b == 0:
       print('您赢啦:)')
    elif b == 1:
       print('hh您输啦:(')
    elif b == a:
        print('平局啦')
'''
'''
if a=='0' and b==1:
    print('您赢啦:)')
elif a=='0' and b==2:
    print('hh你输啦:(')
elif a=='1' and b==0:
    print('hh您输啦:(')
elif a=='1' and b==2:
    print('您赢啦:)')
elif a=='2' and b==0:
    print('您赢啦:)')
elif a=='2' and b==1:
    print('hh您输啦:(')
elif a==b:
    print('平局啦')
'''