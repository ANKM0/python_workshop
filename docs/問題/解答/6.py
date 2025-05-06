# 章6 解答: Python高度トピック

# 課題1

def log_decorator(func):
    def wrapper(*args, **kwargs):
        print("開始")
        result = func(*args, **kwargs)
        print("終了")
        return result
    return wrapper

@log_decorator
def say_hello():
    print("こんにちは！")

say_hello()

# 課題2
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
for _ in range(10):
    print(next(fib))

# 課題3
with open("example.txt", "w") as f:
    f.write("Hello Context!")

# 課題4
import threading

def thread_task(name):
    print(f"Hello from thread {name}")

threads = []
for i in range(3):
    t = threading.Thread(target=thread_task, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

# 課題5
import asyncio

async def task(n):
    await asyncio.sleep(1)
    print(f"Message from task {n}")

async def main():
    await asyncio.gather(
        task(1),
        task(2),
        task(3)
    )

asyncio.run(main())
