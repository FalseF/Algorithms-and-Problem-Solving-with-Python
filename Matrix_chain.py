def fun(p, n):
    dp = [[0 for i in range(n)]for i in range(n)]
    for i in range(1, n):
        dp[i][i] = 0
    for idx in range(1, n-1):
        for i in range(n-idx):
            dp[i][i+idx] = min(dp[i+1][i+idx] + p[i-1] * p[i] * p[i+idx],
                               dp[i][i+idx-1] + p[i-1] * p[i+idx-1] * p[i+idx]
                               )
    return dp[1][n-1]
siz = int(input())
arr = list(map(int,input().split()))
print("Minimum number of multiplications need: ", fun(arr, siz))