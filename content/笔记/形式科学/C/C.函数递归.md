##### 函数递归
- 函数递归
	- **函数递归**是在[[C.函数定义|函数定义]]中允许[[函数]]调用它自己
- 示例
```c
#include <stdio.h>

int factorial(int n) {
    if (n <= 1) return 1;
    return n * factorial(n - 1);  // 调用自身
}

int main() {
    printf("Factorial of 5: %d\n", factorial(5));
    return 0;
}

```