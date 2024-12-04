##### 解释器
- 解释器
	- Python 解释器是执行 Python 代码的程序, 它读取并执行 Python 源代码或已编译的字节码. Python 解释器有多种实现, 其中最常用的是 CPython, 它是官方的 Python 解释器. 使用 C 语言编写
	- 全局解释器锁 (Global Interpreter Lock, GIL) 是 CPython 解释器中的一个机制，用于确保在多线程环境中只有一个线程执行 Python 字节码, 这样可以防止多线程环境中出现的数据竞争和内存管理问题, 但是这个锁对于 CPython 解释器的多线程性能产生了一些影响


