##### 成员选择表达式
- 成员选择表达式
	- **成员选择表达式**用于访问[[C.结构体|结构体]]或[[C.联合体|联合体]]中的成员, 根据对象的类型是值类型还是指针类型, 有两种不同的成员选择操作符点运算符 `.` 和箭头运算符 `->` , 都是[[C.后缀运算符|后缀运算符]]
- 示例
```c
#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main() {
    struct Point p = {10, 20};  // 定义一个结构体变量并初始化
    printf("x: %d, y: %d\n", p.x, p.y);  // 直接访问成员
    return 0;
}


#include <stdio.h>

struct Point {
    int x;
    int y;
};

int main() {
    struct Point p = {10, 20};
    struct Point *ptr = &p;  // 定义一个指针指向结构体

    printf("x: %d, y: %d\n", ptr->x, ptr->y);  // 通过指针访问成员
    return 0;
}

```