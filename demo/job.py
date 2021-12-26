class Employee:
    def __init__(self, first_name, last_name, anual_salary):
        self.first_name = first_name
        self.last_name = last_name
        self.anual_salary = anual_salary

    def give_raise(self, increase_salary=5000):
        self.anual_salary += increase_salary
        return self.anual_salary


a = Employee("XIAO", "QIAN", 1000)
a.give_raise(4000)
print(f"{a.first_name}{a.last_name},年薪{a.anual_salary}")
