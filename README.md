# 清算最適化アルゴリズムの検証

## Overview

割り勘計算サービス、Walicaの清算最適化アルゴリズムの検証を行うためのプログラムです。

詳しくはこちらをご覧ください。

https://qiita.com/MasashiHamaguchi/items/0348082984b8c94ca581

## Install

以下のコマンドを実行して、パッケージのインストールを行ってください。

```bash
$ pip install -r requirements.txt
```

## Usage

`main.py`を実行すると、清算時の送金額を計算することができます。

引数にWalicaのURLを指定すると、Walicaからデータを取得して送金額の計算を行います。

```bash
# サンプルデータで実行
$ python main.py

# Walicaからデータを取得して実行
$ python main.py https://walica.jp/group/xxxxxxxxxxxxxxxxxxxx
```

## Reference

- https://walica.jp/
- https://note.com/38ch/n/nf9824d7c6d77
- https://kyogom.com/tech/walica-releace/
- https://uechi.io/blog/split-bill/?fbclid=IwAR2Rki4umS-IgSWivLCXKi2m02n3JG0wVhgxygdBWCnvvYa9FzS76GU4AuM

