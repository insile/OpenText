##### break
- `break`
	- 终止当前循环或 switch 语句，并将程序控制权转移到终止语句后的语句。当在带有标签的语句内部使用时，它还可以用于跳过该标记语句。
```js
break;
break label;


let i = 0;

while (i < 6) {
  if (i === 3) {
    break;
  }
  i = i + 1;
}

console.log(i);
// Expected output: 3

```

