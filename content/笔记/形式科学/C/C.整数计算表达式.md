##### 整数计算表达式
- 整数计算表达式
	- **整数计算表达式**指使用计算相关的[[C.运算符|运算符]]对[[C.整数|整数]]运算, 包括算数, 逻辑, 按位, 关系等
- 示例
```c
#include <stdio.h>

int main() {
    int a = 5, b = 2, c;
    unsigned int u1 = 7, u2 = 3;
    
    // 算术运算
    printf("算术运算:\n");
    printf("a + b = %d\n", a + b);  // 加法
    printf("a - b = %d\n", a - b);  // 减法
    printf("a * b = %d\n", a * b);  // 乘法
    printf("a / b = %d\n", a / b);  // 整数除法
    printf("a %% b = %d\n", a % b); // 取余
    
    // 关系运算
    printf("\n关系运算:\n");
    printf("a == b: %d\n", a == b);  // 相等
    printf("a != b: %d\n", a != b);  // 不等
    printf("a > b: %d\n", a > b);    // 大于
    printf("a < b: %d\n", a < b);    // 小于
    printf("a >= b: %d\n", a >= b);  // 大于等于
    printf("a <= b: %d\n", a <= b);  // 小于等于

    // 逻辑运算
    printf("\n逻辑运算:\n");
    printf("a && b: %d\n", a && b);  // 逻辑与
    printf("a || b: %d\n", a || b);  // 逻辑或
    printf("!a: %d\n", !a);          // 逻辑非

    // 位运算
    printf("\n位运算:\n");
    printf("a & b: %d\n", a & b);    // 按位与
    printf("a | b: %d\n", a | b);    // 按位或
    printf("a ^ b: %d\n", a ^ b);    // 按位异或
    printf("~a: %d\n", ~a);          // 按位取反
    printf("a << 1: %d\n", a << 1);  // 左移
    printf("a >> 1: %d\n", a >> 1);  // 右移

    // 赋值运算
    printf("\n赋值运算:\n");
    c = a; 
    printf("c = a: %d\n", c);        // 赋值
    c += b; 
    printf("c += b: %d\n", c);       // 加后赋值
    c -= b; 
    printf("c -= b: %d\n", c);       // 减后赋值
    c *= b; 
    printf("c *= b: %d\n", c);       // 乘后赋值
    c /= b; 
    printf("c /= b: %d\n", c);       // 除后赋值
    c %= b; 
    printf("c %%= b: %d\n", c);      // 取余后赋值
    c &= b; 
    printf("c &= b: %d\n", c);       // 按位与后赋值
    c |= b; 
    printf("c |= b: %d\n", c);       // 按位或后赋值
    c ^= b; 
    printf("c ^= b: %d\n", c);       // 按位异或后赋值
    c <<= 1; 
    printf("c <<= 1: %d\n", c);      // 左移后赋值
    c >>= 1; 
    printf("c >>= 1: %d\n", c);      // 右移后赋值

    // 条件运算
    printf("\n条件运算:\n");
    printf("a > b ? a : b = %d\n", a > b ? a : b);  // 条件运算符

    // 类型转换
    printf("\n类型转换:\n");
    double d = (double)a / b; 
    printf("(double)a / b = %f\n", d);

    // unsigned 和 signed 比较
    printf("\n无符号和有符号比较:\n");
    printf("u1 > b: %d\n", u1 > b);     // 无符号与有符号比较
    printf("u1 - u2 = %u\n", u1 - u2); // 无符号减法

    return 0;
}
```