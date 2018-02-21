

#https://www.hackerrank.com/challenges/the-best-aptitude-test/problem

import pandas as pd 
import numpy as np
import math as Math


def r(A,B):
    n = len(A)
    suA = sum(A)
    suB = sum(B)
    val1 = n*(sum([A[i]*B[i] for i in range(len(A))]))-(suA*suB)
    X = [d*d for d in A]
    X = n*sum(X)-(suA*suA)
    Y = [d*d for d in B]
    Y = n*sum(Y)-(suB*suB)
    X = Math.sqrt(X*Y)
    if (X==0):
    	return val1
    return val1/X



def perf(data, gpa):
	df = pd.DataFrame(data)
	diff = 1
	index = 0
	for i in range(5):
		v = np.array(df.loc[i])
		val = r(v,gpa)
		val = abs(val)
		if 1-val<diff:
			diff = 1-val;
			index = i+1
	return index




t = int(raw_input().strip())
for i in range(t):
	c = int(raw_input().strip())
	gpa = map(float, raw_input().split(' '))
	data = []
	for j in range(5):
		val = map(float, raw_input().split(' '))
		data.append(val)
	print(perf(data, gpa))