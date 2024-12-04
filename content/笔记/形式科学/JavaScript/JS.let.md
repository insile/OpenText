##### let 
- `let`
	- `let` 声明用于声明可重新赋值的块级作用域局部变量，并且可以选择将其初始化为一个值。
	- `let` 声明的范围是块作用域
	- `let` 声明的变量不会在作用域中被提升
	- `let` 不允许重新声明
	- `let` 在全局作用域中声明的变量不会成为 window 对象的属性
```js
let name1;
let name1 = value1;
let name1 = value1, name2 = value2;
let name1, name2 = value2;
let name1 = value1, name2, /* …, */ nameN = valueN;


let x = 1;

if (x === 1) {
  let x = 2;

  console.log(x);
  // Expected output: 2
}

console.log(x);
// Expected output: 1


```

