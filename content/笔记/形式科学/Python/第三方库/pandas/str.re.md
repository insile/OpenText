##### 正则示例
1. `str.findall(pat, flags=0)`
```python
import pandas as pd

data = {'text': ['apple is red', 'banana is yellow']}
df = pd.DataFrame(data)

# 提取所有匹配项
matches = df['text'].str.findall(r'\w+')
print(matches)
```
2. `str.extract(pat, flags=0, expand=True)`
```python
import pandas as pd

data = {'text': ['apple is red', 'banana is yellow']}
df = pd.DataFrame(data)

# 提取第一个匹配的捕获组
extracted = df['text'].str.extract(r'(\w+) is (\w+)')
print(extracted)
```
3. `str.extractall(pat, flags=0)`
```python
import pandas as pd

data = {'text': ['apple is red, apple is juicy', 'banana is yellow']}
df = pd.DataFrame(data)

# 提取所有匹配的捕获组
extracted_all = df['text'].str.extractall(r'(\w+) is (\w+)')
print(extracted_all)
```
4. `str.replace(pat, repl[, n, case, ...])`
```python
import pandas as pd

data = {'text': ['apple is red', 'banana is yellow']}
df = pd.DataFrame(data)

# 替换匹配项
replaced = df['text'].str.replace(r'\w+', 'fruit')
print(replaced)
```
5. `str.split(pat=None, *, n=-1, expand=False, regex=None)`
```python
import pandas as pd

data = {'text': ['apple is red', 'banana is yellow']}
df = pd.DataFrame(data)

# 按空格分割
splitted = df['text'].str.split(' \w\w ',regex=True)
print(splitted)
```