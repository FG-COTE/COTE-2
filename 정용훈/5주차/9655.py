# -*- coding: utf-8 -*-
N = int(input())

dp = [-1 for _ in range(N+1)]

dp[0] = 0
dp[1] = 1
dp[2] = 2
dp[3] = 1

## dp로 풀려했으나 Top-Down 재귀 : 런타임 에러 
##def game(n):
##  if dp[n] != -1 : return dp[n]
##  else :
##    if n >= 3 : 
##      dp[n] = game(n-3) + game(n-(n-3))
##      return dp[n]
    
##winner = game(N)

##if winner%2 == 0:
##  print("CY")
##else:
##  print("SK")
##
  
for i in range(4,N+1):
    dp[i] = dp[(i//3)] + dp[(i%3)]

if dp[N]%2 == 0:
    print("CY")
else:
    print("SK")