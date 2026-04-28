##### `pd.to_timedelta(arg, unit=None, errors='raise')`
**功能简介:**
- 用于将输入的时间差数据转换为 pandas 的 Timedelta 对象。它可以用于处理时间差数据，例如时间间隔、持续时间等。

**参数说明:**
- `arg`：要转换为时间差的输入，可以是字符串、列表、Series、数组、DataFrame 等。
- `unit`：时间差的单位，可以是 `'D'`（天）、`'s'`（秒）等。如果未指定，函数将尝试根据输入自动推断单位。
- `errors`：在遇到错误时的处理方式，可以是 `'raise'`（默认，抛出异常）和 `ignore`（忽略错误）。

**返回值:**
- 返回一个包含转换后时间差的 pandas Series。

**用法示例:**
1. 转换字符串为 Timedelta 对象：
```python
import pandas as pd

# 转换单个字符串为 Timedelta
duration_str = '2 days 3 hours 30 minutes'
timedelta = pd.to_timedelta(duration_str)

print(timedelta)
```
2. 转换列表为 TimedeltaIndex：
```python
import pandas as pd

# 转换列表为 Timedelta
duration_list = ['1 days', '3 days 12 hours', '6 hours']
timedeltas = pd.to_timedelta(duration_list)

print(timedeltas)
```
