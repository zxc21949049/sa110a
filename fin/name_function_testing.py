import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('andrew', 'yang')
        self.assertEqual(formatted_name, 'Andrew Yang')  # self.assertEqual內部特有檢驗代碼

if __name__ == '__main__':
    unittest.main()