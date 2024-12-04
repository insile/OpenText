##### do-while 语句
- do-while 语句
	- 循环控制语句, 用于在条件为真时重复执行某段代码. 与[[C.while 语句|while 语句]]不同, do-while 语句先执行循环体, 然后再检查条件表达式
- 语法
```c
do 循环语句 while ( 条件表达式 ) ;
    // 先执行一次循环语句
    // 然后计算条件表达式的值, 如果条件表达式为真(非零), 则继续执行循环体; 如果为假(零), 则退出循环
```
- 示例
```c
// 打印数字 1-10
#include <stdio.h>

int main() {
    int i = 1;

    do {
        printf("%d\n", i);
        i++;
    } while (i <= 10);

    return 0;
}

```