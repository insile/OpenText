##### abc.产品抽象基类设计
```python
from abc import ABC, abstractmethod

# 继承抽象基类ABC来定义抽象基类Product
class Product(ABC):
    def __init__(self, name, price):  # 通用属性
        self.name = name
        self.price = price
        
    @abstractmethod  # 抽象方法 用于计算产品的价格
    def calculate_price(self):
        pass

# 定义子类 Book
class Book(Product):
    def __init__(self, name, price, pages):
        super().__init__(name, price)
        self.pages = pages
        
    def calculate_price(self):  # 实现基类中定义的抽象方法
        return self.price
        
# 定义子类 Electronic
class Electronic(Product):
    def __init__(self, name, price, warranty_years):
        super().__init__(name, price)
        self.warranty_years = warranty_years
        
    def calculate_price(self):  # 实现基类中定义的抽象方法
        return self.price * (1 - self.warranty_years * 0.1)


# 子类实例化
book = Book("Python Programming", 50.0, 400)
electronic = Electronic("Smartphone", 600.0, 2)

# 多个子类之间实现多态性
def print_product_info(product):
    print(f"Product: {product.name}")
    print(f"Price: ${product.calculate_price():.2f}")

print("Book:")
print_product_info(book)

print("\nElectronic:")
print_product_info(electronic)

# 继承顺序
Book.__mro__  # (__main__.Book, __main__.Product, abc.ABC, object)
```

