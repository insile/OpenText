##### if 语句
- if 语句
	- 条件控制语句, 根据条件表达式的真假来决定是否执行某段代码
- 语法
```c
if (条件表达式) 条件语句
    // 当条件表达式为真时执行条件语句

if (条件表达式) 条件语句1 else 条件语句2
    // 当条件表达式为真时执行条件语句1
    // 当条件表达式为假时执行条件语句2
```
- 示例
```c
// 判断数字为正数
#include <stdio.h>

int main() {
    int num = 10;

    if (num > 0) {
        printf("The number is positive.\n");
    }

    return 0;
}

// 嵌套 if 语句
#include <stdio.h>

int main() {
    int num = 15;

    if (num > 0) {
        if (num % 2 == 0) {
            printf("The number is positive and even.\n");
        } else {
            printf("The number is positive and odd.\n");
        }
    } else {
        printf("The number is not positive.\n");
    }

    return 0;
}

```

