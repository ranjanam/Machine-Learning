#https://www.hackerrank.com/challenges/computing-the-correlation/problem
 
import math as Math 
def corr(A,B):
    n = len(A)
    suA = sum(A)
    suB = sum(B)
    val1 = n*(sum([A[i]*B[i] for i in range(len(A))]))-(suA*suB)
    X = [d*d for d in A]
    X = n*sum(X)-(suA*suA)
    Y = [d*d for d in B]
    Y = n*sum(Y)-(suB*suB)
    X = Math.sqrt(X*Y)
    return val1/X

def cal(l1,l2,l3):
    a = corr(l1,l2)
    b = corr(l2,l3)
    c = corr(l1,l3)
    return a,b,c


data = []
t = int(raw_input().strip())    
l1 = []
l2 = []
l3 = []
for i in range(t):
    data = map(int, raw_input().split('\t'))
    l1.append(data[0])
    l2.append(data[1])
    l3.append(data[2])

a,b,c = cal(l1,l2,l3)
print("{:.2f}".format(a))
print("{:.2f}".format(b))
print("{:.2f}".format(c))

