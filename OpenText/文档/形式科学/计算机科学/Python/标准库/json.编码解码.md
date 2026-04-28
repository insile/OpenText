##### json.编码解码
```python
import json

# 定义一个 Python 字典
data = {
    "name": "Alice",
    "age": 30,
    "is_student": False,
    "grades": [85, 90, 78]
}

# 将 Python 字典转换为 JSON 格式字符串
json_data = json.dumps(data, indent=4)  # 使用缩进增强可读性
print("JSON data:")
print(json_data)

# 将 JSON 格式字符串解析为 Python 数据
parsed_data = json.loads(json_data)
print("\nParsed data:")
print(parsed_data)

```
