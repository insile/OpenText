##### class datetime.timedelta 时间间隔
- 实例化方法
```python
class datetime.timedelta(days=0, seconds=0, microseconds=0, milliseconds=0, minutes=0, hours=0, weeks=0)
	# 所有参数都是可选的并且默认为 0。 这些参数可以是整数或者浮点数，也可以是正数或者负数。
	# 只有 days, seconds 和 microseconds 会存储在内部，其他时间参数会转换
	# 0 <= microseconds < 1000000
	# 0 <= seconds < 3600*24 (一天的秒数)
	# -999999999 <= days <= 999999999
```
- 类属性
```python
timedelta.min  # timedelta(-999999999).
timedelta.max  # (days=999999999, hours=23, minutes=59, seconds=59, microseconds=999999)
timedelta.resolution  # 最小的间隔 timedelta(microseconds=1)
```
- 实例属性（只读）：
```python
timedelta.days  # -999999999 至 999999999 ，含999999999
timedelta.seconds  # 0 至 86399，包含86399
timedelta.microseconds  # 0 至 999999，包含999999
```
- 方法
```python
t1 = t2 + t3  # t2 和 t3 的和
t1 = t2 - t3  # t2 减 t3 的差
t1 = t2 * i or t1 = i * t2  # 乘以一个整数
t1 = t2 * f or t1 = f * t2  # 乘以一个浮点数，结果会被舍入到 timedelta 最接近的整数倍。 精度使用四舍五偶入奇不入规则
f = t2 / t3  # 总时间 t2 除以间隔单位 t3 (3)。 返回一个 float 对象。
t1 = t2 / f or t1 = t2 / i  # 除以一个浮点数或整数。 结果会被舍入到 timedelta 最接近的整数倍。 精度使用四舍五偶入奇不入规则。
t1 = t2 // i or t1 = t2 // t3  # 计算底数，其余部分（如果有）将被丢弃。在第二种情况下，将返回整数。 
t1 = t2 % t3  # 余数为一个 timedelta 对象
q, r = divmod(t1, t2)  # 通过 : q = t1 // t2 (3) and r = t1 % t2 计算出商和余数。q是一个整数，r是一个 timedelta 对象。
+t1  # 返回一个相同数值的 timedelta 对象。
-t1  # 等价于 timedelta(-t1.days, -t1.seconds, -t1.microseconds), 和 t1* -1
abs(t)  # 当 t.days >= 0``时等于 +\ *t*, 当 ``t.days < 0 时 -t 。 (2)
str(t)  # 返回一个形如 [D day[s], ][H]H:MM:SS[.UUUUUU] 的字符串，当 t 为负数的时候， D 也为负数。 (5)
repr(t)  # 返回一个 timedelta 对象的字符串表示形式，作为附带正规属性值的构造器调用。
```