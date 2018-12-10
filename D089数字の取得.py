# 正規表現のモジュールをインポートしておく
import re

setting = input()

# 数値にマッチするパターン（0～9の文字(数字)の繰り返し)を定義
pattern = r'([0-9]*)'

# 元の文字列が変数に入っているものとすると、re.findallを使ってlistsに数値を表す文字列のリストが得られる
lists = re.findall(pattern, setting)

print(lists[0])