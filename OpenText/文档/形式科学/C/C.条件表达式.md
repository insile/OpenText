##### 条件表达式
- 条件表达式
	- **条件表达式**是使用[[C.条件表达式运算符|条件表达式运算符]] `?:` 的一种简洁的条件判断表达式
- 示例
```c
#include <stdio.h>

int main() {
    int a = 5, b = 3;
    int max;

    // 使用条件表达式判断 a 和 b 中的最大值
    max = (a > b) ? a : b;

    printf("The maximum value is: %d\n", max);
    return 0;
}

```

