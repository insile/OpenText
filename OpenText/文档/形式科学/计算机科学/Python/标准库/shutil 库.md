##### shutil 库
- `shutil` 是 Python 标准库中的一个模块，提供了一些用于文件和目录操作的高级工具。它是 "shell utility"（shutil）的缩写，旨在提供对文件和目录进行复制、移动、删除等常见操作的功能。
- [[shutil.文件操作]]
```python
import shutil
```
##### shutil 主要API
```python
# 文件对象内容复制
shutil.copyfileobj(fsrc, fdst[, length])
	# 将文件对象 fsrc 的内容拷贝到文件对象 fdst

# 路径文件复制
shutil.copy(src, dst, *, follow_symlinks=True)
	# 将路径 src 的文件复制到 dst 路径目录或文件，不包括元数据，替换存在的
shutil.copyfile(src, dst, *, follow_symlinks=True)
	# 将路径 src 的文件复制到 dst 路径文件，不包括元数据，替换存在的
shutil.copy2(src, dst, *, follow_symlinks=True)
	# 同 copy()，尝试保留文件的元数据

# 路径目录复制
shutil.copytree(src, dst, ignore=None, dirs_exist_ok=False)
	# 将路径 src 的目录复制到 dst 路径目录下
	# ignore = shutil.ignore_patterns(p) 忽略文件
	# ignore=ignore_patterns('*.pyc', 'tmp*') 忽略两种文件
	# dirs_exist_ok=False 遇到存在目录文件报错，True不报错
shutil.move(src, dst, copy_function=copy2)
	# 递归将一个文件或目录 src 移至另一位置 dst 并返回目标位置

shutil.rmtree(path, ignore_errors=False, onerror=None)
	# 递归删除目录所有子目录和子文件
```