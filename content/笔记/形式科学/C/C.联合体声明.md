##### 联合体声明
- 联合体声明
	- **联合体声明**是使用联合体类型说明符[[C.声明|声明]]一个[[C.联合体|联合体]]及其变量
- 语法
	- `union struct_name {type member};`
- 示例
```c
// 联合体声明
union Data {
    int i;
    float f;
    char c;
};

// 联合体变量声明
union Data d1; // 声明变量 d1
union Data d2; // 声明变量 d2

// 直接在联合体定义后声明变量
union Data {
    int i;
    float f;
    char c;
} d1, d2; // 定义联合体并声明变量 d1 和 d2
```


