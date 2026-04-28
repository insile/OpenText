##### pathlib.具体路径类
- 实例化
```python
class pathlib.Path(*pathsegments)
class pathlib.PosixPath(*pathsegments)
class pathlib.WindowsPath(*pathsegments)
	# 参数pathsegments与纯路径一致
Path.cwd() # 当前工作目录
Path.home() # 用户目录
```
- 实例属性和方法
```python
# 因为继承所以可以使用纯路径类全部实例属性和方法
Path.stat() # 返回一个 os.stat_result 对象，其中包含有关此路径的信息
	Path.stat().st_size # 文件大小（以字节为单位）
	Path.stat().st_mtime # 最近的修改时间，以秒为单位。
	Path.stat().st_ctime # 在 Unix 上表示最近的元数据更改时间，在 Windows 上表示创建时间，以秒为单位。

Path.resolve() # 转绝对路径
Path.rename(target) # 重命名
	# path.rename(path.parent/'rename.txt')

Path.exists() # 是否存在的文件或目录
Path.is_dir() # 目录判断
Path.is_file() # 文件判断

Path.mkdir(mode=511, parents=False, exist_ok=False)
	# 创建单个文件夹，若存在则失败
	# exist_ok=True，若存在则忽略
	# exist_ok=True，parents=True，创建多级文件夹
Path.rmdir() 
	# 移除此目录。此目录必须为空的
Path.unlink(missing_ok=False) 
	# 移除此文件，False路径不存在报错，True忽略
Path.open() # 同open()


Path.iterdir() # 当路径指向一个目录时，产生该路径下的对象的路径，返回生成器
Path.glob(pattern) # 解析相对于此路径的通配符 pattern，产生所有匹配的文件生成器
	# list(path.glob('pattern')) 返回当前目录匹配内容
	# list(path.glob('*\pattern')) 返回子目录匹配内容
	# list(path.glob('**\pattern')) 递归返回目录下所有匹配内容
Path.rglob(pattern)  # 递归匹配, 与 path.glob('**\pattern') 相同

```
