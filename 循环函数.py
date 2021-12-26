''''### for循环的第一行代码结束有冒号
# 默认从0开始
for a in range(7):
    print(a)
# 每次加3
for b in range(5, 22, 6):
    print(b)
for c in range(-30, -110, -50):
    print(c)
#在文本类型下应用
name = 'xiaoqian'
for d in name:
    print(d, end='\t')
#在列表中应用
l=['xiaoqian','songguo','zhouhang']
for m in range(len(l)):
    print(m,l[m]) #显示结果：0 xiaoqian 1 songguo 2 zhouhang
'''
'''
####while循环也有冒号
i=8
while i<50:
    print('当前是第%d次循环'%(i+12))
    print('i=%d'%i)
    i +=12

#小题目：1-100求和
n=100
sum=0
counter=1
while counter<=100:
    sum=sum+counter
    counter+=1
    print('1到%d的求和为%d'%(n,sum))

#和while连用
count=0
while count<=10:
    print(count,'小于等于10')
    count+=3
else:
    print(count,'大于10')
'''
'''
#break中断，continue相当于跳过，之结束当次循环
a=9
while a<99:
    a=a+10
    print('~'*20)
    if a==39:
        continue
    print(a)
'''

