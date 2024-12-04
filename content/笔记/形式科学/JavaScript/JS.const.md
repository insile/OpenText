##### const
- `const`
	- `const` 声明用于声明块作用域的局部变量作为常量。
	- 常量的值不能通过使用赋值运算符重新赋值来更改，但是如果常量是一个对象，它的属性可以被添加、更新或删除。

```js
const name1 = value1;
const name1 = value1, name2 = value2;
const name1 = value1, name2 = value2, /* …, */ nameN = valueN;


const number = 42;

try {
  number = 99;
} catch (err) {
  console.log(err);
  // Expected output: TypeError: invalid assignment to const 'number'
  // (Note: the exact output may be browser-dependent)
}

console.log(number);
// Expected output: 42
```

