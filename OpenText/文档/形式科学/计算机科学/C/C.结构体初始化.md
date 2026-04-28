##### 结构体初始化
- 结构体初始化
	- **结构体初始化**是[[C.声明|声明]]中对[[C.结构体|结构体]]和[[C.联合体|联合体]]的变量的[[C.初始化|初始化]]
- 语法
	- `= {表达式, ...}`
- 示例
```c
struct Point {
    int x;
    int y;
} p = {10, 20}; // 初始化结构体变量 p

struct Point p = {10, 20};  // 初始化结构体变量 p
struct Point p = {.y = 20, .x = 10}; // 明确指定成员名进行初始化，顺序无关


union Data {
    int i;
    float f;
} d = {100}; // 初始化联合体变量 d 的整型成员 i

union Data d = {100};  // 初始化联合体变量 d 的整型成员 i
union Data d = {.f = 3.14f}; // 明确指定成员名进行初始化，顺序无关


struct Inner { int a; float b; };
struct Outer { struct Inner in; int c; };
struct Outer o = {{10, 2.5}, 30};  // 嵌套初始化
```


