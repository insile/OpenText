##### io 库
- io 模块提供了 Python 用于处理各种 I/O 类型的主要工具。三种主要的 I/O类型分别为: 文本 I/O, 二进制 I/O 和 原始 I/O
- 独立于其类别，每个具体流对象也将具有各种功能：它可以是只读，只写或读写。它还可以允许任意随机访问（向前或向后寻找任何位置），或仅允许顺序访问（例如在套接字或管道的情况下）
- [[io.认识 io]]
```python
import io
```

##### io 主要API
- [[class io.TextIOWrapper]]  文本文件缓冲读写
- [[class io.BufferedReader]]  二进制文件缓冲读
- [[class io.BufferedWriter]]  二进制文件缓冲写
- [[class io.BytesIO]]  二进制内存流
- [[class io.StringIO]]  文本内存流