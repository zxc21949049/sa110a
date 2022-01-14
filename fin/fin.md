## 建一個函數 姓氏 名字作為輸入 name_function.py
```
def get_formatted_name(family name, given name):
    full_name = family name  + ' ' + given name"  # 生成姓與名 (一種格式)
    return full_name.title()
```
## name_function_testing.py 創建一個測試用例
```
import unittest
from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase): # 測試name_fnction.py
    def test_family_given_name(self):   # 是一個特殊的method 能夠正確處理格式
        formatted_name = get_formatted_name('Mao', 'Zedong') # 毛澤東在英文中寫作Mao Zedong
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

第二行 告訴我們失敗的測試函數 對debug非常有幫助

第三行 Trackback告訴我們具體的錯誤信息

為了保證軟件的可靠性和安全性 我們可以為函數或類編寫測試代碼 這樣不僅僅可以簡化我們手動測試的工作 也幫助我們未來對軟件的維護和再開發更加方便

透過自動化測試取代人工測試 為的不單單只是降低成本 而是自動化測試帶來的優勢無可取代 速度快 品質高 可重複 彈性大 自動化 重要性

參考教學:https://www.youtube.com/watch?v=ekjSThKyYKw&t=1s   模擬

