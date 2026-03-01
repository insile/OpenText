##### hash()
- `hash( object )`
	- 返回对象哈希值
```python
print(hash(42))  # 输出：42 的哈希值
print(hash("hello"))  # 输出："hello" 的哈希值

my_dict = {'a': 1, 'b': 2}
print(hash('a'))  # 输出：'a' 的哈希值，用作字典的键
print(hash('b'))  # 输出：'b' 的哈希值，用作字典的键

```