## 蒙地卡羅方法
它是一種數值方法，利用亂數取樣 (random
sampling) 模擬來解決數學問題。
此方法的理論基礎於更早時候已為人所知，只不過用手動產生亂數
來解決問題，是一件費時又費力的繁瑣工作，必須等到電腦時代，使此繁複計
算工作才變得實際可執行

![p](https://github.com/zxc21949049/sa110a/blob/master/1.jpg)

## 蒙地卡羅方法基本原理
蒙地卡羅方法到底適合解決哪些問題？ 舉凡所有具有隨機效應的過程，均可能
以蒙地卡羅方法大量模擬單一事件，藉統計上平均值獲得某設定條件下實際最
可能測量值。現今此方法已被應用在許多領域中。

蒙地卡羅方法的基本原理是將所有可能結果發生的機率，定義出一機率密度函
數。將此機率密度函數累加成累積機率函數，調整其值最大值為 1，此稱為歸
一化(Normalization)。這也將正確反應出所有事件出現的總機率為 1 的機率特
性，這也為亂數取樣與實際問題模擬建立起連結。也就是說我們將電腦所產生
均勻分佈於 [0, 1] 之間的亂數，透過所欲模擬的過程所具有機率分佈函數，模
擬出實際問題最可能結果。

參考資料:http://blog.udn.com/wiselylin/2093294

## 蒙特卡洛算法经典应用(计算π的值)。 複製



```
	// 随机化值。
   function RadomLocation(min, max) {
        return min + Math.random() * (max - min);
    }
	
    function GeneratorPi(Counts) {
        let count = 0;
        for(let i=0;i<Counts;i++){
        // 采用半径为1的圆来进行测试。
        let x = RadomLocation(-1, 1);
        let y = RadomLocation(-1, 1);
        if ((x ** 2 + y ** 2) <= 1) {
            count++;
        }
        }
        return count * 4.0 / Counts;         //  count / Count 就是这个随机的值在总的次数的比率。
    }
    console.log(GeneratorPi(parseInt(prompt("请输入次数"))));
    
    ```
```
心得:蒙特卡洛算法特點 採樣的樣本越大 越接近真實值。

參考資料:https://blog.csdn.net/weixin_43629719/article/details/99466092