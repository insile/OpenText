##### 结构体声明
- 结构体声明
	- **结构体声明**是使用结构体类型说明符[[C.声明|声明]]一个[[C.结构体|结构体]]及其变量
- 语法
	- `struct struct_name {type member};`
- 示例
```c
// 结构体声明
struct Point {
    int x;
    int y;
};

// 结构体变量声明
struct Point p1; // 声明变量 p1
struct Point p2; // 声明变量 p2

// 直接在结构体定义后声明变量
struct Point {
    int x;
    int y;
} p1, p2; // 定义结构体并声明变量 p1 和 p2
```


