#Python3
import numpy as np
import math
import logging
attribute_list = ["Rel_local","Rel_root","Sim_local","Sim_root"]
attrType = ["○","△","?"]
datas = np.array([["○","○","○","○","○"],
                 ["○","○","○","○","?"],
                 ["○","?","○","?","△"]]) #訓練データの集合(x1,x2,x3,x4,c)
                                      #x1:Rel_root,x2:Rel_local,x3:Sim_root,x4:Sim_local

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
