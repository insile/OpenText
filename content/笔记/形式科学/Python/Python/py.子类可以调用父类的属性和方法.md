##### 子类可以调用父类的属性和方法
- 子类可以调用父类的属性和方法
	- `父类.方法(实例, 实参)`
	- `super(子类, 实例).方法(实参列表)`
	- `super(子类, 实例).类属性` （没什么用）
	- [[py.super()|super()]]
```python
class Animal:  
    fromc = '英国'  
    def __init__(self, name, age):  
        self.name = name  
        self.age = age  
  
    def speak(self):  
        print(f'我叫{self.name}，来自{self.fromc}，今年{self.age}岁')  
    def run(self):  
        print('我想去中国')  
  
class Dog(Animal):  
    fromc = '中国'  
    def __init__(self, name1, name2, gender, age):  
        super().__init__(name1, age)  # 调用了被覆盖的初始化方法
        print('1:', self.name)  # name在Animal中被第一次初始化
        self.name = name2  
        self.gender = gender  
        print('2:', self.name)  # name在Dog中被覆盖
  
    def speak(self):  
        print(f'我叫{self.name}，来自{self.fromc}，是{self.gender}的')  
  
dog = Dog("大壮", '大可', "公", 21) 
dog.speak()  # 子类方法：我叫大壮，来自中国，是公的  
Animal.speak(dog)  # 父类方法：我叫大可，来自中国，今年21岁  
super(Dog, dog).run()  # 父类方法：我想去中国
print(super(Dog, dog).fromc)  # 父类属性：'英国'  

# 考虑这个狗类，覆盖了动物类的类属性fromc，初始化方法__init__，实例方法speak
# 但是狗类在初始化方法中调用了父类的初始化方法，也获得了一些属性覆盖了一些属性
# 只继承object的普通类，没必要调用object类方法
```