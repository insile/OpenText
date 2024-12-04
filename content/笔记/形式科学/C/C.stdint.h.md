##### stdint.h
- stdint.h (Standard integer library)
	- `stdint.h` 库提供了跨平台, 固定宽度的[[C.整数|整数]]类型定义, 方便开发者在不同平台上编写一致的代码, 包括 8, 16, 32, 64 位
- 类型
	- `int8_t` / `int8_t` 固定宽度整数类型
	- `int_fast8_t` / `uint_fast8_t` 最快整数类型
	- `int_least8_t` / `uint_least8_t` 最小整数类型
	- `intmax_t` / `uintmax_t` 最大宽度整数类型
	- `intptr_t` / `uintptr_t` 能够保存指针的整数类型
- 示例
```c
#include <stdio.h>
#include <stdint.h>

int main() {
    // 定义定长整数类型
    int8_t a = -120;
    uint8_t b = 255;
    int16_t c = -32000;
    uint16_t d = 65000;
    int32_t e = -2000000000;
    uint32_t f = 4000000000U;
    int64_t g = -9000000000000000000LL;
    uint64_t h = 18000000000000000000ULL;

    // 使用 printf 打印定长整数类型
    printf("int8_t: %d\n", a);    // 打印有符号8位整数
    printf("uint8_t: %u\n", b);   // 打印无符号8位整数
    printf("int16_t: %d\n", c);   // 打印有符号16位整数
    printf("uint16_t: %u\n", d);  // 打印无符号16位整数
    printf("int32_t: %d\n", e);   // 打印有符号32位整数
    printf("uint32_t: %u\n", f);  // 打印无符号32位整数
    printf("int64_t: %lld\n", g); // 打印有符号64位整数
    printf("uint64_t: %llu\n", h); // 打印无符号64位整数

    // 使用scanf输入定长整数类型
    printf("Enter an int32_t value: ");
    scanf("%" SCNd32, &e);  // 输入有符号32位整数
    printf("You entered: %" PRId32 "\n", e);  // 输出已输入的值

    return 0;
}
```
