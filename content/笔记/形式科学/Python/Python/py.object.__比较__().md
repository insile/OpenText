##### **`object.__比较__()`**
- 这些方法是 Python 中用于自定义对象比较操作的特殊方法，它们分别用于定义对象的小于、小于等于、等于、不等于、大于和大于等于比较。这些方法允许您在自定义类中实现自己的比较逻辑，以满足您的特定需求。[[py.表达式|符号与表达式]]
1. `__lt__(self, other)`: 用于实现小于（`<`）比较操作。当您使用 `<` 运算符比较两个对象时，Python 会调用该方法。
2. `__le__(self, other)`: 用于实现小于等于（`<=`）比较操作。当您使用 `<=` 运算符比较两个对象时，Python 会调用该方法。
3. `__eq__(self, other)`: 用于实现等于（`==`）比较操作。当您使用 `==` 运算符比较两个对象时，Python 会调用该方法。
4. `__ne__(self, other)`: 用于实现不等于（`!=`）比较操作。当您使用 `!=` 运算符比较两个对象时，Python 会调用该方法。
5. `__gt__(self, other)`: 用于实现大于（`>`）比较操作。当您使用 `>` 运算符比较两个对象时，Python 会调用该方法。
6. `__ge__(self, other)`: 用于实现大于等于（`>=`）比较操作。当您使用 `>=` 运算符比较两个对象时，Python 会调用该方法。
##### 自定义
```python
class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score

    def __lt__(self, other):
        return self.score < other.score

    def __le__(self, other):
        return self.score <= other.score

    def __eq__(self, other):
        return self.score == other.score

    def __ne__(self, other):
        return self.score != other.score

    def __gt__(self, other):
        return self.score > other.score

    def __ge__(self, other):
        return self.score >= other.score

# 创建两个 Student 实例
student1 = Student(name="Alice", score=85)
student2 = Student(name="Bob", score=92)

# 比较操作
print(student1 < student2)   # 输出：True
print(student1 <= student2)  # 输出：True
print(student1 == student2)  # 输出：False
print(student1 != student2)  # 输出：True
print(student1 > student2)   # 输出：False
print(student1 >= student2)  # 输出：False

```