with open("编写数据文件/learning_python.txt") as fi:
    content = fi.read()
    print(content.replace("Python", "C++"))

