##### return 语句
- return 语句
	- 过程控制语句, 用于终止函数的执行, 并将控制权返回给调用函数, 还可以返回一个值给调用函数
- 语法
```c
return;
    // 不带返回值的 return 语句
return 表达式; 
    // 带返回值的 return 语句
```
- 示例
```c
#include <stdio.h>

int add(int a, int b) {
    return a + b;  // 返回两个整数的和
}

int main() {
    int sum = add(5, 3);
    printf("Sum: %d\n", sum);
    return 0;
}

```
