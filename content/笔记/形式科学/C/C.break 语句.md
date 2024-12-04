##### break 语句
- break 语句
	- 过程控制语句, 用于立即终止所在的 switch 语句或循环, 并将控制转移到循环或 switch 语句之后的第一条语句
- 语法
```c
break;
    // 提前退出当前语句
```
- 示例
```c
// 在 for 循环中使用 break
#include <stdio.h>

int main() {
    for (int i = 1; i <= 10; i++) {
        if (i == 5) {
            break;  // 当 i 等于 5 时，退出循环
        }
        printf("%d\n", i);
    }

    printf("Loop terminated\n");

    return 0;
}

```
