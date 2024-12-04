##### 枚举声明
- 枚举声明
	- **枚举声明**是使用枚举类型说明符[[C.声明|声明]]一个[[C.枚举|枚举]]及其变量, 每个枚举声明都是定义
- 语法
	- `enum enum_name {const};`
- 示例
```c
// 一般形式
enum EnumName {
    Const1 = value1,  // 可选赋值，默认为 0
    Const2,           // 默认为上一个常量值加 1
    Const3 = value3
};

// 枚举声明
enum Color {
    RED = 1,   // 指定 RED 为 1
    GREEN,     // GREEN 自动为 2
    BLUE = 5   // BLUE 指定为 5
};

// 枚举变量声明初始化
enum Color c = GREEN;  // c 被初始化为 2

// 枚举变量声明
enum Color {
    RED = 1,   // 指定 RED 为 1
    GREEN,     // GREEN 自动为 2
    BLUE = 5   // BLUE 指定为 5
} c = GREEN;
```

