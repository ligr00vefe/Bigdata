"""
날짜 : 2020/08/12
이름 : 권기민
내용 : 머신러닝 - iris 서포트벡터머신 분석 실습
"""
# pandas(파이썬 데이터프레임 패키지) 설치
# seaborn 데이터프레임 시각화 프로그램
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import math
from sklearn import svm, metrics
from sklearn.model_selection import train_test_split  # 훈련 데이터를 무작위로 테스트하기위해 데이터를 뒤섞는 모듈

# 붓꽃 데이터프레임 생성
df_iris = pd.read_csv('./data/iris.csv')

# 결과 확인
# print(df_iris)

# 붓꽃 상관분석 차트 출력
sns.pairplot(df_iris, hue='variety')

# 결과 확인
# plt.show()

# 학습데이터 준비
iris_data = df_iris[['sepal.length', 'sepal.width', 'petal.length', 'petal.width']]
iris_label = df_iris['variety']
# print(iris_data)
# print(iris_label)

# 훈련데이터와 테스트데이터 분류
train_data, test_data, train_label, test_label = train_test_split(iris_data, iris_label)

# 학습하기
model = svm.SVC()
model.fit(train_data, train_label)

# 검증하기
result = model.predict(test_data)
print(result)

# 정답률(학습률) 확인
score = metrics.accuracy_score(test_label, result)
print('학습률 :', math.trunc(score*100))




