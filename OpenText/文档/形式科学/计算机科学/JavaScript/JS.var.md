##### var 
- `var`
	- 可以是函数作用域或全局作用域，不能为块级作用域
	- `var` 声明函数作用域内自动提升，赋值不会
	- `var` 允许重新声明
	- `var` 在全局作用域中声明的变量会成为 window 对象的属性
```js
var name1;
var name1 = value1;
var name1 = value1, name2 = value2;
var name1, name2 = value2;
var name1 = value1, name2, /* …, */ nameN = valueN;


var x = 1;

if (x === 1) {
  var x = 2;

  console.log(x);
  // Expected output: 2
}

console.log(x);
// Expected output: 2

```

