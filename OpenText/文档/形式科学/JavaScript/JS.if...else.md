##### if...else
- `if...else`
	- 在指定的条件为真时执行一个语句。如果条件为假，则会执行可选的 else 子句中的另一个语句。
```js
if (condition)
  statement1

// 带有 else 子句
if (condition)
  statement1
else
  statement2



function testNum(a) {
  let result;
  if (a > 0) {
    result = 'positive';
  } else {
    result = 'NOT positive';
  }
  return result;
}

console.log(testNum(-5));
// Expected output: "NOT positive"


```

