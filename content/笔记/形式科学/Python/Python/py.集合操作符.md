##### 集合操作符
- 集合操作符
	- `|` 并集; `&` 交集; `^` 补集; `-` 差集
```python
# 定义两个集合
set1 = {1, 2, 3, 4, 5}
set2 = {3, 4, 5, 6, 7}

# 并集 (|): 包含两个集合中的所有唯一元素
union_set = set1 | set2
print("并集:", union_set)  # 并集: {1, 2, 3, 4, 5, 6, 7}

# 交集 (&): 包含同时在两个集合中的元素
intersection_set = set1 & set2
print("交集:", intersection_set)  # 交集: {3, 4, 5}

# 补集 (^): 包含在两个集合中，但不同时在两个集合中的元素
symmetric_difference_set = set1 ^ set2
print("补集:", symmetric_difference_set)  # 补集: {1, 2, 6, 7}

# 差集 (-): 包含在第一个集合中，但不在第二个集合中的元素
difference_set = set1 - set2
print("差集:", difference_set)  # 差集: {1, 2}
```