class Restaurant:
    """餐厅属性和营业状况。"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化属性name和type。"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print(f"餐厅{self.restaurant_name.title()}的经营模式是{self.cuisine_type.title()}。")

    def open_restaurant(self):
        print(f"{self.restaurant_name.title()}正在营业。")

    def set_number_served(self, num):
        # 把人数指定为特定的值
        self.number_served = num
        print(f"有{self.number_served}人在这家餐厅吃过饭。")

    def increment_number_served(self, num_1):
        self.number_served += num_1
        print(f"有{self.number_served}人在这家餐厅吃过饭。")


# class IceCreamStand():

class IceCreamStand(Restaurant):
    """冰淇凌小店"""

    def __init__(self, restaurant_name, cuisine_type):
        """初始化一下父类的属性和方法"""
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = ["西红柿", "鸡蛋", "抹茶", "牛奶"]

    def des_flavors(self):
        print(f"小店推出的冰淇凌口味有：\n{self.flavors}")


my_shop = IceCreamStand("行行", "冰淇凌")
my_shop.describe_restaurant()
my_shop.des_flavors()
