#Python3
import numpy as np
attribute_list = ["Rel_local","Rel_root","Sim_local","Sim_root"]
attribute_values = np.array([["○","○","○","○"],
                             ["○","?","○","?"]]) #訓練データの属性値
explanation_data = np.array(["○","△"])#訓練データの説明変数

###  ノードの決定     ###
#属性スコア計算
def Information_content(attr_vals):
    countType = [0,0,0] #[○,△,?]の数
    numOfData = len(attr_vals)

    for attr_val in attr_vals:
        correct = np.sum(attr_val == "○") + correct
        ambiguous = np.sum(attr_val == "△") + ambiguous
        question = np.sum(attr_val=="?") + question
    print(correct,ambiguous,question)

    Info = 0
    for num in countType
        Info = -(num/numOfData)*(np.log2())

Information_content(attribute_values)
