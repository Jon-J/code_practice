class Solution:
    # @return an integer
    def numTrees(self, n):
        if n==1: return 1
        if n==2: return 2
        num=0
        for i in range(1,n+1):
            num=num+self.numTrees(i-1)+self.numTrees(n-i)
        return num
 
    def numTrees2(self, n):
        if n==1: return 1
        if n==2: return 2
        dp=[0 for i in range(n+1)]
        dp[0]=1;dp[1]=1;dp[2]=2
        for i in range(3,n+1):
            for j in range(1,i):
                dp[i]+=dp[j-1]*dp[i-j]
        return dp[n]
