"""
=========================================================
📅 日期: 2026-10-30
📚 章节: 廖雪峰 - 5.6 循环
💡 核心结论与 Java 视角对比：
1. for 循环：Python 的 for 是遍历（for-each），没有传统的 (int i=0; i<10; i++)。
2. range()：用来生成整数序列，通常配合 for 循环当计数器用。
3. while 循环：和 Java 完全一样。
4. break / continue：和 Java 完全一样。
=========================================================
"""

print("--- 模块 1：for...in 遍历 ---")
# 任务 1：定义一个列表 names = ['Michael', 'Bob', 'Tracy']
# 使用 for 循环遍历打印每一个名字。
# 提示：for name in names:

# 你的代码：
names = ['Michael', 'Bob', 'Tracy']
for name in names:
    print(name)

print("\n--- 模块 2：range() 函数 (计数循环) ---")
# 任务 2：使用 for 循环配合 range(5)，打印 0 到 4。
# 提示：range(5) 生成的是 0, 1, 2, 3, 4（包左不包右）。
# 你的代码：
for num in range(5):
    print(num)

# 任务 3：使用 for 循环配合 range(1, 10, 2)，打印 1, 3, 5, 7, 9。
# 提示：range(起始, 结束, 步长)。
# 你的代码：

print()

for rangeNum in range(1, 10, 2):
    print(rangeNum)

print("\n--- 模块 3：while 循环 ---")
# 任务 4：使用 while 循环，计算 1 到 100 的整数和，并打印结果。
# 提示：定义一个 sum = 0，定义一个 n = 1，当 n <= 100 时循环。
# 你的代码：

sum = 0
n = 1
while n <= 100:
    sum += n
    n += 1
print(sum)

print("\n--- 模块 4：break 和 continue ---")
# 任务 5：使用 for 循环配合 range(1, 11) 遍历 1 到 10。
# 如果数字是 5，打印 "遇到 5 停啦！" 并使用 break 结束循环。
# 你的代码：

for index in range(1, 11):
    if index == 5:
        print("遇到 5 停啦！")
        break
    print(index)

print()
# 任务 6：使用 for 循环配合 range(1, 11) 遍历 1 到 10。
# 如果数字是偶数（num % 2 == 0），跳过本次循环（continue）。
# 否则打印该奇数。
# 你的代码：
for index in range(1, 11):
    if index % 2 == 0:
        continue
    print(index)


# 💡 任务 7：如果我想无限循环，应该怎么写？
# 你的代码：
while True:
    print("无限循环")