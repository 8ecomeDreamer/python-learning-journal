"""
=========================================================
📅 日期: 2026-10-28
📚 章节: 廖雪峰 - 5.4 条件判断
💡 核心结论与 Java 视角对比：
1. 语法结构：Python 使用 `if 条件:`，注意冒号和缩进，无大括号。
2. 分支：`if - elif - else`，没有 Java 的 `else if`。
3. 真假规则 (Truthy/Falsy)：非零数值、非空字符串/列表等视为 True；0、""、[]、None 视为 False。
=========================================================
"""

print("--- 模块 1 & 2：基础与多重判断 ---")
age = 10

if age >= 18:
    print("adult")
elif age >= 6:
    print("teenager")
else:
    print("kid")


print("\n--- 模块 3：结合 input() 获取用户输入 ---")
# 注意：input() 拿到的永远是字符串，必须用 int() 转换
number = int(input("请输入一个数字: "))
if number > 0:
    print("这是一个正数")
else:
    print("这是一个非正数")


print("\n--- 模块 4：Python 的“真假”规则 ---")
# 你可以手动修改 x 的值（0, 1, "", "abc", [], [1, 2]）来验证
x = []
if x:
    print("x 被视为 True")
else:
    print("x 被视为 False")


print("\n--- 模块 5：条件表达式（三元运算）---")
# Java: String result = age >= 18 ? "adult" : "kid";
# Python: A if 条件 else B
age = 20
result = "adult" if age >= 18 else "kid"
print("三元运算结果:", result)

# 💡 任务 7 (总结)：
# 心得：input() 接收的数据类型是 str，必须强转 int。Python 的三元表达式 `A if 条件 else B` 读起来比 Java 的问号冒号更直观。