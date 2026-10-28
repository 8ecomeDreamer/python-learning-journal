"""
=========================================================
📅 日期: 待定
📚 章节: 第7章 高级特性
💡 核心结论与 Java 视角对比：
1. 切片：L[0:3] 取前3个，L[-2:] 取后2个。Java里通常需要 subList 或循环。
2. 迭代：for...in 可以遍历任何可迭代对象（list, tuple, dict, str）。
3. 列表生成式：[x * x for x in range(10)] 极大地简化了代码。
4. 生成器：使用 yield，一边循环一边计算，极其节省内存。
=========================================================
"""

print("--- 7.1 切片 ---")
# 任务 1：定义 L = list(range(100))，取出前 10 个数、后 10 个数、以及 11-20 个数。
# 你的代码：
L = list(range(100))
print(L[:10])
print(L[-10:])
print(L[11:20])

print("\n--- 7.2 迭代 ---")
# 任务 2：定义一个字典 d = {'a': 1, 'b': 2, 'c': 3}
# 使用 for 循环同时迭代出它的 key 和 value。
# 提示：for k, v in d.items():
# 你的代码：
d = {'a': 1, 'b': 2, 'c': 3}
for key,value in d.items():
    print(key, value)

print("\n--- 7.3 列表生成式 ---")
# 任务 3：使用一行代码，生成 [1x1, 2x2, 3x3, ..., 10x10] 的列表。
# 你的代码：
[print(x * x) for x in range(0,10)]

# 任务 4：生成一个列表，包含 ['Hello', 'World', 18, 'Apple', None] 中所有的字符串，并忽略大小写。
# 提示：isinstance(x, str)
# 你的代码：
print()

[print(x.lower()) for x in ['Hello', 'World', 18, 'Apple', None] if isinstance(x, str)]

print("\n--- 7.4 生成器 ---")
# 任务 5：把列表生成式的 [] 改成 ()，创建一个生成器，并用 next() 打印前三个元素。
# 你的代码：

g = ( x * x for x in range(0,10))

print(next(g))
print(next(g))
print(next(g))

# 任务 6：编写一个生成器函数 fib(max)，输出斐波那契数列。
# 提示：把 print(b) 改成 yield b。
# 你的代码：

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b # 魔法在这里！把 print(b) 替换掉
        a, b = b, a + b
        n = n + 1
    return 'done'

# 1. 获取生成器对象
f = fib(5)

# 2. 体验 next() 挤牙膏
print(next(f)) # 输出 1
print(next(f)) # 输出 1
print(next(f)) # 输出 2

# 3. 用 for 循环遍历生成器（最常用）
print("\n--- for 循环遍历 ---")
for x in fib(6):
    print(x)