##### Pandas.数据类型
- 对于大多数数据类型，Pandas 使用 NumPy 数组作为包含在 Index、 Series 或 DataFrame 中的具体对象。并且使用 NumPy 的数据类型
- 对于某些数据类型，Pandas 扩展了 NumPy 的类型系统, 包括扩展标量和扩展数组
##### Pandas 数据类型对象
- [[class pd.Timestamp]]  支持时区的日期时间
- [[class pd.Timedelta]]  时间差
- [[class pd.Period]]  一段时间
- [[class pd.Interval]]  区间
- [[class pd.Categorical]] 分类数据对象
##### dtype 参数指定字符串
- 创建 Series 或 DataFrame 时，`dtype` 参数用于指定数据类型
```python
'datetime64[ns, <tz>]'
# 表示带有纳秒精度和可选时区 <tz> 的日期时间数据类型。

'category'
# 表示分类数据类型。分类数据是一种只能取有限、固定数目的值的数据类型。

'period[<freq>]'
# 表示带有指定频率 <freq> 的周期数据类型。

'interval', 'Interval', 'Interval[<numpy_dtype>]', 'Interval[datetime64[ns, <tz>]]', 'Interval[timedelta64[<freq>]]'
# 表示不同形式的区间数据类型，允许包括numpy数据类型、带有时区的datetime64、带有频率的timedelta64等。

'Int8', 'Int16', 'Int32', 'Int64', 'UInt8', 'UInt16', 'UInt32', 'UInt64'
# 表示具有指定位数的整数数据类型。

'Float32', 'Float64'
# 表示具有32位和64位精度的浮点数数据类型。

'string'
# 表示字符串数据类型。

'boolean'
# 表示布尔数据类型。

```