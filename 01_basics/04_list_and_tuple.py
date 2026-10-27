"""
=========================================================
📅 日期: 2026-10-28
📚 章节: 廖雪峰 - 5.3 使用list和tuple
💡 核心结论与 Java 视角对比：
1. List（列表）：类似 Java 的 ArrayList。有序、可变、可以装不同类型的数据（甚至嵌套）。
2. Tuple（元组）：类似 Java 的 final 数组。有序、一旦初始化就不可变，比 List 更安全。
3. 索引：从 0 开始。支持负数索引（-1 代表倒数第一个），这是 Java 没有的骚操作。
=========================================================
"""

print("--- 模块 1：List 的“万能性”与负数索引 ---")
# 1. 创建包含不同类型及嵌套的 List
L = ['Apple', 123, True, ['inner', 'list']]
print("L 的内容:", L)

# 2. 打印长度
print("L 的长度:", len(L))

# 3. 正向索引
print("索引 0:", L[0])

# 4. 负数索引 (Python 特有，Java 做不到)
print("索引 -1 (倒数第一个):", L[-1])

# 5. 双重索引获取嵌套值
print("嵌套取值:", L[3][0])


print("\n--- 模块 2：List 的增、删、改 ---")
classmates = ['Michael', 'Bob', 'Tracy']
print("原始列表:", classmates)

# 6. 末尾追加
classmates.append('Adam')
print("append 追加后:", classmates)

# 7. 指定位置插入
classmates.insert(1, 'Jack')
print("insert 插入后:", classmates)

# 8. 删除末尾
classmates.pop()
print("pop 删除末尾后:", classmates)

# 9. 修改指定索引
classmates[1] = 'Sarah'
print("修改索引 1 后:", classmates)


print("\n--- 模块 3：Tuple (元组) 的基础与不可变性 ---")
t = (1, 2, 3)
print("元组 t:", t)

# 尝试修改元组会报错：TypeError: 'tuple' object does not support item assignment
# t[0] = 4
print("注意：尝试修改 t[0] = 4 会抛出 TypeError，证明其不可变性。")


print("\n--- 模块 4：Tuple 的“单元素陷阱” ---")
# 不加逗号，会被识别为普通整数
t1 = (1)
print("t1 的类型:", type(t1))  # <class 'int'>

# 加逗号，才是真正的元组
t2 = (1,)
print("t2 的类型:", type(t2))  # <class 'tuple'>


print("\n--- 模块 5：终极陷阱 (Tuple 里的 List) ---")
t_trap = ('a', 'b', ['A', 'B'])
print("修改前:", t_trap)

# 修改 Tuple 内部的 List
t_trap[2][0] = 'X'
print("修改后:", t_trap)


"""
💡 终极拷问结论：
虽然 t_trap 是 tuple 类型不可变，但是里面的元素是 List。
Tuple 的不可变是指它指向的“内存地址（引用）”不可变。
这就像 Java 里用 final 修饰一个 List：你不能让这个 final 变量指向另一个新 List，
但是你可以往它原来指向的 List 里面 add() 或 set() 元素。
"""