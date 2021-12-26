from random import choice

cangku = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "q", "r", "y", "h", "g"]

param_1 = choice(cangku)
cangku.pop(cangku.index(param_1))


param_2 = choice(cangku)
cangku.pop(cangku.index(param_2))

param_3 = choice(cangku)
cangku.pop(cangku.index(param_3))

param_4 = choice(cangku)
cangku.pop(cangku.index(param_4))

print(f"{param_1}{param_2}{param_3}{param_4}")
