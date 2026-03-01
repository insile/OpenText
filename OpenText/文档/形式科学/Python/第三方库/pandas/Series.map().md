##### `Series.map(arg, na_action=None)`
**功能简介:**
- 用于将 Series 中的每个元素映射到另一个值，可以是一个标量、字典、函数或其他映射对象。它可以用来对 Series 的元素进行替换、转换或映射操作，并返回一个新的 Series。

**参数说明:**
- `arg`：用于映射的对象，可以是字典、函数、映射对象或其他可调用对象。字典表示映射关系，函数表示转换操作。
- `na_action`：用于处理缺失值的参数。可选值为 'ignore'（默认）表示忽略缺失值，不进行映射；'raise' 表示遇到缺失值时引发异常。

**返回值:**
- 返回一个新的 Series，其中的元素是通过映射操作转换而来的。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 Series
data = ['apple', 'banana', 'cherry']
series = pd.Series(data)

# 创建一个字典作为映射关系
mapping = {'apple': 'fruit', 'banana': 'fruit', 'cherry': 'berry'}

# 使用 map 方法将元素映射为对应的值
mapped_series = series.map(mapping)

print("Original Series:")
print(series)

print("\nMapped Series:")
print(mapped_series)


s = pd.Series(['cat', 'dog', np.nan, 'rabbit'])
#	0      cat
#	1      dog
#	2      NaN
#	3   rabbit
s.map({'cat': 'kitten', 'dog': 'puppy'})
#	0    kitten
#	1     puppy
#	2       NaN
#	3       NaN
s.map('I am a {}'.format)
#	0       I am a cat
#	1       I am a dog
#	2       I am a nan
#	3    I am a rabbit
```