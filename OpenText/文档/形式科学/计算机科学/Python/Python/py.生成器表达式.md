##### 生成器表达式 
- 生成器表达式
	- 生成器表达式是用圆括号 `( )` 括起来的紧凑形式生成器
```python
# 表达式接for循环
a = (x for x in range(1,10))
# <generator object <genexpr> at 0x7faf6ee20a50>`

# 表达式接for循环，接if判断
b = (x for x in range(1,10) if x % 2 == 0)
tuple(b)
# (2, 4, 6, 8)
```
##### 列表生成式
- `[ ]`
```python
# 表达式接for循环
[x*x for x in range(1, 11)]
# [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# 表达式接for循环，接if判断
[x*x for x in range(1, 11) if x%2 = 0]
# [4, 16, 36, 64, 100]

# 可两层循环
[m+n for m in 'ABC' for n in 'XYZ']
# ['AX', 'AY', 'AZ', 'BX', 'BY', 'BZ', 'CX', 'CY', 'CZ']

# 嵌套生成式
[[i+j for i in range(3)] for j in range(4)]
# [[0, 1, 2], [1, 2, 3], [2, 3, 4], [3, 4, 5]]
```
##### 集合生成式 
- `{ }`
```python
# 表达式接for循环
{i**2 for i in (1,2,3)}
# {1, 4, 9}

# 表达式接for循环，接if判断
{x for x in 'abracadabra' if x not in 'abc'}
# {'d', 'r'}
```
##### 字典生成式 
- `{:}`
```python
 # x为键接x的表达式接for循环
{x: x**2 for x in (2, 4, 6)}
# {2: 4, 4: 16, 6: 36}

# x为键接x的表达式接for循环，接if判断
{x: x**2 for x in (2, 3, 4, 5, 6) if x % 2 == 0}
# {2: 4, 4: 16, 6: 36}

{word: len(word) for word in ['apple','banana','peach','pineapple','watermelon']}
# {'apple': 5, 'banana': 6, 'peach': 5, 'pineapple': 9, 'watermelon': 10}

```

