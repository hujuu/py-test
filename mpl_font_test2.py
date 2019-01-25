from numpy.random import *
from matplotlib import pyplot as plt
import matplotlib as mpl
import matplotlib.font_manager as fm

print(mpl.get_configdir())
print(fm.findSystemFonts())

# 乱数生成
rand_nums = randn(100)

# 追加部分 フォントを指定する。
plt.rcParams["font.family"] = "IPAexGothic"

# ヒストグラム表示
plt.hist(rand_nums)
plt.xlabel("X軸と表示したい")
plt.ylabel("Y軸と表示したい")
plt.show()
