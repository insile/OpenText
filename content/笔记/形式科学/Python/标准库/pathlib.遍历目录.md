##### pathlib.遍历目录
- 使用 `Path` 对象的 `iterdir()` 方法来遍历目录中的文件和子目录
```python
from pathlib import Path

# 创建一个 Path 对象表示目标目录
target_directory = Path("/path/to/directory")

# 遍历目录中的文件和子目录
for entry in target_directory.iterdir():
    if entry.is_dir():
        print(f"目录: {entry}")
    elif entry.is_file():
        print(f"文件: {entry}")

```
- 使用 `Path` 对象的 `glob()` 方法来遍历匹配文件
```python
from pathlib import Path

# 创建一个 Path 对象表示目标目录
target_directory = Path("/path/to/directory")

# 使用 glob() 遍历匹配文件
for txt_file in target_directory.glob('*.txt'):
    print(f"文本文件: {txt_file}")

# 使用 glob() 遍历匹配文件及其子目录中的文件
for txt_file in target_directory.glob('**/*.txt'):
    print(f"文本文件: {txt_file}")
```
- 使用 `Path` 对象的 `iterdir()` 的递归生成器
```python
def print_directory_contents(dir_path):
	# dir_path：目录路径字符串
    from pathlib import Path
    dir_path = Path(dir_path)
    for child in dir_path.iterdir(): # 生产子路径对象
        if child.is_dir(): # 文件夹
            for child2 in yield_directory_contents(child): # 递归生成器
	            yield child2 # 生成
        elif child.is_file(): # 文件
			yield child # 生成
```