##### 复合字面量
- 复合字面量
	- **复合字面量**是指在 C 语言中就地构造一个指定类型的无名对象, 在只需要一次[[C.数组|数组]], [[C.结构体|结构体]]或[[C.联合体|联合体]]变量时使用
- 语法
	- `( 存储类说明符 ﻿ 类型 ) { 初始化式列表 }	`
- 示例
```c
// 数组复合字面量
int *arr = (int[]) {1, 2, 3, 4, 5};


struct Point {
    int x;
    int y;
};
 // 结构体复合字面量
struct Point p = (struct Point) {10, 20};


union Data {
    int i;
    float f;
};
// 联合体复合字面量
union Data d1 = (union Data) { .f = 3.14f };

```
