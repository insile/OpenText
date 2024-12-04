##### int scanf()
- `int scanf(const char *format, ...)`
	- 以特定的格式从标准输入获取数据
	- `format` : 字符串, 包含普通字符和[[C.格式说明符|格式说明符]]
	- `...` : 可变参数, 根据格式说明符的类型指定要输出的变量, 常量或表达式
	- `return` : 返回整数, 成功时返回成功读取并赋值的变量数量, 输入到文件结尾时返回 `EOF`, 如果没有匹配任何输入, 返回 0
- 示例
```c
#include <stdio.h>
int main() {
    int day, month, year;
    printf("请输入日期 (格式: YYYY-MM-DD): ");
    scanf("%d-%d-%d", &year, &month, &day);
    printf("年: %d, 月: %d, 日: %d\n", year, month, day);
    return 0;
}

```



