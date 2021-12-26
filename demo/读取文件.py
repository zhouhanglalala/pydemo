# with open("编写数据文件/learning_python.txt") as f:
#     content = f.read()
#
# """打印全部数据"""
# print(content)
#
# with open("编写数据文件/learning_python.txt") as f:
#
#    """遍历文件"""
#     for line in f:
#         print(line.strip())
#
# with open("编写数据文件/learning_python.txt") as f:
#
#     """遍历每一行并创建一个列表储存他们"""
#     lines = f.readlines()
#     for line in lines:
#         print(line.strip())

# try:
#     with open("编写数据文件/cat.txt") as f:
#         content = f.read()
#     print(content)
# except:
#     print("cat文件不存在！")
#
# try:
#     with open("编写数据文件/dog.txt") as fi:
#         content_1 = fi.read()
#     print(content_1)
# except:
#     print("dog文件不存在！")

try:
    with open("编写数据文件/cat.txt") as f:
        content = f.read()
    print(content + "\n")
    with open("编写数据文件/dog.txt") as fi:
        content_1 = fi.read()
    print(content_1)

except:
    pass

