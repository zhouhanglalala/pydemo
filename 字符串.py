'''
###引号的使用

# word='字符串'
sentence="这是一个句子"
paragragh="""
    这是一个段落
    可以书写多行

"""
print(word)
print(sentence)
print(paragragh)

#三引号可以保存所有的格式
#单引号和双引号的区别
#a='I'm xiaoqian'  会报错
a="I'm xiaoqian"
b='I\'m xiaoqian'#需要用反制符
print(a,b)
c="tom says \"i love you \""#同理
d='join says "i like you"'
print(c,'\n',d)
'''
'''
###字符串的截取：把字符串当成列表。[起始位置：结束位置:步进值]（位置从0开始）
sentence="inn chengdu"
print(sentence[1:6])#截取到空格n che
print(sentence[0:10:3])#结果为i ed
#不写结束位置，默认到最后，同理不写初始位置
print(sentence[7:])#结果ngdu
print(sentence[:4])#中途被我改了字符串内容，结果不正确
#几个字符串相连用+
print("您好，"+"欢迎光临！")
print(sentence+"尽享一夏")#inn chengdu尽享一夏
print(sentence *5)
#r和转义字符反斜杠
print("xiao\nqian")
print(r"xiao\nqian")

'''
