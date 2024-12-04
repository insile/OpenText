##### decimal 库
- 用于进行高精度的浮点数运算，避免浮点数运算中的精度丢失问题
```python
import decimal
```
##### decimal 主要API
```python
# 精确四舍五入
from decimal import Decimal, ROUND_HALF_UP
Decimal('11.245').quantize(Decimal('0.00'), 
						   rounding=ROUND_HALF_UP)
# 11.25

# 高精度计算
from decimal import Decimal, getcontext
# 设置全局精度（小数位数）
getcontext().prec = 10
# 创建 Decimal 对象
num1 = Decimal('10.5')
num2 = Decimal('3.2')
# 基本运算
sum_result = num1 + num2
product_result = num1 * num2
division_result = num1 / num2
print("Sum:", sum_result)
print("Product:", product_result)
print("Division:", division_result)
```