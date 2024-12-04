##### Index 属性
```python
Index.name  # 返回索引或多索引名称
Index.values  # 返回一个表示索引中数据的数组
Index.is_monotonic_increasing  # 值相等或递增
Index.is_monotonic_decreasing  # 值相等或递减
Index.is_unique  # 唯一值
Index.has_duplicates  # 是否有重复的值
Index.hasnans  # 有任何 NaN
Index.dtype  # 基础数据的 dtype 对象
Index.inferred_type  # 从值推断出的类型的字符串
Index.shape  # 形状
Index.nbytes  # 字节数
Index.ndim  # 维数
Index.size  # 元素数
Index.empty  # 空的
Index.T  # 转置，根据定义就是 self
Index.memory_usage([deep])  # 内存使用情况
```