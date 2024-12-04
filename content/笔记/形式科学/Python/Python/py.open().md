##### open()
- `open(file, mode='r', buffering=- 1, encoding=None, errors=None, newline=None, closefd=True, opener=None)`
	- 打开文件, 创建一个[[py.文件对象|文件对象]], 文本返回[[class io.TextIOWrapper]], 二进制读返回[[class io.BufferedReader]], 二进制写返回[[class io.BufferedWriter]]
	- `file` 文件路径；`mode` 读取模式；`encoding` 编码；`errors` 编码错误的处理方式；
```python
# 文件路径: 绝对路径，相对路径，pathlib路径对象
# 打开模式：'r' 只读；'w' 覆盖写；'x' 创建写；'a' 追加写；'b' 二进制；'t' 文本；'+' 同时读写

# 打开文件并读取内容
file_path = 'example.txt'
with open(file_path, 'r') as file:
    content = file.read()
    print(content)

# 打开文件并写入内容
with open('output.txt', 'w') as file:
    file.write('Hello, world!')

# 打开文件并按行读取内容
with open('example.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        print(line.strip())

```