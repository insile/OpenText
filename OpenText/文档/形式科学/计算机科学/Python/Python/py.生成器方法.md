##### 生成器方法
- 生成器方法
```python
generator.send(value)
# 恢复执行并向生成器函数“发送”一个值
# value 参数将成为当前 yield 表达式的结果
# send() 方法会返回生成器所产生的下一个值，或者如果生成器没有产生下一个值就退出则会引发 StopIteration

def my_generator():
    while True:
        x = yield  # x = value
        print(f"Received: {x}")

gen = my_generator()
next(gen)  
# 首次调用生成器的时候需要使用next()方法，执行到第一个yield语句
gen.send("Hello")  
# 发送数据到生成器中，并执行生成器的代码，打印 "Received: Hello"
gen.send(123)  
# 再次发送数据到生成器中，并执行生成器的代码，打印 "Received: 123"
```