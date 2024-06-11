isConnected1 = [[1,1,0],[1,1,0],[0,0,1]]
isConnected2 = [[1,0,0],[0,1,0],[0,0,1]]


# Thoughts:
# this problem is very similar to 841 keys and rooms problem. 
# But instead of stoping at "unable to visit all rooms" you need 
# to restart the DFS at the next "unopened room". while somehow keeping 
# count of how many times you had to restart.
class Solution:
    def findCircleNum(self, cnx: list[list[int]]) -> int:
        res=0
        n=len(cnx)
        def dfs(i):
            cnx[i][i]=2
            for j in range(0,n):
                if cnx[i][j]==1:
                    cnx[i][j]=2
                    dfs(j)
        for i in range(0,n):
            if cnx[i][i]==1:
                res+=1
                dfs(i)
        return res
    
        

test = Solution()
print(test.findCircleNum(isConnected1))
print(test.findCircleNum(isConnected2))
                    

