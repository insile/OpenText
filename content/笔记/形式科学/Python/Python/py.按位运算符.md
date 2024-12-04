##### 按位运算符
- 按位运算符
	- `&` 按位与; `|` 按位或; `^` 按位异或; `~` 按位取反; `<<` 左移运算; `>>` 右移运算
```python
num1 = 12    # 二进制表示为  1100
num2 = 25    # 二进制表示为 11001

# & 按位与
bitwise_and_result = num1 & num2
print("按位与:", bitwise_and_result)  # 8

# | 按位或
bitwise_or_result = num1 | num2
print("按位或:", bitwise_or_result)  # 29

# ^ 按位异或
bitwise_xor_result = num1 ^ num2
print("按位异或:", bitwise_xor_result)  # 21

# ~ 按位取反
bitwise_not_result = ~num1
print("按位取反:", bitwise_not_result)  # -13

# << 左移运算
left_shift_result = num1 << 2  # 将二进制表示向左移动两位
print("左移运算:", left_shift_result)  # 48

# >> 右移运算
right_shift_result = num2 >> 1  # 将二进制表示向右移动一位
print("右移运算:", right_shift_result)  # 12
 
```