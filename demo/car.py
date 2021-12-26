
"""
描述一辆车的型号，厂商和其他信息。
"""


def make_car(xinghao,chanshang,**something):
    #定义字典,让空字典something的键=函数
    #something[car_1]=xinghao #错误
    something["car_1"]=xinghao
    something["car_2"]=chanshang
    print(something)


