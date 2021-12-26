"""导入单元测试模块和要测试的函数"""
import unittest
from city_functions import place

"""创建一个继承单元测试的类"""


class PlaceTestCase(unittest.TestCase):
    """创建测试方法"""

    def test_city_country(self):
        """能正确格式化城市和国家吗?"""
        formatted_place = place("beijing", "zhongguo")
        """进行断言"""
        self.assertEqual(formatted_place, "Beijing,Zhongguo")


if __name__ == "__main__":
    unittest.main()
