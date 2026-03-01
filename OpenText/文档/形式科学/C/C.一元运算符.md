##### 一元运算符
- 一元运算符
	- 一元运算符出现在其操作数前, 并按照从右到左的顺序关联
- 语法
```c
++ unary-expression
// 前缀自增
// ++a 存储 a+1 到 a, 返回 a+1

-- unary-expression
// 前缀自减
// --a 存储 a-1 到 a, 返回 a-1

& 
// 取址	
// &a	创建指向对象或函数 a 的指针

* 
// 指针解引用	
// *a	解引用指针 a 以访问其所指向的对象或函数

+ 
// 一元加
// +a	a 提升后的值

- 
// 算术求反
// -a	a 的相反数

~ 
// 按位非
// ~a	a 的按位非

!
// 逻辑非
// !a	a 的逻辑非

sizeof unary-expression
sizeof ( type-name )
// sizeof 运算符
// sizeof a	 a 的字节大小

_Alignof( type-name )
alignof( type-name )
// 类型的对齐要求, 返回size_t类型的整数常量
// alignof是<stdalign.h>中的对齐要求便利宏
```


