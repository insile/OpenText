##### 指针
- 指针
	- **指针**是一个变量, 它存储另一个变量的[[C.内存地址|内存地址]], 指针可以指向变量, 数组, 函数甚至其他指针. 通过指针可以直接访问和修改该地址上的数据, 用[[C.空指针|空指针]]表示无效地址
- 语法
	- [[C.指针声明|指针声明]]
	- [[C.标量初始化|标量初始化]]
	- [[C.指针操作表达式|指针操作表达式]]
- 示例
```c
#include <stdio.h>

// 定义一个结构体
struct MyStruct {
    int a;
    double b;
    char c;
};

// 定义一个联合体
union MyUnion {
    int x;
    double y;
    char z;
};

// 定义一个枚举
enum MyEnum {
    VALUE_ONE,
    VALUE_TWO,
    VALUE_THREE
};

// 定义一个函数
void myFunction() {
    printf("This is a function.\n");
}

int main() {
    // 基本类型
    int integer = 42;
    float floating = 3.14f;
    double double_floating = 2.71828;
    char character = 'A';

    // 派生类型
    int array[5] = {1, 2, 3, 4, 5};
    int *pointer = &integer;

    // 结构体、联合体和枚举
    struct MyStruct my_struct = {1, 3.14, 'C'};
    union MyUnion my_union = {.x = 42};
    enum MyEnum my_enum = VALUE_TWO;

    // 获取函数指针
    void (*func_ptr)() = myFunction;

    // 输出各类型的内存大小和地址
    printf("Integer: size = %zu bytes, address = %p\n", sizeof(integer), (void *)&integer);
    printf("Float: size = %zu bytes, address = %p\n", sizeof(floating), (void *)&floating);
    printf("Double: size = %zu bytes, address = %p\n", sizeof(double_floating), (void *)&double_floating);
    printf("Char: size = %zu bytes, address = %p\n", sizeof(character), (void *)&character);

    printf("Array: size = %zu bytes, address = %p\n", sizeof(array), (void *)array);
    printf("Pointer: size = %zu bytes, address = %p, points to = %p\n", sizeof(pointer), (void *)&pointer, (void *)pointer);

    printf("Struct: size = %zu bytes, address = %p\n", sizeof(my_struct), (void *)&my_struct);
    printf("Union: size = %zu bytes, address = %p\n", sizeof(my_union), (void *)&my_union);
    printf("Enum: size = %zu bytes, address = %p, value = %d\n", sizeof(my_enum), (void *)&my_enum, my_enum);

    printf("Function: address = %p\n", (void *)func_ptr);

    return 0;
}

```


