#https://www.hackerrank.com/challenges/predicting-office-space-price/problem
import pandas as pd
# import matplotlib.pyplot as plt
# import sys
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import Ridge
from sklearn.linear_model import LinearRegression
from sklearn.linear_model import BayesianRidge
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

def getDf(A,B, f,s,t):

	return pd.DataFrame(A), pd.DataFrame(B)


def check(df, tf, f):
	features = df.drop([f], axis=1)
	target = df[f]
	tr_x,tt_x,tr_y,tt_y = train_test_split(features, target, test_size=0.4, shuffle=True)

	for a in [1,0.1,0.001]:
		model = make_pipeline(PolynomialFeatures(3), BayesianRidge(alpha=a))
		model.fit(features,target)
		print(model.score(tt_x,tt_y))
def model(df, tf, f):
	features = df.drop([f], axis=1)
	target = df[f]
	
	model = LinearRegression()
	tr_x,tt_x,tr_y,tt_y = train_test_split(features, target, test_size=0.4, shuffle=True)
	
	model = make_pipeline(PolynomialFeatures(2), Ridge(alpha = 0.001))
	model.fit(features,target)
	ans =model.predict(tf)
	for a in ans:
		print("{0:.2f}".format(a))
	


# sys.stdin = open('sample')
f,s = map(int, raw_input().split(" "))
data = []
for x in range(s):
	data.append([float(x) for x in raw_input().split(" ")])

t = int(raw_input().strip())
test = []
for x in range(t):
	test.append([float(x) for x in raw_input().split(" ")])
df,tf= getDf(data,test, f,s,t)
model(df,tf,f)
