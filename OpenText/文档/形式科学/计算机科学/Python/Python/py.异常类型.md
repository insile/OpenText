##### 异常类型
- 异常类型 `<class 'BaseException'>`
	- `BaseException` 是 Python 中所有内置异常类的基类. 它是一个顶层的异常类, 它继承自 [[py.object类|object类]], 所有的异常类都间接或直接地继承自 `BaseException`, 在 Python 中, 异常类的继承关系如下
```python
BaseException
 +-- SystemExit
 +-- KeyboardInterrupt
 +-- GeneratorExit
 +-- Exception
      +-- StopIteration  # 迭代器达末尾
      +-- StopAsyncIteration
      +-- ArithmeticError
      |    +-- FloatingPointError
      |    +-- OverflowError
      |    +-- ZeroDivisionError  # 除零错误
      +-- AssertionError
      +-- AttributeError  # 属性错误
      +-- BufferError
      +-- EOFError
      +-- ImportError  # 导入错误
      |    +-- ModuleNotFoundError
      +-- LookupError
      |    +-- IndexError  # 索引错误
      |    +-- KeyError  # 字典键错误
      +-- MemoryError
      +-- NameError
      |    +-- UnboundLocalError
      +-- OSError
      |    +-- BlockingIOError
      |    +-- ChildProcessError
      |    +-- ConnectionError
      |    |    +-- BrokenPipeError
      |    |    +-- ConnectionAbortedError
      |    |    +-- ConnectionRefusedError
      |    |    +-- ConnectionResetError
      |    +-- FileExistsError
      |    +-- FileNotFoundError  # 文件未找到错误
      |    +-- InterruptedError
      |    +-- IsADirectoryError
      |    +-- NotADirectoryError
      |    +-- PermissionError
      |    +-- ProcessLookupError
      |    +-- TimeoutError
      +-- ReferenceError
      +-- RuntimeError
      |    +-- NotImplementedError
      |    +-- RecursionError
      +-- SyntaxError
      |    +-- IndentationError
      |         +-- TabError
      +-- SystemError
      +-- TypeError  # 类型错误
      +-- ValueError  # 值错误
      |    +-- UnicodeError
      |         +-- UnicodeDecodeError
      |         +-- UnicodeEncodeError
      |         +-- UnicodeTranslateError
      +-- Warning
           +-- DeprecationWarning
           +-- PendingDeprecationWarning
           +-- RuntimeWarning
           +-- SyntaxWarning
           +-- UserWarning
           +-- FutureWarning
           +-- ImportWarning
           +-- UnicodeWarning
           +-- BytesWarning
           +-- EncodingWarning
           +-- ResourceWarning
```