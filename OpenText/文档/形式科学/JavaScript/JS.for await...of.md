##### for await...of
- `for await...of`
	- 创建循环，异步迭代
```js
for await (variable of iterable)
  statement



async function* foo() {
  yield 1;
  yield 2;
}

(async function () {
  for await (const num of foo()) {
    console.log(num);
    // Expected output: 1

    break; // Closes iterator, triggers return
  }
})();

```

