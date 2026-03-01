##### throw
- `throw`
	- 用于抛出用户自定义的异常
```js
throw expression;



function getRectArea(width, height) {
  if (isNaN(width) || isNaN(height)) {
    throw new Error('Parameter is not a number!');
  }
}

try {
  getRectArea(3, 'A');
} catch (e) {
  console.error(e);
  // Expected output: Error: Parameter is not a number!
}

```

