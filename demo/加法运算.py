while True:
    try:
        fir_num = int(input("请输入第一个数： \n"))
        sec_num = int(input("请输入第二个数： \n"))
        sum = fir_num + sec_num
    except:
        print("请输入数值！")
    else:
        print(f"两数之和为： {sum}")


