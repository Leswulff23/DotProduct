'''
    Author: Leslie N. Kodjoe
    Assignment 1

'''
import random

N=10
A=[];
for i in range(1,N):
    fill =random.randint(1,1000) #takes numbers at random from 1 to N
    A.append(fill) # adds number picked to the list

B=[];
for j in range(1,N):
    fill2 =random.randint(1,1000) #takes numbers at random from 1 to N
    B.append(fill2) # adds number picked to the list



    
def DotProduct(N,A,B):
    product =0 #holds total number
    for i in range(N):
        product+= A[i]* B[i] #multiplies the index of A and B then adds to product
    return product           # repeats this process till the end of the loop

def main():
    answer = DotProduct(N,A,B)
    print(answer)



main()

