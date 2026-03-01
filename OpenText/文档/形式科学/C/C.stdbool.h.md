##### stdbool.h
- stdbool.h (Standard bool library)
	- `stdbool.h` 库提供了布尔类型支持
- 宏
	- `typedef _Bool bool;`
		- `bool` 是 `_Bool` 类型的别名
	- `#define true  1`
		- `true` 是布尔值 `1` 的宏定义。
	- `#define false 0`
		- `false` 是布尔值 `0` 的宏定义。
	- `#define __bool_true_false_are_defined 1`
		- 标识当前环境中 `bool`, `true` 和 `false` 已被定义
- 示例
```c
#include <stdio.h>
#include <stdbool.h>
 
int main(void)
{
    _Bool c=1, d=0;
    bool a=true, b=false; // stdbool.h
    printf("%d\n", a&&b);
    printf("%d\n", a||b);
    printf("%d\n", !b);
}
```

