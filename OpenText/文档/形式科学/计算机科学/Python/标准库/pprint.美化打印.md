##### pprint.美化打印
```python
from pprint import pprint, PrettyPrinter

data = {
    'name': 'John',
    'age': 30,
    'city': 'New York',
    'skills': ['Python', 'JavaScript', 'SQL'],
    'projects': {
        'project1': 'Web App',
        'project2': 'Data Analysis',
        'project3': 'Machine Learning'
    }
}

# 使用 pprint 高级接口
pprint(data)

# 自定义 PrettyPrinter 实例
custom_printer = PrettyPrinter(indent=2, width=40, depth=2, compact=True, sort_dicts=False)
custom_printer.pprint(data)
```
