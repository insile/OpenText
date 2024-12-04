##### continue 语句
- continue 语句
	- 过程控制语句, 用于跳过当前循环体中剩余的语句, 并继续执行下一次循环迭代. 它常用于在循环中遇到特定条件时跳过某些操作
- 语法
```c
continue;
    // 跳过当次循环
```
- 示例
```c
// 在 for 循环中使用 continue
#include <stdio.h>

int main() {
    for (int i = 1; i <= 10; i++) {
        if (i % 2 == 0) {
            continue;  // 跳过偶数
        }
        printf("%d\n", i);
    }

    return 0;
}

```
