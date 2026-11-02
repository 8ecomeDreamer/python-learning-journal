"""
=========================================================
📚 模块: 17 进程与线程
💡 核心对比：
1. GIL：Python 纯计算多线程无法利用多核，计算密集需用多进程；Java 多线程则是真正的并行。
2. ThreadLocal：每个线程绑定的独立上下文，在 Flask/FastAPI 等 Web 框架中用来隔离请求上下文。
=========================================================
"""
import multiprocessing
import os
import threading
import time
from _thread import lock

print("--- 1. 多线程与 Lock 竞态 ---")
balance = 0
# 任务 1：实现 change_it(n) 对 balance 加减，启动两个线程各跑 10 万次，观察无锁结果。
# 任务 2：使用 threading.Lock() 加锁后重跑，确保 balance 恢复为 0。

def change_it(n, use_lock):
    global balance
    for i in range(100000):
        # 加锁
        if use_lock:
            lock.acquire()
        try:
            balance += n
            # 👇 魔法就在这一行！强制让当前线程睡 0.0001 秒
            # 这就好比线程 A 刚把数据加上去，然后去上了个厕所，这就给线程 B 留出了插队篡改的机会！
            time.sleep(0.00001)
            balance -= n
        finally:
            if use_lock:
                # 释放锁
                lock.release()
# lock = threading.Lock()

# 测试无锁
print("[无锁测试]")
balance = 0
t1 = threading.Thread(target=change_it, args=(5, False))
t2 = threading.Thread(target=change_it, args=(8, False))
t1.start(); t2.start()
t1.join(); t2.join()
print(f"无锁结果: {balance} ")

print("\n--- 2. ThreadLocal 线程上下文 ---")
# 任务 3：创建 local_school = threading.local()，在两个线程中分别绑定 student 属性并打印。

# 创建全局变量
local_school = threading.local()

def process_school(name):
    # 将 student 属性绑定到当前线程
    local_school.student = name
    do_task()

def do_task():
    # 获取 student 线程
    print(f"线程 {threading.current_thread().name} 获取到的学生姓名是： {local_school.student}")

# 启动线程，传入不同的名字
t1 = threading.Thread(target=process_school, args=('Curry', ), name = 'Thread-A')
t2 = threading.Thread(target=process_school, args=('James', ), name = 'Thread-B')

# 运行线程
t1.start(); t2.start()
t1.join(); t2.join()

print("\n--- 3. 多进程与进程池 ---")
# 任务 4：用 multiprocessing.Process 启动子进程计算 2**10。
# 任务 5：用 multiprocessing.Pool(4) 并发执行多个任务。

def calc_power(base, exponent):
    result = base ** exponent
    print(f"子进程 [PID: {os.getpid()}] 计算 {base} 的 {exponent} 次方结果： {result}")

if __name__ == '__main__':
    # 创建子进程，target是目标， args是传参元组
    p = multiprocessing.Process(target=calc_power, args=(2, 3))

    # 启动子进程
    p.start()
    p.join()

    print("主进程结束")

    print("\n [进程池测试]")

def pool_task(n):
    time.sleep(1)
    return n * n

if __name__ == "__main__":
    with multiprocessing.Pool(processes=4) as pool:
        tasks =  [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
        print("开始并发执行任务...")
        results = pool.map(pool_task, tasks)

        print(f"进程池计算结果: {results}")