
```
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_first_last_name(self):
        formatted_name = get_formatted_name('andrew', 'yang')
        self.assertEqual(formatted_name, 'Andrew Yang')  # self.assertEqual內部特有檢驗代碼

if __name__ == '__main__':
    unittest.main()

```
## 測試成功

![p]()
第一行 代表測試通過
..........................
第二行 測試花費的時間
第三行 OK告訴我們這個測試用例通過

參考教學:https://turingplanet.org/2019/10/04/python-testing/