##### 整数
- 整数
	- **整数**是没有小数部分的数字, 基本类型指 `int` , 另外字符类型 `char` 也是是整数类型, 因为实际上储存的是整数而不是字符, 计算机使用数字编码来处理字符, 即用特定的整数表示特定的字符, 主要是ASCII码. 布尔类型也是整数. [[C.stdint.h|stdint.h]] 提供了固定大小的整数类型
- 语法
	- [[C.整数字面量|整数字面量]]
	- [[C.整数声明|整数声明]]
	- [[C.标量初始化|标量初始化]]
	- [[C.整数计算表达式|整数计算表达式]]

| [[C.类型说明符\|类型说明符]]                                                     | [[C.格式说明符\|格式说明符]]     | 描述          | 最小大小(位) | [[C.字面量\|字面量]]                                                                  |
| ---------------------------------------------------------------------- | ---------------------- | ----------- | ------- | ------------------------------------------------------------------------------- |
| int<br>signed<br>signed int                                            | `%d` `%i`<br>`%o` `%u` | 有符号整型<br>   | 16      | 十进制 `[十进制数字]`<br>二进制 `0b/0B[二进制数字]` <br>八进制 `0[八进制数字]` <br>十六进制 `0x/0X[十六进制数字]` |
| short<br>short int<br>signed short<br>signed short int                 | `%hd` `%hi`            | 有符号短整型<br>  | 16      |                                                                                 |
| long<br>long int<br>signed long<br>signed long int                     | `%ld` `%li`            | 有符号长整型<br>  | 32      | 后缀 `L`                                                                          |
| long long<br>long long int<br>signed long long<br>signed long long int | `%lld` `%lli`          | 有符号长长整型<br> | 64      | 后缀 `LL`                                                                         |
| unsigned<br>unsigned int                                               | `%u`                   | 无符号整型<br>   | 16      | 后缀 `U`                                                                          |
| unsigned short<br>unsigned short int                                   | `%hu`                  | 无符号短整型<br>  | 16      |                                                                                 |
| unsigned long<br>unsigned long int                                     | `%lu`                  | 无符号长整型<br>  | 32      | 后缀 `LU`                                                                         |
| unsigned long long<br>unsigned long long int                           | `%llu`                 | 无符号长长整型     | 64      | 后缀 `LUU`                                                                        |
| char                                                                   | `%c`                   | 字符          | 8       | 字符单引号 `'[ASCII字符]'`<br>字符[[C.转义序列\|转义序列]] `'\'`                                 |
| signed char                                                            | `%c`                   | 有符号字符       | 8       |                                                                                 |
| unsigned char                                                          | `%c`                   | 无符号字符       | 8       |                                                                                 |
| _Bool                                                                  |                        | 布尔类型        | 8       |                                                                                 |
- 示例
```c
#include <stdio.h>
int main()
{
    long long a = 1000000;
    printf("%lld\n", a);
    printf("%lld\n", 1000000LL);
    printf("%d\n", 0b10);
    printf("%d\n", 010);
    printf("%o\n", 010);
    printf("%d\n", 0x10);
    printf("%u\n", 0x10);
    printf("%c\n", 'a');
    printf("%d\n", 'a');
}
```


