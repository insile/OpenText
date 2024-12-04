##### continue
- `continue`
	- 终止当前循环或标记循环的当前迭代中的语句执行，并在下一次迭代时继续执行循环。
```js
continue;
continue label;


let text = '';

for (let i = 0; i < 10; i++) {
  if (i === 3) {
    continue;
  }
  text = text + i;
}

console.log(text);
// Expected output: "012456789"

```

