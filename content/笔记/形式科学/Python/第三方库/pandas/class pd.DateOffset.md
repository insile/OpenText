##### class pd.DateOffset
- 日期运算的偏移量
```python
import pandas as pd
# 当前日期
current_date = pd.to_datetime('2023-08-15')
# 增加一天
new_date = current_date + pd.DateOffset(days=1)
print(new_date)
```
- `pd.DateOffset(n,normalize,**kwds)`
```python
import pandas as pd

# 当前日期
current_date = pd.to_datetime('2023-08-15')

print("Business Day:")
print(current_date + pd.DateOffset(weeks=1, days=2))  # 增加 1 周 2 天的工作日

print("\nCustom Business Day:")
print(current_date + pd.DateOffset(weekday=2))  # 增加下一个星期三

print("\nDay:")
print(current_date + pd.DateOffset(days=5))  # 增加 5 天

print("\nWeek:")
print(current_date + pd.DateOffset(weeks=2))  # 增加 2 周
```
##### `freq` 频率别名
```python
'B'：工作日（周一至周五）
'C'：自定义工作日
'D'：每日
'W'：每周
'M'：每月的月底
'SM'：半月（月初和月底）
'BM'：每月的最后一个工作日
'CBM'：自定义月底工作日
'MS'：每月的月初
'SMS'：半月的月初
'BMS'：每月的第一个工作日
'CBMS'：自定义月初工作日
'Q'：季度结束（每季度最后一个月底）
'BQ'：工作日季度结束
'Qs'：季度开始
'BQS'：工作日季度开始
'A' 或 'Y'：每年的年底
'BA' 或 'BY'：工作日年底
```