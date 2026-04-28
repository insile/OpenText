##### inttypes.h
- inttypes.h (Integer types library)
	- `inttypes.h` 库提供了用于格式化输入输出操作 `printf` 和 `scanf` 的宏, 特别是与定长整数类型 [[C.stdint.h|stdint.h]] 相关的输入输出函数
- 宏
	- `PRId8`
	- `SCNd8`
- 示例
```c
#include <stdio.h>
#include <inttypes.h>

int main() {
    int32_t i = 12345;
    uint32_t u = 67890;

    // 使用inttypes.h宏格式化输出
    printf("int32_t value: %" PRId32 "\n", i);
    printf("uint32_t value: %" PRIu32 "\n", u);

    return 0;
}

```
