# 章4 解答: 実務向けツール・静的解析

# 課題1
from collections import Counter

text = "apple banana apple orange banana apple"
words = text.split()
counter = Counter(words)
print(counter)

# 課題2（型ヒント追加）
def greet(name: str) -> str:
    return "Hello, " + name

# 課題3
# 手順：
# 1. greet.py に上記関数を保存
# 2. コマンドラインで次を実行
#    - black greet.py
#    - flake8 greet.py
# ※ pyproject.toml で black の設定をカスタマイズ可能
