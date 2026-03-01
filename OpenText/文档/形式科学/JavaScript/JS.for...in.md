##### for...in
- `for...in`
	- 迭代一个对象所有可枚举属性
```js
for (variable in object)
  statement


const object = { a: 1, b: 2, c: 3 };

for (const property in object) {
  console.log(`${property}: ${object[property]}`);
}

// Expected output:
// "a: 1"
// "b: 2"
// "c: 3"

```

