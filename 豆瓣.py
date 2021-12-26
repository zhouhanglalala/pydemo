
#
# #调用其他文件的函数
# from demo.文件操作 import a#从哪个文件里引入某函数,引入自定义的模块
# print(a(3,6))#打印函数下的
#
# from demo import 文件操作 #从某个包里引入某个文件
# print(文件操作.a(5,7))#打印某个文件中定义的函数


#引入系统的模块
import os
import sys

#引入第三方模块
import bs4  #网页解析，获取数据
import re   #正则表达式，进行文字匹配
import urllib.request,urllib.error   #制定URL，获取网页数据
import xlwt          #进行Excel操作
import sqlite3       #进行sqlite数据库操作


from bs4 import beautifulsoup


def main():
    baseurl="https://movie.douban.com/top250?start="


