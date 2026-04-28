##### Null 语句
- Null 语句
	- 空语句是仅包含分号的语句, 它可在需要语句时显示, 执行空语句时不会发生任何事件, 通常用于占位, 空循环体, 空条件分支
- 语法
```
;
// 无实质性语句体
```
- 示例
```c
// 空条件分支
#include <stdio.h>

int main() {
    int condition = 0;

    if (condition) {
        ; // 什么也不做
    } else {
        printf("Condition is false.\n");
    }

    return 0;
}
```
