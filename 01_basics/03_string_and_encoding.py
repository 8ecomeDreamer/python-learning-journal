"""
=========================================================
📅 日期: 2026-10-28
📚 章节: 廖雪峰 - 5.2 字符串和编码
💡 核心结论与 Java 视角对比：
1. Python 3 的字符串是 Unicode 编码，支持多语言。对应 Java 的 String。
2. 网络传输或保存到磁盘时，需要 encode 成 bytes（字节流），对应 Java 的 byte[]。
3. 格式化输出：Python 有 %、format()、f-string，最推荐 f-string，类似 Java 的 String.format()。
=========================================================
"""

# 1. 字符与编码 (ord / chr)
print("A 的编码:", ord("A"))       # 65
print("中 的编码:", ord("中"))     # 20013
print("编码 66 对应:", chr(66))    # B

# 整数编码转str
print('\u4e2d\u6587')

# 2. 字符串转字节 (encode) 和 字节转字符串 (decode)
# 纯英文字符串转 bytes
print("ABC".encode("ascii"))      # b'ABC'
# 中文字符串转 bytes (注意：中文必须用 utf-8，不能用 ascii)
print("中文".encode("utf-8"))     # b'\xe4\xb8\xad\xe6\x96\x87'

# 3. 格式化输出 (重点：f-string 最香)
name = "coderJ"
age = 26

# 方式一：% 占位符 (类似 C 语言)
print("Hello, %s." % name)
print("Hello, %s. You are %d years old." % (name, age))

# %运算符就是用来格式化字符串的，%s表示用字符串替换，%d表示用整数替换，有几个%?占位符，后面就跟几个变量或者值，顺序要对应好。如果只有一个%?，括号可以省略。
print('%2d-%02d' % (3, 1))
print('%.4f' % (3.14159))

# 方式二：format() 方法
print("Hello, {}. You are {} years old.".format(name, age))

# 方式三：f-string (Python 3.6+ 引入，最直观，极力推荐！)
print(f"Hello, {name}. You are {age} years old.")
