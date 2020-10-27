"""
날짜 : 2020/08/12
이름 : 권기민
내용 : 머신러닝 - Random Forest 실습(iris)
"""

import pandas as pd
import math
from sklearn import svm, metrics, model_selection
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

# 데이터 프레임 생성
df_iris = pd.read_csv('./data/iris.csv')
iris_data = df_iris.iloc[:, 0:4]
iris_label = df_iris.iloc[:, 4]

# 결과 확인
print(iris_data)
print(iris_label)

# 훈련데이터와 테스트데이터 분류
train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label)

# 학습하기
rf_model = RandomForestClassifier()
rf_model.fit(train_data, train_label)

# 검증하기
rf_result = rf_model.predict(test_data)

# 학습률 확인
rf_score = metrics.accuracy_score(rf_result, test_label)
print('rf_score :', math.trunc(rf_score*100),'점')