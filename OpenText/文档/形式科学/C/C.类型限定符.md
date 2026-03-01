##### 类型限定符
- 类型限定符
	- **类型限定符**用于修饰基本数据类型, 以增加变量的特性和行为
- 语法
	- `const` 
		- 表示变量的值不能被修改, 即只读变量
	- `volatile` 
		- 提示编译器变量可能在程序控制外被改变, 避免优化
	- `restrict` 
		- 用于指针, 表明指针是访问目标数据的唯一方式
	- `_Atomic` 
		- 表示变量是原子类型, 支持多线程安全操作
- 示例
```c
const int max_value = 100;
// max_value = 200; // 错误：不能修改 const 变量


volatile int status_register;
while (status_register == 0) {
    // 编译器不会优化此循环
}

void process_data(int *restrict p1, int *restrict p2);
// 提示指针是唯一访问目标数据的方式

_Atomic int atomic_var = 0;
atomic_var++;
// 提供线程安全的原子操作
```

