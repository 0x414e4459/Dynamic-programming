print('enter bag weight: ',end='')
bag_weight=int(input())
print('enter number of elements in array:  ',end='')
n=int(input())
print('enter the weights: ',end='')
w=[int(i) for i in input().split()]
print('enter the prices: ',end='')
p=[int(i) for i in input().split()]

def knapsack(w,p,bw,n):
    if(n==0 or bw==0):
        return 0
    if(bw<w[n]):
        return knapsack(w,p,bw,n-1)
    else:
        return max(knapsack(w,p,bw,n-1),p[n]+knapsack(w,p,bw-w[n],n-1))

pro=knapsack(w,p,bag_weight,n-1)
print(pro)