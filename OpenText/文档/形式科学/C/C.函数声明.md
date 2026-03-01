##### 函数声明
- 函数声明
	- **函数声明**指[[C.声明|声明]]一个[[C.函数|函数]], 用于向编译器提供函数的函数名称, 参数类型和返回类型. 函数名称使用[[C.声明符|非指针声明符]], 返回类型和参数类型使用[[C.类型说明符|类型说明符]]. 函数声明也称为函数原型, 帮助编译器进行参数和返回值的类型检查. 不同于[[C.函数定义|函数定义]], 函数声明可以出现于块作用域和文件作用域中
- 语法
	- `非指针声明符(形参列表)`
		- 典型的 `S D(params)` 声明函数 `D` 接收参数 `params` 并返回 `S` , `f(void)` 明确表示函数没有参数, `f()` 表示函数参数不受限制
- 示例
```c
#include <stdio.h>

void greet();  // 声明一个没有参数且无返回值的函数
void print_sum(int a, int b);  // 声明一个有两个参数且无返回值的函数
int add(int a, int b);  // 声明一个有两个参数并返回整数的函数
float get_pi();  // 声明一个没有参数但返回浮点数的函数
int multiply(int, int);  // 声明一个省略参数名的函数
int* get_array();  // 声明返回一个指向整数的指针的函数
void print_array(int arr[], int size);  // 声明一个接受整数数组作为参数的函数, arr[] 实际上等价于 int *arr
void modify_array(int *arr, int size);  // 声明接受指向数组的指针的函数
void print_student(struct Student student);  // 声明接受结构体作为参数的函数



```



