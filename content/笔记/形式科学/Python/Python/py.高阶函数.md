##### 高阶函数
- 高阶函数
	- 高阶函数是一个函数可以接收另一个函数作为参数, 例如 [[py.map()|map()]], [[py.filter()|filter()]], [[py.sorted()|sorted()]]
```python
def add(x, y, f):
	return f(x) + f(y)
```
- 回调函数
	- 回调函数 (Callback Function) 是作为参数传递给其他函数的函数, 用于在特定事件发生时执行自定义的操作. 它通常用于异步编程, 事件处理等情况下. 回调函数可以让程序更加灵活和可扩展, 允许你定义特定的逻辑以响应不同的事件, 钩子函数 (Hook Function) 功能与其相似, 可视为相同
```python
# 假设你正在开发一个数据处理应用，需要对一批数据进行过滤和转换
# 首先定义一个主函数处理标准化数据，并且接受回调函数
# 接着定义一个回调函数，用于对数据标准化，返回标准化数据
# 然后将这个回调函数传递给主函数，让主函数根据需要调用回调函数来处理非标准化数据
# 定义复杂的回调函数，根据规则过滤和转换数据
def data_processing_callback(data, rules):
    processed_data = []
    for item in data:
        if all(rule(item) for rule in rules):
            processed_data.append(item.upper())
    return processed_data

# 主函数，接受数据和回调函数作为参数
def main_function(data, callback):
    filtered_data = callback(data, [lambda x: len(x) > 3, lambda x: x.isalpha()])
    print("Processed Data:", filtered_data)

# 示例数据
data = ["apple", "123", "banana", "orange", "abcde"]

# 调用主函数，传递数据和回调函数
main_function(data, data_processing_callback)
# ['APPLE', 'BANANA', 'ORANGE', 'ABCDE']
```
