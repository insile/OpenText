##### numpy 通用函数可选关键字参数
- 所有 ufuns 都带有可选的关键字参数。其中大多数代表高级用法，通常不会被使用。
##### **out：**
- 这是一个用于存储计算结果的数组。您可以提供一个现有的数组，以便将计算结果存储在其中，而不是创建一个新的数组
```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
result = np.add(x, y, out=x)  # 将计算结果存储在数组x中
```
##### **where：**
- 这个参数用于指定条件，只有满足条件的元素才会参与计算。可以是一个布尔数组或条件表达式
```python
import numpy as np

x = np.array([1, 2, 3, 4, 5])
y = np.array([5, 4, 3, 2, 1])
condition = x > 2
result = np.add(x, y, where=condition)  # 仅对满足条件的元素进行计算
```
##### **dtype：**
- 这个参数用于指定输出数组的数据类型。默认情况下，NumPy会根据输入数组的数据类型来选择合适的数据类型
```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([4, 5, 6])
result = np.add(x, y, dtype=np.float64)  # 指定输出数据类型为float64
```

##### **casting：**
如果输出数据类型与输入数据类型不兼容，casting参数可以用来指定数据类型转换的行为。可以设置为"no"、"equiv"、"safe"、"same_kind"、"unsafe"等

```python
import numpy as np

x = np.array([1, 2, 3])
y = np.array([0.5, 1.5, 2.5])
result = np.add(x, y, casting="unsafe")  # 允许不安全的数据类型转换
```

##### **order：**
如果输入数组是多维数组，order参数可以用于指定输出数组的内存布局顺序（"C"表示C顺序，"F"表示Fortran顺序）

```python
import numpy as np

x = np.array([[1, 2], [3, 4]])
y = np.array([[5, 6], [7, 8]])
result = np.add(x, y, order="F")  # 指定输出数组的内存布局为Fortran顺序
```
##### **axes：**
- 使用广义 ufunc 应该操作的轴索引的元组列表
##### **axis：**
- 一个广义 ufunc 应该在其上运行的单轴
```python
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
sums_along_axis_0 = np.sum(arr, axis=0)  # 沿着第0个轴计算和
```
##### **keepdims：**
- 一个布尔值，指示是否保持输出数组的维度。如果设置为True，输出数组将保留原始数组的维度，而在相应的轴上插入大小为1的维度
```python
import numpy as np

arr = np.array([[1, 2], [3, 4], [5, 6]])
sums_along_axis_0 = np.sum(arr, axis=0, keepdims=True)  # 保持维度
```
##### **subok：**
- 一个布尔值，指示是否允许子类化。如果设置为True，返回的数组将是输入数组的子类（如果可能的话）
```python
import numpy as np

arr = np.array([1, 2, 3])
result = np.add(arr, 5, subok=True)  # 返回一个子类数组（如果可能）
```

