## 建一個函數 姓氏 名字作為輸入 name_function.py
```
def get_formatted_name(family name, given name):
    full_name = f"{family name} {given name}"
    return full_name.title()
```
## name_function_testing.py 創建一個測試用例
```
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    def test_family_given_name(self):
        formatted_name = get_formatted_name('Mao', 'Zedong') #毛澤東在英文中寫作Mao Zedong
        self.assertEqual(formatted_name, 'Mao Zedong')  # self.assertEqual內部特有檢驗代碼

if __name__ == '__main__':
    unittest.main()

```

單元測試可以對一個模塊、一個函數或者一個類進行正確性檢驗的測試工作，提升我們的測試效率。

## 測試成功

![p](https://github.com/zxc21949049/sa110a/blob/master/fin/001.jpg)

第一行 代表測試通過

..........................

第二行 測試花費的時間

第三行 OK告訴我們這個測試用例通過


## 測試失敗

![p](https://github.com/zxc21949049/sa110a/blob/master/fin/002.jpg)

第一行的E（Error）

..........................

第二行 告訴我們失敗的測試函數

第三行 Trackback告訴我們具體的錯誤信息


參考教學:https://www.youtube.com/watch?v=ekjSThKyYKw&t=1s   模擬

