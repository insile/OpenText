##### return
- `return`
	- 用于终止函数执行，并指定要返回给调用函数的值。
```js
return;
return expression;


function getRectArea(width, height) {
  if (width > 0 && height > 0) {
    return width * height;
  }
  return 0;
}

console.log(getRectArea(3, 4));
// Expected output: 12

console.log(getRectArea(-3, 4));
// Expected output: 0

```

