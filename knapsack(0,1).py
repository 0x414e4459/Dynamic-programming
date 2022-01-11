print('enter bag weight: ',end='')
bag_weight=int(input())
print('enter number of elements in array:  ',end='')
n=int(input())
print('enter the weights: ',end='')
w=[int(i) for i in input().split()]
print('enter the prices: ',end='')
p=[int(i) for i in input().split()]
memo=[[-1 for x in range(bag_weight+1)]for y in range(n+1)]

def knapsack_dp(w,p,bw,n):        #dp using memmoisation 
    if(n==0  or bw==0):
        return 0
    if(memo[n][bw]!=-1):
        return memo[bw][n]
    else:
        res=0
        if(bw<w[n]):           #skip the element if element weigh>bag weight
            res=knapsack_dp(w,p,bw,n-1)
        else:              # max of price+fun(next_element) and fun(next_element)
            res= max(knapsack_dp(w,p,bw,n-1),p[n]+knapsack_dp(w,p,(bw-w[n]),n-1))
        memo[n][bw]=res
        return res
    
def knapsack_rec(w,p,bw,n):          #recursive approach
    if(n==0 or bw==0):
        return 0
    if(bw<w[n]):           #skip the element if element weigh>bag weight
        return knapsack_rec(w,p,bw,n-1)
    else:              # max of price+fun(next_element) and fun(next_element)
        return max(knapsack_rec(w,p,bw,n-1),p[n]+knapsack_rec(w,p,bw-w[n],n-1))


dp=knapsack_dp(w,p,bag_weight,n-1)
rec=knapsack_rec(w,p,bag_weight,n-1)
print(dp)
print(rec)