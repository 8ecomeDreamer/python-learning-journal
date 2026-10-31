"""
=========================================================
📚 模块: 14 面向对象高级编程
💡 核心对比：
1. __slots__：在动态语言中用元组限制属性绑定范围（类似 Java 类结构固定），减少内存开销。
2. __getattr__ / __setattr__：用于动态代理与拦截，在框架（如 ORM、FastAPI）底层大量使用。
=========================================================
"""
print("--- 1. 动态属性与 __slots__ ---")
# 任务 1：定义普通类并动态绑定属性，体会实例属性的自由性。
# 任务 2：在类中定义 __slots__ = ('name', 'age')，尝试绑定其他属性（如 score），捕获 AttributeError。
# 任务 3：定义子类继承上述类，不加 __slots__，尝试给子类实例绑定 score，观察限制是否生效。

class NormalPerson:
    __slots__ = ("name", "age")

    def __init__(self, name, age):
        self.name = name
        self.age = age

print("定义普通类并动态绑定属性：")
p1 = NormalPerson("Alice",22)
p1.age = 265
# p1.score = 265

print(f"p1.name: {p1.name}, p1.age: {p1.age}")
# print(f"p1.name: {p1.name}, p1.age: {p1.age}, p1.score: {p1.score}")
# print(f"__slots__能限制类里面的属性添加")

class ChildPerson(NormalPerson):

    __slots__ = ("store", )

    def __init__(self, name, age, store):
        super().__init__(name, age)
        self.store = store

    def init(self, store):
        self.store = store

c1 = ChildPerson("Alice", 22, "Walmart")
print(c1.store)
try:
    c1.store = 100
    print(c1.store)
except AttributeError as e:
    print(f"成功拦截非法属性: {e}")


print("\n--- 2. 魔法方法拦截器 ---")
# 任务 4：实现 __getattr__，当访问不存在的属性（如 obj.xxx）时，动态返回 'default_value'。
# 任务 5：实现 __call__，让实例本身可以像函数一样被调用，如 obj()。

class LukaMagic(NormalPerson):

    def __getattr__(self, name):
        print(f"报告，这个 {name} 属性名未找到！")
        return "default_value"

    def __call__(self, *args, **kwargs):
        print(f"实例当成函数调用，参数有： {args}")
        return "__call__返回值"

luka = LukaMagic("luka Doncic", 27)
print(f"给你介绍luka， 全名是： {luka.name}, 年龄是： {luka.age}")
print(f"他的爱好是 {luka.hobby}")

print(luka(27, **{
    "name": "luka Doncic",
    "age": 27
}))


print("\n--- 3. 使用 @property 管理属性 ---")
# 任务 6：使用 @property 定义只读属性 birth，内部根据当前年份计算年龄。
# 任务 7：为 birth 添加 @birth.setter，实现反向设置 birth 时更新 __age。

class OnlyReadClass(NormalPerson):

    def __init__(self, name, age, birth):
        super().__init__(name, age)
        # 💡 内部变量统一用单下划线开头，表示“这是内部私有的”
        self._birth = birth

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

onlyRead = OnlyReadClass("onlyRead", 27, "2026-10")
print(f"只读类属性：{onlyRead.name}, {onlyRead.age}, {onlyRead.birth}")
onlyRead.birth = "2026-11"
print(f"更改Birth属性：{onlyRead.name}, {onlyRead.age}, {onlyRead.birth}")

# 总结：
# getattr流程： 1.先找实例的__dict__,看有没有对应字段。 2.去继承的类里找 3.以上都没有，找__getattr__ ,当然这个名字是python底层默认写死的。
# __call__:当你给一个类加入了__call__方法，就获得了调用实例如同调用方法的能力。
# *args: 接收多余的位置参数，打包成tuple。对应java的可变参数。
# **kwargs: dict，收集多余的关键字参数，打包成dict（字典），对应java的Map传参。
# 内部变量默认用_xxx代替，否则会触发无限循环。