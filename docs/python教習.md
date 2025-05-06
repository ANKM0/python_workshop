# Python 学習プラン（JS経験者向け）

## 章1: 開発環境の準備

### 内容

* Python最新版インストール（推奨: 3.10以上）
* VSCode + Python拡張
* 仮想環境（venv / Poetry）
* venvとPoetryの違い
* （補足）colab/jupyter, git/github

### ゴール

Python開発に必要な基本ツールをインストール・起動できるようになる

### 練習課題

* 仮想環境を作成し `hello.py` を実行する
* VSCodeで仮想環境を選択し、Pythonコードを実行

---

## 章2-1: データ型と基本操作

### 内容

* コメントの書き方
* 変数と代入
* データ型：int, float, str, bool
* 数値計算、文字列操作
* 演算子・論理演算子

### ゴール

Pythonの基本データ型と計算・文字列処理が書けるようになる

### 練習課題

* ユーザーから2つの数値を入力して四則演算
* 文字列のフォーマット出力（例："名前: 山田, 年齢: 30"）

---

## 章2-2: コレクションと制御構文

### 内容

* list, dict, set, tuple
* if文、for、while
* break、continue
* 関数（def, 戻り値, デフォルト引数, 可変長引数）

### ゴール

条件分岐とループを使って処理の流れを制御できるようになる

### 練習課題

* リストの合計値、平均値を求める関数
* FizzBuzzの実装

---

## 章2-3: モジュールと例外処理

### 内容

* try / except / finally
* import / from import

### ゴール

エラー発生を制御しながら、標準モジュールを使えるようになる

### 練習課題

* ユーザー入力をintに変換する処理（例外処理あり）
* `math`, `random` をインポートして利用

---

## 章3: Pythonの表現力とファイル処理

### 内容

* クラス（基本構文）
* デバッグ（print, breakpoint）
* f-string、リスト内包表記、lambda
* enumerate, zip
* datetime / time
* ファイル操作（open/with）
* CSV, JSON処理
* os, sys, pathlib

### ゴール

Pythonらしい書き方で、日常的なファイルやデータを処理できるようになる

### 練習課題

* CSVを読み取り、平均値を出力
* JSONに保存→再読み込み
* フォルダ内のファイル一覧を表示

---

## 章4: 実務向けツール・静的解析

### 内容

* collections（defaultdict, Counter, deque）
* itertools, functools（map, filter, reduce）
* タイプアノテーション / mypy
* PEP8、DocString
* black, flake8（+ pyproject.toml 設定）

### ゴール

Pythonコードの品質を高めるための書き方・ツールを使えるようになる

### 練習課題

* Counterで単語出現回数を数える
* アノテーション付き関数＋mypyで型チェック
* black, flake8でフォーマット

---

## 章5: テストとオブジェクト指向の拡張

### 内容

* 正規表現
* logging
* pytest（テスト作成）
* 継承、dataclass
* JSONとクラスの変換

### ゴール

小規模なアプリをクラス・テスト付きで構成できるようになる

### 練習課題

* dataclassでUserを定義し、JSONに変換
* 正規表現でメールアドレスチェック
* クラスメソッドにpytestテストを書く

---

## 章6: Python高度トピック（任意）

### 内容

* デコレーター
* ジェネレーター / イテレーター
* コンテキストマネージャー
* 並列処理（threading / multiprocessing）
* 非同期処理（asyncio）

### ゴール

Pythonの高度な制御・抽象化手法を理解し、応用できるようになる

### 練習課題

* デコレータで関数の実行時間をログ出力
* ジェネレータでフィボナッチ数列
* `asyncio`で並列ダウンロード（模擬）
