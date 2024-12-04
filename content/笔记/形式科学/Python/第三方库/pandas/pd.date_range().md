##### `pd.date_range(start=None, end=None, periods=None, freq=None, tz=None, normalize=False, name=None, inclusive='both', *, unit=None, **kwargs)`
**功能简介:**
- `pandas.date_range()` 函数用于生成一个日期范围，返回一个包含指定日期间隔的日期时间索引。

**参数说明:**
- `start`：开始日期或时间点。
- `end`：结束日期或时间点。
- `periods`：生成的日期数量。
- `freq`：日期间隔字符串或 DateOffset 对象，用于定义日期间隔。
- `tz`：时区。
- `normalize`：是否将时间戳归一化到午夜。
- `name`：生成日期时间索引的名称。
- `inclusive`：开始和结束日期是否包含在日期范围内，可以是 `'both'`（默认，包含）、`'neither'`、`'left'`、`'right'`。
- `unit`：如果 `freq` 参数不提供，可以使用 `unit` 参数指定间隔单位，例如 `'D'` 表示天。
- `**kwargs`：其他参数，可以用于设置特定频率的额外参数。

**返回值:**
- 返回一个 DatetimeIndex。

**用法示例:**
1. 生成一个日期范围：
```python
import pandas as pd

# 生成一个日期范围，从 2023-08-01 到 2023-08-10
date_range = pd.date_range(start='2023-08-01', end='2023-08-10')

print(date_range)
```
2. 生成一个日期范围，指定日期间隔：
```python
import pandas as pd

# 生成一个日期范围，从 2023-08-01 到 2023-08-10，每隔 2 天
date_range = pd.date_range(start='2023-08-01', end='2023-08-10', freq='2D')

print(date_range)
```
