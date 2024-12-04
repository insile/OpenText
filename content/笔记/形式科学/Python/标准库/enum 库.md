##### enum 库
- 枚举（Enum）是一种数据类型，用于定义一组**命名的常量值**。枚举可以帮助你在代码中更清晰地表示一组相关的常量，从而增强代码的可读性和可维护性
```python
from enum import Enum,unique,auto
```
##### enum 主要API
```python
# 装饰器 @unique 确保枚举值唯一，如果有重复的枚举值被定义，会报错
# 辅助类 auto() 自动分配递增唯一的整数值给枚举成员

# 下面枚举基类，用于继承
# Enum 类：这是最常见的枚举类，用于创建一个基本的枚举类型，可以包含多个枚举项，每个枚举项都有一个名称和一个关联的值。
class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
print(Color.RED)          # Color.RED
print(Color.GREEN.value)  # 2

# IntEnum 类：与 Enum 类类似，但是它的枚举值是整数类型，用于限制枚举值只能是整数。
class Status(IntEnum):
    SUCCESS = 200
    NOT_FOUND = 404
    SERVER_ERROR = 500
print(Status.SUCCESS)     # Status.SUCCESS
print(Status.NOT_FOUND)   # Status.NOT_FOUND

# Flag 类：用于定义位标志（bit flags）枚举类型，允许枚举值使用按位操作组合成多个标志。每个枚举项的值应该是 2 的幂，以便进行位操作。
@unique
class Permissions(Flag):
    READ = 1
    WRITE = 2
    EXECUTE = 4
print(Permissions.READ)   # Permissions.READ
print(Permissions.WRITE)  # Permissions.WRITE

# IntFlag 类：与 Flag 类类似，但是枚举值是整数类型
@unique
class Flags(IntFlag):
    A = auto()
    B = auto()
    C = auto()
print(Flags.A)            # Flags.A
print(Flags.B.value)      # 2
```