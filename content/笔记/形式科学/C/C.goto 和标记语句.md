##### goto 和标记语句
- goto 和标记语句
	- 过程控制语句, 用于无条件地跳转到程序中的另一部分, 与之相关的是标记语句, 它标识跳转的目标位置
- 语法
```c
goto label;
    // 跳转到标记语句
label: 语句
    // 标记后面语句
```
- 示例
```c
// 跳出多重循环
#include <stdio.h>

int main() {
    for (int i = 0; i < 5; i++) {
        for (int j = 0; j < 5; j++) {
            if (i == 3 && j == 3) {
                goto end;  // 跳出所有循环
            }
            printf("i = %d, j = %d\n", i, j);
        }
    }

end:
    printf("Exited the loops.\n");
    return 0;
}

```
