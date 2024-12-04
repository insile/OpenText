##### 面向对象程序设计
- 面向对象程序设计
	- 面向对象程序设计 (Object-Oriented Programming, OOP) 是一种广泛使用的编程范式, 它以现实世界中对象的概念为基础, 将数据和操作封装在一个单一的单位中, 以实现代码的模块化, 可维护性和可重用性. 在面向对象程序设计中, 程序被组织为一系列相互关联的对象, 这些对象可以互相协作来完成任务
	- 面向对象程序设计的核心概念包括封装, 继承, 和多态. 这些概念帮助开发人员创建高效, 可靠且易于维护的代码, 从而更好地应对不断变化的软件需求
- 示例
	- 想象一下一个现实世界的场景, 比如制造一辆汽车
		- 类 (Class)
			- 类是一个模板或蓝图, 定义了对象的属性和行为. 在汽车制造中, 类可以表示汽车的整体设计和规格
		- 对象/实例 (Object/Instance) 
			- 对象是类的一个实例, 具有特定的属性和行为. 在汽车制造中, 对象可以是一辆具体的汽车, 例如一辆特定品牌和型号的车
		- 属性 (Attributes)
			- 属性是对象的特征或数据. 在汽车制造中, 属性可以包括车辆的颜色, 引擎类型, 座位数量等
		- 方法 (Methods)
			- 方法是对象可以执行的操作或行为, 在汽车制造中, 方法可以包括启动引擎, 加速, 制动等操作
	- 在这个例子中, 我们定义了一个名为 `Car` 的类, 它有以下特点
		- 类的初始化方法 `__init__` 用于初始化汽车的属性, 包括制造商, 型号, 年份和颜色
		- `start` 方法用于启动汽车, 但只有当汽车没有运行时才会执行启动操作
		- `stop` 方法用于停止汽车, 但只有当汽车正在运行时才会执行停止操作
		- `honk` 方法用于鸣喇叭, 无论汽车是否在运行
```python
class Car:
    def __init__(self, make, model, year, color):
        self.make = make  # 制造商
        self.model = model  # 车型
        self.year = year  # 年份
        self.color = color  # 颜色
        self.is_running = False  # 运行

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.year} {self.make} {self.model} is now running.")
        else:
            print("The car is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.year} {self.make} {self.model} has been stopped.")
        else:
            print("The car is already stopped.")

    def honk(self):
        print(f"{self.year} {self.make} {self.model} is honking its horn!")

# 创建一个 Car 实例
my_car = Car(make="Toyota", model="Corolla", year=2022, color="Blue")

# 调用方法来操作汽车
my_car.start()  # 启动汽车
my_car.honk()   # 鸣喇叭
my_car.stop()   # 停止汽车

```
