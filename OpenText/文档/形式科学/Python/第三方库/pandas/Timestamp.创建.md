##### `pd.Timestamp(ts_input=<object object>, year=None, month=None, day=None, hour=None, minute=None, second=None, microsecond=None, tzinfo=None, *, nanosecond=None, tz=None, unit=None, fold=None)`
**功能简介:**
- `pandas.Timestamp` 是用于表示时间戳的类。它表示一个具体的时间点，包括年、月、日、时、分、秒、微秒等信息。

**参数说明:**
- `ts_input`：时间戳输入，可以是各种时间戳表示，如整数、字符串等。
- `year`、`month`、`day`、`hour`、`minute`、`second`、`microsecond`：用于指定时间戳的具体日期和时间部分。
- `tzinfo`：时区对象，标准库 `datetime.timezone`，默认无。
- `nanosecond`：用于指定纳秒部分。
- `tz`：时区字符串，`pytz.timezone`，默认无。`tz='Asia/Shanghai'`
- `unit`：时间单位字符串，如 `'s'` 表示秒，`'ms'` 表示毫秒。
- `fold`：用于处理 DST 时钟回退的折叠参数。

**返回值:**
- 返回一个 `Timestamp` 对象，表示指定的时间戳。

**用法示例:**
```python
import pandas as pd

# 创建一个示例 Timestamp
timestamp = pd.Timestamp(year=2023, month=6, day=2, hour=10, minute=30)

# 输出创建的 Timestamp 对象
print(timestamp)
```
