# Dynamic programming

Types of DP:

## 1.Knapsack Problem

find highest price for a given weights and price of items where we can include items whose sum is less than bag weight.  
Types of knampsack.

### 1.0/1

we can either include a item completely or exclude it.  
Base case is bag weight=0 or elementsInArray=0.  
the element is excluded if **element weight> basg weight**. Else the element is further underoes into two cases either _include it and move to next element or exclude and move to bext element_.  
The **max of the above two cases gives the maximum profit**.  
![tree, the tree for the problem](</home/anirudh/Documents/DP/images/knps(0,1).png>)

