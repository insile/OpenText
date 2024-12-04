---
~
---
##### switch 语句
- switch 语句
	- 条件控制语句, 根据一个表达式的值执行不同的代码块, 可以替代多重 if-else 语句, 使代码更清晰易读
- 语法
```c
// 一般形式
switch (表达式) {
    case 常量表达式1:
        // 当表达式的值等于 常量表达式1 时执行的代码
        break;
    case 常量表达式2:
        // 当表达式的值等于 常量表达式2 时执行的代码
        break;
	case 常量表达式3:
	case 常量表达式4:
		// 当表达式的值等于 常量表达式3或4 时执行的代码
        break;
    // 可以有多个 case 分支
    default:
        // 当表达式的值不等于任何一个常量表达式时执行的代码
}
// 计算 switch 表达式的值
// 将该值与每个 case 标签的值进行比较
// 如果找到匹配的 case, 则从该 case 开始执行代码, 直到遇到 break 语句或 switch 语句的末尾, 意味着多个 case 标签可共享执行代码
// 如果没有找到匹配的 case, 则执行 default 分支的代码（如果有）
```
- 示例
```c
// 星期
#include <stdio.h>

int main() {
    int day = 8;

    switch (day) {
        case 1:
            printf("Monday\n");
            break;
        case 2:
            printf("Tuesday\n");
            break;
        case 3:
            printf("Wednesday\n");
            break;
        case 4:
            printf("Thursday\n");
            break;
        case 5:
            printf("Friday\n");
            break;
        case 6:
            printf("Saturday\n");
            break;
        case 7:
            printf("Sunday\n");
            break;
        default:
            printf("Invalid day\n");
    }

    return 0;
}

```