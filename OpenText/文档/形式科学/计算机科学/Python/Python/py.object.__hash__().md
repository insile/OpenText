##### **`object.__hash__(self)`**
- `__hash__()` 方法是 Python 中的一个特殊方法，用于定义对象的哈希值计算逻辑。哈希值（hash value）是一个整数，用于标识对象在哈希表等数据结构中的位置，从而实现高效的查找和比较操作。
- 您可以通过实现 `__hash__()` 方法来自定义对象的哈希值计算方式。通常情况下，自定义的哈希值应该基于对象的内容，以确保相等的对象具有相等的哈希值。
##### 自定义
```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __hash__(self):
        # 根据对象的内容计算哈希值
        return hash((self.name, self.age))

# 创建两个 Person 实例
person1 = Person(name="Alice", age=25)
person2 = Person(name="Bob", age=30)

# 打印对象的哈希值
print(hash(person1))
print(hash(person2))

```