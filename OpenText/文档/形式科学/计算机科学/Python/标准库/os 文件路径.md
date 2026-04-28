##### os 文件路径
```python
os.chdir(path)  # 改变当前工作目录

os.getcwd()  # 返回表示当前工作目录的字符串。Path.cwd()
os.listdir(path='.')  # 目录中文件和子目录。Path.iterdir()
os.remove(path)  # 删除文件。Path.unlink()
os.rmdir(path)  # 删除空目录。Path.rmdir()
os.rename(src, dst)  # 重命名文件或目录路径。Path.rename()

os.mkdir(path, mode=0o777, *, dir_fd=None)  
	# 创建一个新目录。Path.mkdir()
os.makedirs(name, mode=0o777, exist_ok=False)  
	# 递归地创建多级目录。Path.mkdir()
```
##### os.path
```python
os.path.realpath(path)  # 绝对路径 Path.resolve()
os.path.exists(path)  # 存在判断 Path.exists()
os.path.isfile(path)  # 文件判断 Path.is_file()
os.path.isdir(path)  # 目录判断 Path.is_dir()
os.path.join(path, *paths)  # 路径拼接 PurePath.joinpath()
os.path.basename(path)  # 名字 PurePath.name
```