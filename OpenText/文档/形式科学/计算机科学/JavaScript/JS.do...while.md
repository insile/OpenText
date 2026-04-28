##### do...while
- `do...while`
	- 创建循环，只要测试条件为 true，该循环就会执行指定语句。执行语句后会对条件进行评估，从而使指定语句至少执行一次
```js
do
  statement
while (condition);


let result = '';
let i = 0;

do {
  i = i + 1;
  result = result + i;
  console.log(result);
} while (i < 5);


```

