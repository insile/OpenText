##### int putchar()
- `int putchar( int ch )`
	- 向标准输出写入一个字符
	- `return` : 返回整数, 成功返回写入的字符, 失败返回 `EOF`
- 示例
```c
#include <stdio.h>

int main() {
    const char *str = "Hello, World!";
    
    while (*str) {
        putchar(*str); // 输出当前字符
        str++;         // 移动到下一个字符
    }
    putchar('\n'); // 输出换行符

    return 0;
}

```