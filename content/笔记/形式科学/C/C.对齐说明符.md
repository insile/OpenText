##### 对齐说明符
- 对齐说明符
	- 对齐说明符用于显式指定变量或类型的[[C.对齐|对齐]]方式, 覆盖编译器默认对齐规则
- 语法
	- `_Alignas`
- 示例
```c
// _Alignas(alignment) type; 指定类型对齐
// _Alignas(alignment) variable; 指定变量对齐

#include <stdio.h>

int main() {
    _Alignas(16) int x; // 强制 x 对齐到 16 字节
    printf("Address of x: %p\n", (void*)&x);
    return 0;
}

```

