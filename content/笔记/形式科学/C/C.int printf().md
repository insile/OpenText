##### int printf()
- `int printf(const char *format, ...)`
	- 以特定的格式输出数据到标准输出
	- `format` : 字符串, 包含普通字符和[[C.格式说明符|格式说明符]]
	- `...` : 可变参数, 根据格式说明符的类型指定要输出的变量, 常量或表达式
	- `return` : 返回整数, 表示打印字符的个数, 如果有输出错误, 则返回一个负值
- 示例
```c
#include <stdio.h>  
  
int main() {  
    int num = 10;  
    char str[] = "Hello";  
    int octal_num = 075;  
    int hex_num = 0x1F;  
  
    printf("Integer: %d, String: %s\n", num, str);  
    printf("Octal: %o, Hexadecimal: %X\n", octal_num, hex_num);  
  
    return 0;  
}

// Integer: 10, String: Hello
// Octal: 75, Hexadecimal: 1F
```



