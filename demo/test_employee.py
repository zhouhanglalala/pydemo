import unittest
from job import Employee


class TestEmployee(unittest.TestCase):
    # setUp会在每次调用测试方法前自动调用

    def setUp(self):
        self.employee = Employee("XIAO", "QIAN", 1000)
        self.list = [ 3000, 6000]

    def test_give_raise_by_default(self):
        self.assertTrue(self.employee.give_raise() == 6000)
        self.employee.anual_salary = 1000
        self.assertFalse(self.employee.give_raise() == 3000)
        self.employee.anual_salary = 1000
        self.assertEqual(self.employee.give_raise(), 6000)
        self.employee.anual_salary = 1000
        self.assertNotEqual(self.employee.give_raise(), 3000)
        self.employee.anual_salary = 1000
        self.assertIn(self.employee.give_raise(), self.list)
        self.employee.anual_salary = 1000
        self.assertNotIn(self.employee.give_raise()+1000, self.list)

    def test_give_raise_by_given(self):
        self.assertTrue(self.employee.give_raise(2000) == 3000)
        self.employee.anual_salary = 1000
        self.assertFalse(self.employee.give_raise(2000) == 6000)
        self.employee.anual_salary = 1000
        self.assertEqual(self.employee.give_raise(2000), 3000)
        self.employee.anual_salary = 1000
        self.assertNotEqual(self.employee.give_raise(2000), 6000)
        self.employee.anual_salary = 1000
        self.assertIn(self.employee.give_raise(2000), self.list)
        self.employee.anual_salary = 1000
        self.assertNotIn(self.employee.give_raise(2000)+1000, self.list)
