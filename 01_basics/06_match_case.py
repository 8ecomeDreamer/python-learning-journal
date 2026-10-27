"""
=========================================================
📅 日期: 2026-10-29
📚 章节: 廖雪峰 - 5.5 模式匹配
💡 核心结论与 Java 视角对比：
1. match-case 是 Python 3.10 引入的，类似于 Java 的 switch 语句。
2. 注意：每个 case 后面都有冒号，匹配成功后直接结束，不需要写 Java 里的 break。
3. 最后的 case _: 相当于 Java 的 default。
=========================================================
"""

print("--- 模块 1：基础 match-case (类似 switch) ---")
# 任务 1：定义变量 command = "start"
# 使用 match command 匹配：
# 如果是 "start"，打印 "系统启动中..."
# 如果是 "stop"，打印 "系统已停止。"
# 其他情况（用 case _:），打印 "未知指令！"

# 你的代码：
command = "start"
match command:
    case "start":
        print("系统启动中...")
    case "stop":
        print("系统已停止")
    case _:
        print("未知指令！")


print("\n--- 模块 2：模式匹配进阶 (匹配列表结构) ---")
# 任务 2：定义变量 point = [0, 5]
# 使用 match point 匹配：
# case [0, y]: 打印 "在 Y 轴上，Y 坐标是", y
# case [x, 0]: 打印 "在 X 轴上，X 坐标是", x
# case [x, y]: 打印 "普通坐标", x, y
# 提示：这能直接把列表里面的值提取出来赋给变量。

# 你的代码：
point = [0, 5]
# point = [0, 5]
match point:
    case [0, y]:
        print("在 Y 轴上，Y 坐标是", y)
    case [x, 0]:
        print("在 X 轴上，X 坐标是", x)
    case [x, y]:
        print("普通坐标", x, y)


print("\n--- 模块 3：加上守卫 (if 条件) ---")
# 任务 3：定义变量 score = 85
# 使用 match score 匹配：
# case x if x >= 90: 打印 "优秀"
# case x if x >= 60: 打印 "及格"
# case _: 打印 "不及格"
# 提示：这相当于在 case 里面又加了一层 if 判断。

# 你的代码：
score = 85
# point = [0, 5]
match score:
    case x if x >= 90:
        print("优秀")
    case x if x >= 60:
        print("及格")
    case _:
        print("不及格")

# 💡 任务 4：请用一句话总结，你觉得相比于 if-elif-else，match-case 的优势是什么？
# 你的结论：match-case 不仅能做条件判断，还能直接‘拆解’列表或字典的结构，把里面的值顺手捞出来，比写一堆 if 判断更优雅。