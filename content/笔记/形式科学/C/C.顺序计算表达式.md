##### 顺序计算表达式
- 顺序计算表达式
	- **顺序计算表达式**指使用[[C.顺序计算运算符|顺序计算运算符]] `,` 计算多个表达式的语法结构. 这些表达式按照从左到右的顺序依次求值, 并返回最后一个表达式的结果
- 示例
```c
#include <stdio.h>

int main() {
    int x = 0, y = 5;

    // 顺序计算表达式
    int z = (x++, y--, x + y);
    printf("x = %d, y = %d, z = %d\n", x, y, z);  // 输出 x = 1, y = 4, z = 5

    // 循环中的顺序计算
    for (int i = 0, j = 5; i < j; i++, j--) {
        printf("i = %d, j = %d\n", i, j);
    }

    // 函数调用中的顺序计算
    int result = (printf("First step\n"), printf("Second step\n"), 42);
    printf("Result = %d\n", result);  // 输出 42

    // 条件语句中的顺序计算
    if (x++, y--, x > y) {
        printf("x is greater than y\n");
    } else {
        printf("x is not greater than y\n");
    }

    return 0;
}


```
