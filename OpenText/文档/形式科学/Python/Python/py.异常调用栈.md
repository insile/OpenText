##### 异常调用栈
- 异常调用栈
	- 异常调用栈（Exception Call Stack），也称为堆栈跟踪（Stack Trace），是指在程序运行过程中，当发生异常时，记录了函数调用关系的一种数据结构。
	- 它按照函数调用的先后顺序，将每个函数调用的信息（包括函数名、文件名、行号等）记录在栈中，形成一个调用链。当异常发生时，程序会生成一个异常对象，并将异常对象与异常调用栈关联起来，形成一个异常回溯（traceback）信息。
	- 异常调用栈主要用于帮助程序员快速定位程序中的异常发生位置，从而更容易排查和解决问题。在异常回溯信息中，最先打印的是最底层（最后调用的）函数信息，然后依次向上打印每个调用函数的信息，直到达到异常发生的位置。
```python 
$ python3 err.py  # 错误文件
Traceback (most recent call last):  # 回溯信息，表示以下内容是最近的调用堆栈
  File "err.py", line 11, in <module>  # 文件名、行号和出现异常的函数调用信息
    main()
  File "err.py", line 9, in main
    bar('0')
  File "err.py", line 6, in bar
    return foo(s) * 2
  File "err.py", line 3, in foo  # 
    return 10 / int(s)
ZeroDivisionError: division by zero  # 给出了具体的异常类型和错误消息, 除零错误

# 通过这个回溯信息，我们可以逐级追踪函数调用的路径
# 定位到 foo 函数的第 3 行，即 return 10 / int(s) 这一行
# 该行代码导致了 ZeroDivisionError 异常
# 进一步，我们知道这是由于除以零引起的错误
```