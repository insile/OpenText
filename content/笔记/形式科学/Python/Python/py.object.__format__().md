##### **`object.__format__(self, format_spec)`**
- 在 Python 中，`__format__()` 方法是一个特殊的内置方法，用于定义对象的自定义格式化字符串。通过实现这个方法，您可以控制如何将对象转换为指定格式的字符串。[[py.format()|format()]]
##### 自定义
```python
class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    def __format__(self, format_spec):
        if format_spec == 'c':
            return f"{self.celsius}°C"
        elif format_spec == 'f':
            fahrenheit = (self.celsius * 9/5) + 32
            return f"{fahrenheit:.2f}°F"
        else:
            return str(self)

# 创建一个 Temperature 实例
temperature = Temperature(celsius=25)

# 使用 format() 函数进行格式化
formatted_celsius = format(temperature, 'c')
formatted_fahrenheit = format(temperature, 'f')

print(formatted_celsius)  # 输出：25°C
print(formatted_fahrenheit)  # 输出：77.00°F

```