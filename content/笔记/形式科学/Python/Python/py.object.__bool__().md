##### `object.__bool__(self)`
- `object.__bool__(self)` 方法是 Python 中内置的 `object` 类的特殊方法之一，用于实现对象的布尔转换。`object` 类是所有类的基类，因此其他类都会继承这个方法。在其他类中，您可以覆盖 `__bool__()` 方法来定义自定义的布尔转换行为。
- 默认情况下，`object` 类的 `__bool__()` 方法返回 `True`，即所有对象都被视为真。这在大多数情况下是合理的，因为通常我们希望对象默认情况下是真的。
##### 自定义
```python
class NonEmptyList:
    def __init__(self, data):
        self.data = data

    def __bool__(self):
        return len(self.data) > 0

# 创建一个非空列表对象
non_empty_list = NonEmptyList(data=[1, 2, 3])

# 在条件语句中使用对象的布尔值
if non_empty_list:
    print("The list is not empty.")
else:
    print("The list is empty.")

```