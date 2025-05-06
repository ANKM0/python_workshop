# 章2-3 解答: モジュールと例外処理

# 課題1
try:
    value = int(input("数値を入力してください: "))
    print(f"2倍の値: {value * 2}")
except ValueError:
    print("数値を入力してください")

# 課題2
import math
import random

num = float(input("平方根を求めたい数値を入力してください: "))
print(f"{num} の平方根は {math.sqrt(num)}")

print("1〜10の乱数5個:")
for _ in range(5):
    print(random.randint(1, 10))
