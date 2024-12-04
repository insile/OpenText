##### 转型表达式
- 转型表达式
	- **转型表达式**是用[[C.强制转换运算符|强制转换运算符]] `()` 将一个表达式的值强制转换为指定类型的[[C.表达式|表达式]], 它通常用来解决类型不兼容问题或进行明确的类型转换
- 示例
```c
#include <stdio.h>
int main() {
    int a = 10, b = 3;
    double result = (double)a / b;  // 转型为 double 类型
    printf("Result: %f\n", result);  // 输出 3.333333
    return 0;
}

```
