##### math 库
- 该模块提供了对C标准定义的数学函数的访问
- 除非另有明确说明，否则所有返回值均为浮点数
```python
import math
```
##### math 主要API
```python
# 数论与表示函数
math.ceil(x)  # 向上取整
math.floor(x)  # 向下取整
math.fmod(x, y)  # 取余
math.modf(x)  # 返回 x 的小数和整数部分。两个结果都带有 x 的符号并且是浮点数。
math.trunc(x)  # 返回去除小数部分的 x ，只留下整数部分。 
math.fabs(x)  # 绝对值

math.comb(n, k)  # 组合数，返回不重复且无顺序地从 n 项中选择 k 项的方式总数
math.perm(n, k=None)  # 排列数返回不重复且有顺序地从 n 项中选择 k 项的方式总数。

math.frexp(x)  # 以 (m, e) 对的形式返回 x 的尾数和指数
math.ldexp(x, i)  # 返回 x * (2**i) 。 这基本上是函数 frexp() 的反函数。
math.fsum(iterable)  # 返回迭代中的所有元素精确求和
math.prod(iterable, *, start=1)  # 返回迭代中的所有元素精确求积 积的默认 start 值为 1。
math.gcd(*integers)  # 一组整数的最大公约数
math.lcm(*integers)  # 一组整数的最小公倍数
math.isclose(a, b, *, rel_tol=1e-09, abs_tol=0.0)  # 函数用于比较两个浮点数是否接近相等，避免由于浮点数精度问题导致的误差。
math.isfinite(x)  # 如果 x 既不是无穷大也不是NaN，则返回 True ，否则返回 False
math.isinf(x)  # 如果 x 是正或负无穷大，则返回 True ，否则返回 False 。
math.isnan(x)  # 如果 x 是 NaN（不是数字），则返回 True ，否则返回 False 。
math.isqrt(n)  # 返回非负整数 n 的整数平方根。 这就是对 n 的实际平方根向下取整，或者相当于使得 a² ≤ n 的最大整数 a。

# 幂函数与对数函数
math.sqrt(x)  # 返回 x 的平方根。
math.cbrt(x)  # 立方根
math.exp(x)  # 返回 e 的 x 幂
math.exp2(x)  # 返回 2 的 x 幂
math.log(x[, base])  # 使用一个参数，返回 x 的自然对数（底为 e ）。使用两个参数，返回给定的 base 的对数 x ，计算为 log(x)/log(base) 。
math.log2(x)  # 返回 x 以2为底的对数。这通常比 log(x, 2) 更准确。
math.log10(x)  # 返回 x 底为10的对数。这通常比 log(x, 10) 更准确。
math.pow(x, y)  # ** 运算符

# 三角函数
math.degrees(x)  # 将角度 x 从弧度转换为度数。
math.radians(x)  # 将角度 x 从度数转换为弧度。
math.cos(x)  # 返回 x 弧度的余弦值。
math.sin(x)  # 返回 x 弧度的正弦值。
math.tan(x)  # 返回 x 弧度的正切值。
math.acos(x)  # 返回以弧度为单位的 x 的反余弦值。 结果范围在 0 到 pi 之间。
math.asin(x)  # 返回以弧度为单位的 x 的反正弦值。 结果范围在 -pi/2 到 pi/2 之间。
math.atan(x)  # 返回以弧度为单位的 x 的反正切值。 结果范围在 -pi/2 到 pi/2 之间。.
math.atan2(y, x)  # 以弧度为单位返回 atan(y / x) 。结果是在 -pi 和 pi 之间。从原点到点 (x, y) 的平面矢量使该角度与正X轴成正比。 atan2() 的点的两个输入的符号都是已知的，因此它可以计算角度的正确象限。 例如， atan(1) 和 atan2(1, 1) 都是 pi/4 ，但 atan2(-1, -1) 是 -3*pi/4 。
math.dist(p, q)  # 返回 p 与 q 两点之间的欧几里得距离，以一个坐标序列（或可迭代对象）的形式给出。 两个点必须具有相同的维度。
math.hypot(*coordinates)  # 返回欧几里得范数，sqrt(sum(x**2 for x in coordinates))。 这是从原点到坐标给定点的向量长度。

# 双曲函数
math.acosh(x)  # 返回 x 的反双曲余弦值。
math.asinh(x)  # 返回 x 的反双曲正弦值。
math.atanh(x)  # 返回 x 的反双曲正切值。
math.cosh(x)  # 返回 x 的双曲余弦值。
math.sinh(x)  # 返回 x 的双曲正弦值。
math.tanh(x)  # 返回 x 的双曲正切值。

# 常量
math.pi  # 数学常数 π = 3.141592...，精确到可用精度。
math.e  # 数学常数 e = 2.718281...，精确到可用精度。
math.tau  # 数学常数 τ = 6.283185...，精确到可用精度。Tau 是一个圆周常数，等于 2π，圆的周长与半径之比。
math.inf  # 浮点正无穷大。 （对于负无穷大，使用 -math.inf 。）相当于 float('inf') 的输出。
math.nan  # 一个浮点的 "非数字"（NaN）值。相当于 float('nan') 的输出。 由于 IEEE-754标准 的要求， math.nan 和 float('nan') 不被认为等于任何其他数值，包括其本身。要检查一个数字是否为NaN，请使用 isnan() 函数来测试 NaN ，而不是 is 或 == 。 例子:

import math
math.nan == math.nan  # False
float('nan') == float('nan')  # False
math.isnan(math.nan)  # True
math.isnan(float('nan'))  # True
```