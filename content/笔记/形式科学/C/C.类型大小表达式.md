##### 类型大小表达式
- 类型大小表达式
	- **类型大小表达式**指使用[[C.一元运算符|一元运算符]] `sizeof` 返回数据类型在内存中占据的字节数, 它是一个编译时运算符, 因此它的计算是在编译期间完成的, 而不是在程序运行时
- 示例
```c
#include <stdio.h>

struct Example {
    int x;
    float y;
    double z;
};

int main() {
    int a = 10;
    float b = 5.5f;
    double c = 3.14;
    int arr[10];  // 定义一个包含10个整数的数组
    struct Example e;

    printf("Size of int: %zu\n", sizeof(int));       // int类型的大小
    printf("Size of float: %zu\n", sizeof(float));   // float类型的大小
    printf("Size of double: %zu\n", sizeof(double)); // double类型的大小
    printf("Size of char: %zu\n", sizeof(char));     // char类型的大小
    printf("Size of a: %zu\n", sizeof(a));   // 变量 a 的大小
    printf("Size of b: %zu\n", sizeof(b));   // 变量 b 的大小
    printf("Size of c: %zu\n", sizeof(c));   // 变量 c 的大小
    printf("Size of arr: %zu\n", sizeof(arr));       // 整个数组的大小
    printf("Size of struct Example: %zu\n", sizeof(struct Example));  // 结构体大小
    return 0;
}

```
