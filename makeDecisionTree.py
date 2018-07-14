#Python3
import numpy as np
import math
import logging
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


###  関数群     ###
#属性の種類を計算(D:その属性のみの全データ)
def caluculateAttrType(D):
    attrType = [];
    typeNum = [];
    for data in D:
        if data not in attrType:
            attrType.append(data)
            typeNum.append(1)
        else:
            typeNum[attrType.index(data)] = typeNum[attrType.index(data)]+1
    return [attrType,typeNum]


#平均情報量計算関数(D:その属性のみのデータ)
def Info(D):
    info = 0
    attrType = caluculateAttrType(D)

    #平均情報量を計算して、結果を返す
    for attr in attrType[1]:
        p = attr / len(D) #その属性の出現確率を計算
        if p != 0:
            info += -1 * p * math.log2(p) #その属性の情報量を計算
    return info


#属性ごとの情報利得(attr:属性データ,train:訓練データ)
def InfoA(attrD,trainD):
    info = 0  #最終的に出力する情報利得
    attrType = caluculateAttrType(attrD)   #attrDの属性の種類を出力
    aDtD = np.array([attrD,trainD])
    for i in range(len(attrType[0])):
        info += (attrType[1][i]/len(trainD)) * Info(aDtD[1][aDtD[0] == attrType[0][i]])

    return info


def makeDecisionTree(datas,attr_list):
    ## 変数定義 ##
    transD = datas.transpose()  #転置したdata
    Dlength = len(datas)  #データ数
    trainD = transD[len(transD)-1] #訓練データ
    attrD = transD[:len(transD)-1] #属性データ集合
    GainMax = 0 #情報利得最大値

    ## 情報利得から選択する属性を決定 ##
    #全体の情報利得を計算
    infoAll = Info(trainD)
    #各情報利得計算&最大の情報利得とその属性を記録
    for i in range(len(attrD)):
        tmpGM = GainMax
        GainMax = max(GainMax,infoAll-InfoA(attrD[i],trainD))
        if tmpGM != GainMax or i == 0:
            MaxAttr = attr_list[i]
    ##MaxAttrで決定されたノードを元に分類
    #MaxAttrに関するデータ収集
    maxAttrIndex = attr_list.index(MaxAttr)#最大属性のインデックス
    maxAttrD = attrD[maxAttrIndex]#最大属性データ
    maxAttrType = caluculateAttrType(maxAttrD)[0] #情報利得最大の属性値タイプ一覧


