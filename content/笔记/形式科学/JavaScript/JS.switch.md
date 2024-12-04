##### switch
- `switch`
	- 对一个表达式求值，并将表达式的值与一系列 case 子句进行匹配，一旦遇到与表达式值相匹配的第一个 case 子句后，将执行该子句后面的语句，直到遇到 break 语句为止。若没有 case 子句与表达式的值匹配，如果没有任何 case 子句与表达式的值匹配，则会跳转至 switch 语句的 default 子句执行。
```js
switch (expression) {
  case caseExpression1:
    statements
  case caseExpression2:
    statements
  // …
  case caseExpressionN:
    statements
  default:
    statements
}


const expr = 'Papayas';
switch (expr) {
  case 'Oranges':
    console.log('Oranges are $0.59 a pound.');
    break;
  case 'Mangoes':
  case 'Papayas':
    console.log('Mangoes and papayas are $2.79 a pound.');
    // Expected output: "Mangoes and papayas are $2.79 a pound."
    break;
  default:
    console.log(`Sorry, we are out of ${expr}.`);
}

```

