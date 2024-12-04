##### shutil.文件操作
```python
import shutil

# 复制文件
source_file = 'source.txt'
destination_file = 'destination.txt'

shutil.copy(source_file, destination_file)
print(f'File "{source_file}" copied to "{destination_file}"')

# 复制目录及其内容
source_dir = 'source_folder'
destination_dir = 'destination_folder'

shutil.copytree(source_dir, destination_dir)
print(f'Directory "{source_dir}" copied to "{destination_dir}"')

# 删除目录及其内容
shutil.rmtree(destination_dir)
print(f'Directory "{destination_dir}" removed')

```