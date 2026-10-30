"""
=========================================================
📚 模块: 13 面向对象基础
💡 核心对比：
1. self 绑定：Python 实例方法第一个参数必须是 self（显式体现接收者），不像 Java 隐式传入 this。
2. 鸭子类型：Python 多态不依赖接口/继承树，只要对象具有相同的方法即可多态调用。
=========================================================
"""
print("--- 1. 类与实例：过程式 vs 面向对象 ---")
# 场景：从 dict 存储学生数据，升级为封装类
# 任务 1：定义 Student 类，__init__(self, name, score) 初始化实例属性。
# 任务 2：实现 get_grade() 方法（>=90返回A，>=60返回B，否则C）。
# 任务 3：实例化 Bart(59) 和 Lisa(87)，分别打印其等级。

class Student:
    def __init__(self, name, score):
        self.name = name
        self.score = score
    def get_grade(self):
        if self.score >= 90:
            return "A"
        elif self.score >= 60:
            return "B"
        else:
            return "C"
Bart = Student("bart", 59)
Lisa = Student("Lisa", 87)

print(Bart.get_grade())
print(Lisa.get_grade())

print("\n--- 2. 访问限制与私有属性 ---")
# 任务 4：将 Student 的 score 改为私有属性 __score。
# 任务 5：提供 get_score() 和 set_score() 方法。
# 任务 6：尝试外部直接 s.__score 修改，观察是否生效（体会名称改编 Name Mangling）。


class privateStudent:
    def __init__(self, name, score):
        self.__name = name
        self.__score = score
    def get_score(self):
        return self.__score
    def set_score(self, score):
        self.__score = score
Allen = privateStudent("bart", 59)
print(Allen.get_score())
Allen.__score = 90
print("测试是否能修改属性", Allen.get_score())
Allen.set_score(90)
print("通过set方法内部修改", Allen.get_score())


print("\n--- 3. 继承与多态（结合鸭子类型）---")
# 任务 7：定义 Animal 基类，拥有 run() 方法返回字符串。
# 任务 8：定义 Dog 和 Cat 子类，重写 run() 方法。
# 任务 9：定义独立类 Robot（不继承 Animal），也实现 run() 方法。
# 任务 10：写一个 run_twice(animal) 函数，接收任意有 run() 方法的对象并调用两次，体会“鸭子类型”。

class Animal:
    def run(self):
        return "Animal is running"

class Dog(Animal):
    def run(self):
        return "Dog is running"

class Cat(Animal):
    def run(self):
        return "Cat is running"


cat = Cat()
print(cat.run())
dog = Dog()
print(dog.run())