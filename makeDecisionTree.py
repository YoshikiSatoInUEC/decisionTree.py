#Python3
import numpy as np
import math
import logging

###  ノードの決定     ###
#情報利得の計算関数(D:データセット)
def Gain(D):
    attrNum = [0,0,0] #[○,△,?]の数
    Dlength = len(D)  #データ数

    #全体の情報利得を計算
    infoAll = Info(data)

    #それぞれの独立変数毎で平均情報量を計算
    for attr in range(len(attribute_list)):
        #クラスに分類(○ or △ or ?)
        Cs = np.array(3) #クラス集合（初期）
        for data in D:
            #data[4]と一致するattrTypeのインデックスを取ってくる
attr_list = ["age","income","student","credit_rating","buy_computer"]
datas = np.array([["youth","high","no","fair","no"],
                  ["youth","high","no","excellent","no"],
                  ["middle_age","high","no","fair","yes"],
                  ["senior","medium","no","fair","yes"],
                  ["senior","low","yes","fair","yes"],
                  ["senior","low","yes","excellent","no"],
                  ["middle_age","low","yes","excellent","yes"],
                  ["youth","medium","no","fair","no"],
                  ["youth","high","yes","fair","yes"],
                  ["senior","medium","yes","fair","yes"],
                  ["youth","medium","yes","excellent","yes"],
                  ["middle_age","medium","no","excellent","yes"],
                  ["middle_age","high","yes","fair","yes"],
                  ["senior","medium","no","excellent","no"]])




#平均情報量計算関数(D:データセット)
def Info(D):
    Dlength = len(D) #全体のデータ数
    info = 0

    #平均情報量を計算して、結果を返す
    for i in range(len(attrType)):
        p = np.sum(D.transpose()[4] == attrType[i]) / Dlength #その属性の出現確率を計算
        info += -1 * p * math.log(p,3) #その属性の情報量を計算
    return info



info = Info(datas)
print(info)




#Gain(datas)
