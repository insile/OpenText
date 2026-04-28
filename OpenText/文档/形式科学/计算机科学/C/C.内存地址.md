##### 内存地址
- 内存地址
	- **内存地址**是[[C.内存|内存]]中[[C.字节|字节]]的位置, 属于[[C.地址空间|地址空间]], 是一个标量类型  (整数, 浮点数, 指针) 的对象或非零长位域的最大连续序列, [[C.指针|指针]]是存储内存地址的变量, 
- 示例
```c
#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main() {
    struct Point p = {10, 20};

    // 输出结构体的地址
    printf("Address of struct p: %p\n", (void*)&p);

    // 输出结构体每个成员的地址
    printf("Address of p.x: %p\n", (void*)&p.x);
    printf("Address of p.y: %p\n", (void*)&p.y);

    return 0;
}

// Address of struct p: 000000d28a7ffc48
// Address of p.x: 000000d28a7ffc48
// Address of p.y: 000000d28a7ffc4c
	
```