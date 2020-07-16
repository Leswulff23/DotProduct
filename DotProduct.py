'''
    Author: Leslie N. Kodjoe
    Assignment 1

'''
import random

N=10
A=[];
for i in range(1,N):
    fill =random.randint(1,1000)
    A.append(fill)

B=[];
for j in range(1,N):
    fill2 =random.randint(1,1000)
    B.append(fill2)



    
def DotProduct(N,A,B):
    product =0
    for i in range(len(A)):
        product+= A[i]* B[i]
    return product

def main():
    answer = DotProduct(N,A,B)
    print(answer)



main()

