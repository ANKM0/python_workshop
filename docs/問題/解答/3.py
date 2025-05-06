# 章3 解答: Pythonの表現力とファイル処理

# 課題1
even_squares = [x**2 for x in range(1, 21) if x % 2 == 0]
print("偶数の2乗:", even_squares)

# 課題2
nums = [5, 10, 15, 20]
doubled = list(map(lambda x: x * 2, nums))
print("2倍にしたリスト:", doubled)

# 課題3
import csv

with open("./scores.csv", "w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["名前", "点数"])
    writer.writerow(["Alice", 80])
    writer.writerow(["Bob", 90])
    writer.writerow(["Carol", 70])

# 課題4
scores = []
with open("./scores.csv", "r") as file:
    reader = csv.reader(file)
    next(reader)  # ヘッダーをスキップ
    for row in reader:
        scores.append(int(row[1]))

average = sum(scores) / len(scores)
print("平均点:", average)

# 課題5
from pathlib import Path

files = Path(".").iterdir()
print("現在のディレクトリのファイル:")
for path in files:
    print(path.name)
