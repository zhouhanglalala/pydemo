while True:
    name = input("请输入您的姓名： ")
    with open("编写数据文件/guest.txt", "a") as f:
        f.write(name+'\n')
    with open("编写数据文件/guest.txt") as f:
        content = f.read()
    print(content)
