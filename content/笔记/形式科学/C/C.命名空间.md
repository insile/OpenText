##### 命名空间
- 命名空间
	- **命名空间**用于区分不同种类的[[C.标识符|标识符]], C 语言没有显式的命名空间机制, 但它通过不同的标识符类型隐含地使用了多个命名空间, 允许某些标识符在同一[[C.作用域|作用域]]中具有相同的名称, 但不互相冲突
- 语法
	- `标签名称的标识符`
		- [[C.goto 和标记语句|goto 和标记语句]]的标签在独立的命名空间中, 和其他名称不会冲突
	- `结构体, 联合体及枚举类型名称的标识符`
		- 这些类型名称的标识符在独立的命名空间中, 和其他名称不会冲突
	- `结构体或联合体成员的标识符`
		- 这些类型里成员的标识符在独立的命名空间中, 和其他名称不会冲突
	- `通常标识符`
		- 变量名, 函数名, typedef 名, 枚举常量在独立的命名空间中, 和其他名称不会冲突
- 示例
```c
// 标签名称的标识符
void func() {
    int myLabel = 0;
    goto myLabel;
myLabel:  // myLabel 不会冲突
    myLabel = 10;
    printf("%d\n", myLabel);
}

// 结构体, 联合体及枚举类型名称的标识符
struct MyStruct {
    int a;
};
int MyStruct = 10;  // MyStruct 变量名与结构体名不冲突

// 结构体或联合体成员的标识符
struct MyStruct {
    int MyStruct;  // MyStruct 成员名与结构体名不冲突
};

// 通常标识符
int myVar = 10;
void myVar() {  // 错误：函数名不能与变量名相同
}
```
