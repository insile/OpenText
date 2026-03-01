##### 指针操作表达式
- 指针操作表达式
	- **指针操作表达式**主要涉及两个[[C.一元运算符|一元运算符]]分别是[[C.指针|指针]]的取地址运算符 `&` 和解引用运算符 `*` . 其中, `&` 用来获取一个变量的地址, 而 `*` 用来访问指针指向的地址处存储的值. 初次之外还支持多种运算包括算术, 关系, 逻辑等用于元素访问, 例如算数运算表示将指针偏移指定的元素数量
- 示例
```c
#include <stdio.h>  
  
int main() {  
    int arr[5] = {1, 2, 3, 4, 5};  // 一个整型数组  
    int *p = arr;                  // 指针 p 指向数组 arr 的第一个元素  
  
    // 指针算术运算  
    printf("p points to: %d\n", *p);  // 输出 p 指向的值 (1)    
    p++;  // 指针加一，指向数组中的下一个元素  
    printf("After p++, p points to: %d\n", *p);  // 输出 p 指向的值 (2)    
    p--;  // 指针减一，指向数组中的上一个元素  
    printf("After p--, p points to: %d\n", *p);  // 输出 p 指向的值 (1)    int *q = &arr[4];  // 指针 q 指向数组的最后一个元素  
    printf("q points to: %d\n", *q);  // 输出 q 指向的值 (5)  
    
    // 指针差值运算  
    printf("Difference between p and q: %lld\n", q - p);  // 输出指针差值，即 q 和 p 之间的元素个数 (4)  
    
    // 指针关系运算  
    if (p < q) {  
        printf("p is less than q\n");  // 判断 p 是否在 q 之前  
    }  
    if (q > p) {  
        printf("q is greater than p\n");  // 判断 q 是否在 p 之后  
    }  
  
    // 指针和整数的运算  
    p = p + 2;  // 指针加上整数，指向数组中的第3个元素  
    printf("After p + 2, p points to: %d\n", *p);  // 输出 p 指向的值 (3)
    p = p - 1;  // 指针减去整数，指向数组中的第2个元素  
    printf("After p - 1, p points to: %d\n", *p);  // 输出 p 指向的值 (2)  
    
    // 指针与常量的运算  
    p = arr + 3;  // 将指针 p 指向数组的第4个元素  
    printf("p points to: %d\n", *p);  // 输出 p 指向的值 (4)  
    return 0;  
}
```
