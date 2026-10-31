"""
=========================================================
📚 模块: 15 错误、调试和测试
💡 核心对比：
1. 异常捕获顺序：子类异常在前，父类异常在后（类似 Java）。
2. unittest 断言：Python 内置 unittest 风格与 JUnit 类似，支持 setup/teardown。
=========================================================
"""
import logging
import unittest

print("--- 1. 异常捕获与 finally 资源释放 ---")
# 任务 1：用 try...except ValueError 捕获 int('abc')，并在 finally 中打印 '执行完毕'。
# 任务 2：在 except 中加 as e，打印 e（体验类似 Java 的 catch (Exception e)）。

def getValue(value):
    try:
        return int(value)
    except ValueError as e:
        print("捕获ValueError", e)
    finally:
        print("执行完毕")

getValue("abc")
getValue(22)

print("\n--- 2. logging 级别划分 ---")
# 任务 3：配置 logging.basicConfig(level=logging.INFO)，分别打印 debug, info, warning, error 级别的日志，观察输出。
logging.basicConfig(level=logging.INFO, format= '%(asctime)s - %(name)s - %(levelname)s - %(message)s)')

logging.debug("这是一个debug日志")
logging.info("这是一个info日志")
logging.warning("这是一个warning日志")
logging.error("这是一个error日志")


print("\n--- 3. 单元测试 TestCase ---")
# 任务 4：写一个测试类继承 unittest.TestCase。
# 任务 5：写 test_abs 测试 abs(-1) == 1，写 test_str_upper 测试 'abc'.upper() == 'ABC'。

class TestMyFunctions(unittest.TestCase):

    def test_abs(self):
        self.assertEqual(abs(-1), 1)

    def test_str_upper(self):
        self.assertEqual('abc'.upper(), "ABC")

if __name__ == '__main__':
    unittest.main()


#总结：
#logging级别： debug < info < warning < error < critical