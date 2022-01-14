import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_family_given_name(self): 
        formatted_name = get_formatted_name('mao','zedong') # 毛澤東在英文中寫作Mao Zedong
        self.assertEqual(formatted_name, 'Mao Zedong')  # self.assertEqual內部特有檢驗代碼

if __name__ == '__main__':
    unittest.main()