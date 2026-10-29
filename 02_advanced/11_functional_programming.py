"""
=========================================================
📅 日期: 待定
📚 章节: 第8章 函数式编程
💡 核心结论与 Java 视角对比：
1. 高阶函数：函数本身也可以赋值给变量，可以接收其他函数作为参数。
2. map/reduce：map 类似 Java Stream 的 map，reduce 类似 Stream 的 reduce。
3. 装饰器 (Decorator)：Python 的 AOP 神器，在不修改原函数的情况下增加功能。
=========================================================
"""
import functools

print("--- 8.1 & 8.2 高阶函数与 map/reduce ---")
# 任务 1：使用 map() 函数，把 [1, 2, 3, 4, 5] 变成 [1, 4, 9, 16, 25]。
# 提示：map 接收两个参数，一个是函数，一个是 Iterable。
# 你的代码：
def f(x):
    return x*x
r = map(f,  [1, 2, 3, 4, 5])
print(list(r))

print("\n--- 8.3 匿名函数 lambda ---")
# 任务 2：将任务 1 中的普通函数替换为 lambda 函数。
# 你的代码：

r2 = map(lambda x: x * x, [1,2,3,4,5])
print(list(r2))

print("\n--- 8.4 装饰器 (难点) ---")
# 任务 3：定义一个装饰器 log，在函数执行前打印 "调用函数: 函数名"。
# 提示：使用 @functools.wraps(func) 保持原函数名，内部定义 wrapper(*args, **kw)。 *args：表示任何多个无名参数，它是一个tuple；**kw表示关键字参数，它是一个dict。
# 你的代码：


def logFn(func):

    @functools.wraps(func)
    def wrapper(*args, **kw):
        # 1.在函数执行前做的事
        print("调用函数: %s" % func.__name__)

        # 2.真正执行原始函数
        return func(*args, **kw)

    return wrapper

@logFn
def fn():
    print("装饰器模式")

fn()