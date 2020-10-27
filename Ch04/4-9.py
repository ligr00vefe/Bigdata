"""
날짜 : 2020/08/12
이름 : 권기민
내용 : 머신러닝 - mnist 숫자이미지 서포트 벡터 머신 분석 실습
"""

import pandas as pd
import math
from sklearn import svm, metrics

# 데이터프레임
df_mnist_train = pd.read_csv('./data/mnist_train.csv')
df_mnist_test  = pd.read_csv('./data/mnist_test.csv')

# 학습 데이터 준비 및 데이터 초기화(픽셀데이터를 0 ~1 사이 실수로 초기화)
df_mnist_train_data = df_mnist_train.iloc[:, 1:]/255 # 0열은 label이기 때문에 1열부터 계산
df_mnist_train_label = df_mnist_train.iloc[:, 0] # 0열의 label 값만 출력

# 테스트데이터 준비 및 데이터 초기화
df_mnist_test_data = df_mnist_test.iloc[:, 1:]/255
df_mnist_test_label = df_mnist_test.iloc[:, 0]

# 학습하기
model = svm.SVC()
model.fit(df_mnist_train_data, df_mnist_train_label)

# 검증하기
result = model.predict(df_mnist_test_data)

# 학습률 확인
score = metrics.accuracy_score(df_mnist_test_label, result)
print(math.trunc(score))


