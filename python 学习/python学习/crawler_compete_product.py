#!/usr/bin/python3

# class Site:
#     def __init__(self, name, url):
#         self.name = name       # public
#         self.__url = url   # private
#
#     def who(self):
#         print('name  : ', self.name)
#         print('url : ', self.__url)
#
#     def __foo(self):          # 私有方法
#         print('这是私有方法')
#
#     def foo(self):            # 公共方法
#         print('这是公共方法')
#         self.__foo()
#
# x = Site('菜鸟教程', 'www.runoob.com')
# x.who()        # 正常输出
# x.foo()        # 正常输出
# x.__foo()      # 报错

# 类定义
# class Site:
#     def __init__(self, name, url):
#         self.name = name
#         self.__url = url
#     def who(self):
#         print('name:', self.name)
#         print('url:', self.__url)
#
# siteObj = Site('菜鸟教程', 'www.runoob.com')
# siteObj.who()


# 数组
# list1 = ['physics', 'chemistry', 1997, 2000]
# list2 = [1, 4, 3, 4, 5, 6, 7]
#
# print ("list1[0]: ", list1[0])
# # 看不懂
# print ("list2[1:5]: ", list2[1:2])


# 保留字
# import keyword
#
# print(keyword.kwlist)


# 数组
# total = [
#     'item_one',
#     'item_two',
#     'item_three',
#     'item_four',
#     'item_five'
# ]
# print(total)


# 元组
# dict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'}
#
# print("dict['Name']", dict['Name'])
# print("dict['Age']", dict['Age'])
# print(dict)


# 函数
# 定义函数
# def printme(str):
#     "打印任何传入的字符串"
#     print(str)
#     return
#
# # 调用函数
# printme("我要调用用户自定义函数!")
# printme("再次调用同一函数")
#
# def aAddB(a, b):
#     return a + b
#
# print(1+2)
#
# def aAddB(a, b, c):
#     return a*b*c
#
# print(aAddB(4, 2, 4))
#
# total = 0;  # 这是一个全局变量
#
#
# # 可写函数说明
# def sum(arg1, arg2):
#     # 返回2个参数的和."
#     total = arg1 + arg2;  # total在这里是局部变量.
#     print( "函数内是局部变量 : ", total)
#     return total;
#
#
# # 调用sum函数
# sum(10, 20);
# print("函数外是全局变量 : ", total)


# number = 7
# guess = -1
# print("数字猜谜游戏!")
# while guess != number:
#     guess = int(input("请输入你猜的数字："))
#
#     if guess == number:
#         print("恭喜，你猜对了！")
#     elif guess < number:
#         print("猜的数字小了...")
#     elif guess > number:
#         print("猜的数字大了...")


# 异常捕获
# try:
#     int(input("请输入你猜的数字："))
# except Exception as e:
#     print('请输入数字', e.message)

# 循环
# sites = ["Baidu", "Google","Runoob","Taobao"]
# for site in sites:
#     if site == "Runoob":
#         print("菜鸟教程!")
#         print('hahahhah ')
#         break
#     print("循环数据 " + site)
# else:
#     print("没有循环数据!")
# print("完成循环!")


# from test import Person
# Person.show(2)


### 操作数据库
# import pymysql.cursors
#
# # 连接数据库
# connect = pymysql.Connect(
#     host='localhost',
#     port=3306,
#     user='root',
#     passwd='root',
#     db='test',
#     charset='utf8'
# )
# # 查询数据
# sql = "select * from test"
# # 获取游标
# cursor = connect.cursor()
# cursor.execute(sql)
#
# print(cursor.fetchall())
# exit()
# for row in cursor.fetchall():
#     print("Name:%s\tSaving:%.2f" % row)
# print('共查找出', cursor.rowcount, '条数据')


### 爬虫
# from urllib import request
# import http.cookiejar
#
# url="http://www.baidu.com"
# print('第三种方法')
# cj=http.cookiejar.CookieJar()
# opener=request.build_opener(request.HTTPCookieProcessor(cj))
# request.install_opener(opener)
# response3=request.urlopen(url)
# print(response3.getcode())
# print(cj)
# # print(response3.read())


### 正则
# import re
# # str='abc,afc,amc,aic,^abc'
# # res = 'abc'
# # print(re.findall(res, str))
# #
# #
# # res = re.sub('abc', '你妹', str)
# # print(res)
#
# line = "Cats are smarter than dogs"
# matchObj = re.search('than', line)
# print(matchObj)


### mysql
import mysqlDB

