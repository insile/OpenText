##### label
- `label`
	- 标记语句可以和 break 或 continue 语句一起使用。标记就是在一条语句前面加个可以引用的标识符
```js
label :
   statement



let str = '';

loop1: for (let i = 0; i < 5; i++) {
  if (i === 1) {
    continue loop1;
  }
  str = str + i;
}

console.log(str);
// Expected output: "0234"

```

