# TDD / BDD
## Test-driven Development (測試驅動開發):
先寫測試再開發程式
最大的好處是開發者寫出測試時 就可以瞭解這一個元件/方法最後會怎麼使用 同時也釐清程式該怎麼設計 
整個開發流程會在單元測試、撰寫程式、重構三者間不斷循環 是一種有效提升程式品質的開發方法
## Behavior-driven Development (行為驅動開發):
BDD 是 TDD 的進化版 除了一樣先寫測試再實作外 還要先寫規格
程式語法描述其極接近日常口語 相當簡單易懂 也可以執行

![p](https://github.com/zxc21949049/sa110a/blob/master/TB.jpg)

參考:https://medium.com/hobo-engineer/ricky%E7%AD%86%E8%A8%98-tdd-bdd-and-test-double-76eee9e75092

pullAllWith

```
export function pullAllWith(array, values)
var basePullAll = require('./_basePullAll');

function pullAllWith(array, values, comparator) {
  return (array && array.length && values && values.length)
    ? basePullAll(array, values, undefined, comparator)
    : array;
}

module.exports = pullAllWith;
```

pullAt
```
var arrayMap = require('./_arrayMap'),
    baseAt = require('./_baseAt'),
    basePullAt = require('./_basePullAt'),
    compareAscending = require('./_compareAscending'),
    flatRest = require('./_flatRest'),
    isIndex = require('./_isIndex');

var pullAt = flatRest(function(array, indexes) {
  var length = array == null ? 0 : array.length,
      result = baseAt(array, indexes);

  basePullAt(array, arrayMap(indexes, function(index) {
    return isIndex(index, length) ? +index : index;
  }).sort(compareAscending));

  return result;
});

module.exports = pullAt;
```

slice.js
```
var baseSlice = require('./_baseSlice'),
    isIterateeCall = require('./_isIterateeCall'),
    toInteger = require('./toInteger');

function slice(array, start, end) {
  var length = array == null ? 0 : array.length;
  if (!length) {
    return [];
  }
  if (end && typeof end != 'number' && isIterateeCall(array, start, end)) {
    start = 0;
    end = length;
  }
  else {
    start = start == null ? 0 : toInteger(start);
    end = end === undefined ? length : toInteger(end);
  }
  return baseSlice(array, start, end);
}

module.exports = slice;
```
