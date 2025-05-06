# 章5 解答: テストとオブジェクト指向の拡張

# 課題1
from dataclasses import dataclass
import json

@dataclass
class User:
    name: str
    age: int

user = User("Taro", 30)
json_str = json.dumps(user.__dict__, ensure_ascii=False)
print(json_str)

# 課題2
import re

email = input("メールアドレスを入力してください: ")
pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"

if re.match(pattern, email):
    print("有効なメールアドレスです")
else:
    print("無効なメールアドレスです")

# 課題3（greet_user関数のテスト）
class Greeter:
    def greet_user(self, name: str) -> str:
        return f"Hello, {name}!"

# pytest テストコード
# ファイル名: test_greeter.py

def test_greet_user():
    greeter = Greeter()
    assert greeter.greet_user("Alice") == "Hello, Alice!"
