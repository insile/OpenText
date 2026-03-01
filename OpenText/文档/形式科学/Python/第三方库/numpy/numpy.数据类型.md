##### numpy 标量数据类型
```python
# 数字使用位宽约定的别名，以确保数组的大小总是正确
np.int8  # 字节长度的整数
np.int16  # 16位长度的整数
np.int32  # 32位长度的整数
np.int64  # 64位长度的整数
np.uint8  # 无符号字节长度的整数
np.uint16  # 无符号16位长度的整数
np.uint32  # 无符号32位长度的整数
np.uint64  # 无符号64位长度的整数
np.float16  # 半精度，符号1位，指数5位，尾数10位
np.float32  # 半精度，符号1位，指数8位，尾数23位
np.float64  # 半精度，符号1位，指数11位，尾数52位
np.complex64  # 实数和虚数各占32位的复数
np.complex128  # 实数和虚数各占64位的复数
# 其他类型
np.bool_  # 布尔类型，True或False
np.str_  # unicode字符串
np.bytes_  # 字节字符串

# 建议在创建 array 时指定数据类型，且使用统一的数据类型计算。
np.arange(100, dtype=np.float32)
np.arange(100, dtype=np.int32)
np.array(['100'], dtype=np.str_)
```
##### numpy 数据类型
```python
np.dtype(dtype, align=False, copy=False)
# 自定义数据类型和结构化数组(一组结构化的数据)

dt = np.dtype('i4')   
# 32位整数
np.arange(100, dtype=dt)  
# 使用dt类型

student = np.dtype([('name', 'U10'), ('age', 'i'), ('weight', 'f4')]) 
# student结构化数组，名字10个字符，年龄8位整数，体重32位浮点数
s = np.array([('peter',18, 50.5),('lin',18, 50.5)],student)
# 两个元素
```

