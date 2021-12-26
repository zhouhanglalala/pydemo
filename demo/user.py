class User:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.login_attempts = 0

    def describe_user(self):
        print(f"用户姓名：{self.first_name.title()}{self.last_name.title()}。")

    def greet_user(self):
        print(f"hello! {self.first_name.title()}{self.last_name.title()}\n")

    def increment_login_attempts(self):
        self.login_attempts += 1
        print(f"该用户尝试登陆{self.login_attempts}次。")

    def reset_login_attempts(self):
        self.login_attempts = 1
        print(f"该用户登陆次数重置为{self.login_attempts}次。\n")


class Admin(User):
    """特殊用户：管理员"""

    def __init__(self, first_name, last_name):
        """初始化一下父类的属性和方法"""
        super().__init__(first_name, last_name)
        self.privileges = Privileges()


class Privileges:
    """权限的类"""

    def __init__(self):
        self.privileges = ["can add post", "can delete post", "can ban user"]

    """把父类的方法移到这个新类里"""

    def show_privileges(self):
        print(f"先是管理员权限： \n{self.privileges}")


songGuo = Admin("song", "guo")
songGuo.privileges.show_privileges()


