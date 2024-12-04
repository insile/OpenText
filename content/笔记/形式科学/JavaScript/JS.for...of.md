##### for...of
- `for...of`
	- 循环按顺序逐个处理从可迭代对象获取的值
```js
for (variable of iterable)
  statement


let result = '';
let i = 0;

const array1 = ['a', 'b', 'c'];

for (const element of array1) {
  console.log(element);
}

// Expected output: "a"
// Expected output: "b"
// Expected output: "c"


```

