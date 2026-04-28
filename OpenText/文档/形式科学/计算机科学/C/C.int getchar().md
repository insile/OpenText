##### int getchar()
- `int getchar( void )`
	- 用于从标准输入流读取一个字符
	- `return` : 成功时返回读取到的字符, 失败返回 `EOF`
- 示例
```c
#include <stdio.h>

int main() {
    int c;

    printf("请输入字符 (Ctrl+D 结束):\n");

    while ((c = getchar()) != EOF) {
        putchar(c); // 输出读取到的字符
    }

    return 0;
}

```
