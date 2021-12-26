'''
a=() #创建一个空的元组 <class 'tuple'>
b=(7,)#创建有内容的元组，必须末尾加上逗号<class 'tuple'>
c=(7)#<class 'int'>
d=(3,5,6)#<class 'tuple'>
print(type(a))
print(type(b))
print(type(c))

#类似于列表
a=("xiaoqian","zhouhang","0409","0107")
print(a[-1])#0107
print(a[1])#zhouhang
print(a[1:3])#打印的时候是不包含结束索引的内容的，左闭右开('zhouhang', '0409')

#改：不能改
a=(0,"kiko","mac")

a[1]="毛戈平"
print(a)#TypeError: 'tuple' object does not support item assignment


#增,并不是在原来的元组中增加，而是创建了一个新的tuple，即连接
a=("kiko","mac")
b=("Armani","Dior","Bobbi Brown",)
c=("Estee Lauder","3 concept colors")

d=a+b+c#连接('kiko','mac', 'Armani', 'Dior', 'Bobbi Brown', 'Estee Lauder', '3 concept colors')
print(d)

'''
#删
b=("Armani","Dior","Bobbi Brown",)
del b#不是只把内容删除了，而是b元组彻底删除了
print(b)



#查















