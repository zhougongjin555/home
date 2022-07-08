import os
import pandas as pd


def getFiles(path, suffix):
    # 获取文件夹所有xlsx文件
    return [os.path.join(root, file) for root, dirs, files in os.walk(path) for file in files if file.endswith(suffix)]


def summary(file):
    # 汇总有效信息
    df = pd.read_excel(file, sheet_name='表-09 综合单价分析表', header=None)
    df.columns = list(map(lambda x: "col" + str(x), list(range(df.shape[1]))))
    res = df[
        (df["col0"] == "子目编码")
        | (df["col0"] == "人工单价")
        | (pd.isnull(df["col0"]) & ~(pd.isnull(df["col1"])) & (df["col1"] != "材料费小计"))
    ]
    return res


files = getFiles("E:\home\复习\算法\数据结构\excel", "xlsx")
for file in files:
    print(summary(file))