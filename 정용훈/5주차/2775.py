T = int(input())


for _ in range(T):
  k = int(input())
  n = int(input())
  
  dp = [[0 for _ in range(n+1)] for _ in range(k+1)]  # ���� 0���� �ʱ�ȭ
  for i in range(n+1):                                # 0�� i ȣ i ������ �Ҵ�
    dp[0][i] = i


  for i in range(1,k+1):                              # k�� nȣ = (k-1)�� nȣ + k�� (n-1)ȣ
    for j in range(1,n+1):
      dp[i][j] = dp[i-1][j] + dp[i][j-1]
    
  print(dp[k][n])
  