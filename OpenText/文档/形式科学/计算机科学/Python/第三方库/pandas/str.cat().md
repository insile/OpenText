##### Series.str.cat(others=None, sep=None, na_rep=None, join='left')
**功能简介:**
- 用于将一系列字符串连接为一个单一的字符串。它可以在 Series 中的字符串元素之间插入指定的分隔符，并将它们连接成一个字符串。

**参数说明:**
- `others`：要连接的其他字符串或 Series，可以是列表、元组或 Series 对象。
- `sep`：用于连接字符串的分隔符。
- `na_rep`：用于表示缺失值的字符串。
- `join`：指定连接的方式，可选值为 `'left'`（默认）表示从左边开始连接，`'right'` 表示从右边开始连接。

**返回值:**
- 返回一个新的 Series，其中字符串元素已经连接成一个字符串。

**用法示例:**
```python
import pandas as pd

# 自身拼接
s = pd.Series(['a', 'b', np.nan, 'd'])
print(s.str.cat(sep=' '))  # 'a b d'
print(s.str.cat(sep=' ', na_rep='?'))  # 'a b ? d'

# 与其它拼接
print(s.str.cat(['A', 'B', 'C', 'D'], sep=','))  # 对应位置拼接

t = pd.Series(['d', 'a', 'e', 'c'], index=[3, 0, 4, 2])
print(s.str.cat(t, join='left', na_rep='-'))  # 连接拼接
```

