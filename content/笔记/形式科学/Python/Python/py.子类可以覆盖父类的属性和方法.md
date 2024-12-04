##### 子类可以覆盖父类的属性和方法
- 只继承 object 类
```python
class Animal:
    def __init__(self, name):
        self.name = name

# 考虑这个动物类，覆盖了 object 的 __init__ 方法
# 所以 object 的 __new__ 构造的实例在 Animal 中初始化，进行属性赋值
```
- 继承多个父类
```python
class Animal:  
    fromc = '英国'  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
    def speak(self):  
        print(f'我叫{self.name}，来自{self.fromc}，今年{self.age}岁') 
         
class Dog(Animal):  
    fromc = '中国'  
    def __init__(self, name, gender):  
        self.name = name  
        self.gender = gender  
    def speak(self):  
        print(f'我叫{self.name}，来自{self.fromc}，是{self.gender}的')  
        
animal = Animal("大哈", 20)  # 父类实例  
dog = Dog("大壮", "公")  # 子类实例  
animal.speak()  # 我叫大哈，来自英国，今年20岁
dog.speak()  # 我叫大壮，来自中国，是公的

# 考虑这个狗类，覆盖了动物类的所有，包括类属性fromc，初始化方法__init__，实例方法speak
# 所以完全没有体现继承的特性，继承了个寂寞
```