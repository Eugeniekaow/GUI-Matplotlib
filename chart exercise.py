"""
=== 1. covid-19 ====
seaborn
設計3個 seaborn
改為 def 函數
昨天作業的 資料
"""
import seaborn as sns    # pip install seaborn    # 匯入函示庫 seaborn 換名 sns
import pandas as pd                               # 匯入函示庫 pandas 換名 pd
import matplotlib.pyplot as plt                   # 匯入函示庫 matplotlib.pyplot 換名 plt



sns.set_theme(style="whitegrid")                  # 設定主題

df = pd.DataFrame({"A": ["Taipei", "Newtaipei", "Taoyuan"],
                   "B": [2903,5062,3264],
                   "C": ["Taipei", "Newtaipei", "Taoyuan"]})

g = sns.catplot(
    data=df, kind="bar",
    x="A", y="B", hue="C",             # 設定 x=A, y=C, hue=C
    ci="sd",                          # 設定 ci 顏色
    palette="dark",                   # 設定色彩
    alpha=.6,                         # 設定 alpha  透明度
)

g.despine(left=True)
g.set_axis_labels("city", "number of people")
g.legend.set_title("COVID-19 ")

plt.savefig("5.png")
plt.show()


import seaborn as sns    # pip install seaborn    # 匯入函示庫 seaborn 換名 sns
import pandas as pd                               # 匯入函示庫 pandas 換名 pd
import matplotlib.pyplot as plt                   # 匯入函示庫 matplotlib.pyplot 換名 plt



sns.set_theme(style="whitegrid")                  # 設定主題

df = pd.DataFrame({"A": [1,2,3],
                   "B": [2903,5062,3264],
                   "C": [7, 8, 9]})

g =sns.lmplot(
           data=df,
           x="A",
           y="B",
           col="C",
           hue="C",
           col_wrap=2, ci=None, palette="muted", height=4,
           scatter_kws={"s": 50, "alpha": 1})
"""
g = sns.catplot(
    data=df, kind="bar",
    x="A", y="B", hue="C",             # 設定 x=A, y=C, hue=C
    ci="sd",                          # 設定 ci 顏色
    palette="dark",                   # 設定色彩
    alpha=.6,                         # 設定 alpha  透明度
)
"""
g.despine(left=True)
g.set_axis_labels("city", "number of people")
#g.legend.set_title("title")


plt.savefig("11.png")
plt.show()

import seaborn as sns    # pip install seaborn    # 匯入函示庫 seaborn 換名 sns
import pandas as pd                               # 匯入函示庫 pandas 換名 pd
import matplotlib.pyplot as plt                   # 匯入函示庫 matplotlib.pyplot 換名 plt

sns.set_theme(style="whitegrid")                  # 設定主題

df = pd.DataFrame({"A": [2903,2578,2457,2266,2355],
                   "B": [2903,2578,2457,2266,2355],
                   "C": [0, 0, 1, 1, 1]})      # 分類
g=sns.pairplot(df, hue="C")



plt.savefig("22.png")
plt.show()


