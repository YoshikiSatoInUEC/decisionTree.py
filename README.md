# decisionTree.py
Pythonで作成したID3決定木作成アルゴリズム(知識データ工学課題用)

## 関数
* main関数:makeDecisionTree(datas,attribute_list)
   * 入力：datas(属性値＋訓練データの行列),attr_list(属性値+訓練データの名前)
   * 出力：print文で条件分岐を出力(「if (属性名) == (属性値) \n(改行) (結果)」の形式で)
* 属性ごとの種類とタイプを計算する関数：caluculateAttrType(D)
  * 入力：D(属性ごとの種類を分けたいデータ)
  * 出力：attrType(属性の種類),typeNum(属性の種類毎の個数)
* 平均情報量計算関数：Info(D)
  * 入力：D(訓練データ)
  * 出力：info(平均情報量)
* 属性ごとの平均情報量計算関数：InfoA(attrD,trainD)
  * 入力：attrD(求めたい属性のデータ),trainD(訓練データ)
  * 出力：info(その属性の平均情報量)
