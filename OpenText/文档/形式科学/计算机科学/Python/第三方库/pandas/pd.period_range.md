##### `pd.period_range(start=None, end=None, periods=None, freq=None, name=None)`
**功能简介:**
- 用于生成一个周期范围，返回一个包含指定周期间隔的 PeriodIndex。

**参数说明:**
- `start`：开始周期。
- `end`：结束周期。
- `periods`：生成的周期数量。
- `freq`：周期间隔字符串或 DateOffset 对象，用于定义周期间隔。
- `name`：生成周期索引的名称。

**返回值:**
- 返回一个 PeriodIndex。

**用法示例:**
1. 生成一个周期范围：
```python
import pandas as pd

# 生成一个周期范围，从 2023-01 到 2023-12，每个月为一个周期
period_range = pd.period_range(start='2023-01', end='2023-12', freq='M')

print(period_range)
```
2. 生成一个周期范围，指定周期间隔：
```python
import pandas as pd

# 生成一个周期范围，从 2023-01 到 2023-12，每隔 2 个月
period_range = pd.period_range(start='2023-01', end='2023-12', freq='2M')

print(period_range)
```
