"""
=========================================================
📚 模块: 16 IO编程
💡 核心对比：
1. with open()：本质是上下文管理器，实现 __enter__ / __exit__ 方法，等价于 Java try-with-resources。
2. BytesIO：用于在内存中读写二进制数据（如图片、视频流），是文件上传处理的基础。
=========================================================
"""
from io import StringIO, BytesIO

from datetime import datetime

import json

print("--- 1. 文件读写与指针 ---")
# 任务 1：用 'w' 模式写入多行文本，用 'r' 读取全部内容。
# 任务 2：用 f.seek(0) 回到文件开头，使用 read(5) 读取前 5 个字符，观察指针位置。

with open("../test/test_io.txt", "w", encoding="utf-8") as f:
    f.write("第一行文本\n")
    f.write("第二行文本\n")

with open("../test/test_io.txt", "r", encoding="utf-8") as f:
    print("读取全部内容\n")
    print(f.read())

    #移动指针
    f.seek(0)

    print("读取前五个字符\n")
    print(f.read(5))

print("\n--- 2. StringIO / BytesIO ---")
# 任务 3：创建 StringIO，写入中文字符串并读取。
# 任务 4：创建 BytesIO，写入 b'Hello'，读取并解码。

s_io = StringIO()
s_io.write("你好，StringIO!")

s_io.seek(0)
print("StringIO读取：", s_io.read())
print("StringIO getvalue:", s_io.getvalue())

bytes_io = BytesIO()
bytes_io.write(b"Hello")

bytes_io.seek(0)
print("BytesIO读取", bytes_io.read())


print("\n--- 3. JSON 序列化与自定义编码 ---")
# 任务 5：定义包含 datetime 对象的 dict，用 json.dumps(..., default=str) 序列化。
# 任务 6：将嵌套字典转为 JSON，再用 json.loads 还原。

data = {
    "name": "coderJ",
    "current_time": datetime.now(), # datetime 对象默认不能被 json 序列化
    "skills": ["Java", "Vue", "Python"] # 嵌套列表
}

# default=str 的意思是：如果遇到json不认识的类型，就用str()将它转成字符串
json_str = json.dumps(data, default=str, ensure_ascii=False)
print("序列化后的JSON字符串：\n", json_str)

restored_dict = json.loads(json_str)
print("\n反序列化后的字典：\n", restored_dict)
print(f"\n取出技能了列表： {restored_dict['skills']}")

# 总结：
# dumps: dump string，将python的字典、列表转换成一段文本。
# loads: 使用loads还原成python的字段或列表。