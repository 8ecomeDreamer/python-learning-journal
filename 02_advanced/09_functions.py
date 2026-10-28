"""
=========================================================
📅 日期: 2026-10-31 (按你的实际日期填)
📚 章节: 廖雪峰 - 第6章 函数
💡 核心结论与 Java 视角对比：
1. 定义：使用 def 关键字，没有返回值类型声明，直接 def 函数名(参数):。
2. 返回值：如果没有 return 语句，默认返回 None（相当于 Java 的 void）。
3. 参数魔法：支持默认参数、可变参数 (*args 接收元组)、关键字参数 (**kwargs 接收字典)，比 Java 灵活得多。
4. 空函数：使用 pass 占位，防止语法报错。
=========================================================
"""

# 请利用Python内置的hex()函数把一个整数转换成十六进制表示的字符串：
n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))

print("--- 6.1 & 6.2 定义函数与空函数 ---")
# 任务 1：定义一个函数 my_abs(x)，实现求绝对值的功能。
# 提示：使用 if x >= 0: return x，否则 return -x。
# 你的代码：

def my_abs(x):
    if x >= 0:
        return x
    else: return -x

# 任务 2：定义一个空函数 nop()，里面什么都不写，但要保证程序不报错。
# 提示：使用 pass。
# 你的代码：

def nop():
    pass


print("\n--- 6.3 函数的参数 (重头戏) ---")
# 任务 3：定义一个函数 power(x, n=2)，计算 x 的 n 次方。
# 提示：使用 ** 运算符计算次方（如 x ** n），n 默认值为 2。
# 你的代码：

def power(x, n=2):
    return x ** n

print(power(2))

# 任务 4：定义一个函数 calc(*numbers)，接收任意个参数，并返回它们的和。
# 提示：参数前面的 * 表示可变参数，numbers 在函数内部会自动变成一个 tuple。
# 你的代码：

def calc(*numbers):
    sum = 0
    for n in numbers:
        sum += n
    return sum

print(calc(1,3,5,7,9))

print("\n--- 6.4 递归函数 ---")
# 任务 5：使用递归实现阶乘 fact(n)。
# 阶乘定义：n! = 1 * 2 * 3 * ... * n，且 1! = 1。
# 提示：递归的基线条件是 if n == 1: return 1。
# 你的代码：

def Factorial(n):
    if n == 1: return 1
    return n * Factorial(n-1)

print(Factorial(5))

