'''Given two strings, S1 and S2, the task is to find the length of the Longest Common Subsequence, 
i.e. longest subsequence present in both of the strings. '''
#Using Bottom-up (Tabulation approach)
def longest_common_subsequence(X, Y):
    m, n = len(X), len(Y)

   
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j - 1] + 1 if X[i - 1] == Y[j - 1] else max(dp[i - 1][j], dp[i][j - 1])

    i, j, lcs = m, n, []
    while i > 0 and j > 0:
        if X[i - 1] == Y[j - 1]:
            lcs.append(X[i - 1])
            i, j = i - 1, j - 1
        elif dp[i - 1][j] > dp[i][j - 1]:
            i -= 1
        else:
            j -= 1

    return "".join(reversed(lcs))


X = "STRING"
Y = "RING"
result = longest_common_subsequence(X, Y)
print("Longest Common Subsequence:", result)
print("Length of LCS:", len(result))
