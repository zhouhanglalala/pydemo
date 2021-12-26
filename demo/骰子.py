class Die:
    """创建一个die类"""

    def __init__(self):
        self.sides = 6

    """创建一个方法"""

    def roll_die(self):
        from random import randint
        print(randint(1, 6))

"""先创建对象"""
die=Die()
die.roll_die()