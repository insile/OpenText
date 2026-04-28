##### 浮点数计算表达式
- 浮点数计算表达式
	- **浮点数计算表达式**指使用计算相关的[[C.运算符|运算符]]对[[C.浮点数|浮点数]]运算, 包括算数, 关系等, 特别的取余运算符 `%` 不能直接用于浮点数, 也不支持位运算
- 示例
```c
#include <stdio.h>

int main() {
    float a = 5.5f, b = 2.0f, c;

    // 算术运算
    printf("算术运算:\n");
    printf("a + b = %.2f\n", a + b);  // 加法
    printf("a - b = %.2f\n", a - b);  // 减法
    printf("a * b = %.2f\n", a * b);  // 乘法
    printf("a / b = %.2f\n", a / b);  // 除法

    // 关系运算
    printf("\n关系运算:\n");
    printf("a == b: %d\n", a == b);  // 相等
    printf("a != b: %d\n", a != b);  // 不等
    printf("a > b: %d\n", a > b);    // 大于
    printf("a < b: %d\n", a < b);    // 小于
    printf("a >= b: %d\n", a >= b);  // 大于等于
    printf("a <= b: %d\n", a <= b);  // 小于等于

    // 逻辑运算（浮点数会自动转换为布尔值）
    printf("\n逻辑运算:\n");
    printf("a && b: %d\n", a && b);  // 逻辑与
    printf("a || b: %d\n", a || b);  // 逻辑或
    printf("!a: %d\n", !a);          // 逻辑非

    // 自增和自减（浮点数支持自增和自减）
    printf("\n自增和自减:\n");
    printf("a = %.2f\n", a);          // 初始值
    printf("++a = %.2f\n", ++a);      // 前置自增
    printf("a++ = %.2f\n", a++);      // 后置自增
    printf("a = %.2f\n", a);          // 自增后的值
    printf("--a = %.2f\n", --a);      // 前置自减
    printf("a-- = %.2f\n", a--);      // 后置自减
    printf("a = %.2f\n", a);          // 自减后的值

    // 赋值运算
    printf("\n赋值运算:\n");
    c = a;
    printf("c = a: %.2f\n", c);      // 赋值
    c += b;
    printf("c += b: %.2f\n", c);     // 加后赋值
    c -= b;
    printf("c -= b: %.2f\n", c);     // 减后赋值
    c *= b;
    printf("c *= b: %.2f\n", c);     // 乘后赋值
    c /= b;
    printf("c /= b: %.2f\n", c);     // 除后赋值

    // 条件运算
    printf("\n条件运算:\n");
    printf("a > b ? a : b = %.2f\n", a > b ? a : b);  // 条件运算符

    return 0;
}

```