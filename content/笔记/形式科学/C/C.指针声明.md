##### 指针声明
- 指针声明
	- **指针声明**指[[C.声明|声明]]一个[[C.指针|指针]], 用于向编译器提供指针的指针名称和指针将指向的数据类型, 指针名称使用[[C.声明符|声明符]], 指针指向的数据类型使用[[C.类型说明符|类型说明符]]
- 语法
	- `*声明符`
		- 声明符是指针名称
- 示例
```c
int *ptr;  // ptr 是一个指向 int 类型的指针
int *p1, *p2, *p3; // p1, p2, p3 都是指针
int **pptr; // 声明一个指针，指向另一个指向 int 类型的指针

int *arr[5]; // 声明一个数组，其中每个元素是一个指向 int 类型的指针
int (*arr_ptr)[5]; // 声明一个指针，指向一个包含 5 个整数的数组

int* get_array();  // 声明返回一个指向整数的指针的函数
void (*func_ptr)();  // 声明了一个指向返回类型为 void 且无参数的函数的指针

```



