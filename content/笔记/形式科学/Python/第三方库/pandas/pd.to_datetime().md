##### `pd.to_datetime(arg, errors='raise', dayfirst=False, yearfirst=False, utc=False, format=None, exact=_NoDefault.no_default, unit=None, infer_datetime_format=_NoDefault.no_default, origin='unix', cache=True)`
**功能简介:**
- 用于将输入的日期时间数据转换为 pandas 的 Timestamp 对象。它可以处理多种日期时间格式，并可用于数据清洗和处理。

**参数说明:**
- `arg`：要转换为日期时间的输入，可以是字符串、列表、Series、数组、DataFrame 等。
- `errors`：在遇到错误时的处理方式，可以是 `'raise'`（默认，抛出异常）、`'coerce'`（将无效日期设置为 NaT）和 `ignore`（忽略错误）。
- `dayfirst`：是否将日期中的日放在前面。
- `yearfirst`：是否将日期中的年放在前面。
- `utc`：是否将结果转换为 UTC 时间。
- `format`：自定义的日期时间格式字符串。
- `unit`：指定输入数据的时间单位，可以是 `'D'`（天）、`'s'`（秒）等。
- `origin`：用于处理整数时间戳的起始时间，可以是 `'unix'`（默认，1970-01-01）或其他日期。
- `cache`：是否启用日期格式缓存。

**返回值:**
- 返回一个包含转换后日期时间的 pandas Series 或 DatetimeIndex。

**用法示例:**
1. 转换字符串为 Timestamp 对象：
```python
import pandas as pd

# 转换单个字符串为 Timestamp
date_str = '2023-08-22'
timestamp = pd.to_datetime(date_str)

print(timestamp)
```
2. 转换列表为 DatetimeIndex：
```python
import pandas as pd

# 转换列表为 DatetimeIndex
date_list = ['2023-08-20', '2023-08-21', '2023-08-22']
datetime_index = pd.to_datetime(date_list)

print(datetime_index)
```