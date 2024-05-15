flowerbed1 = [1,0,0,0,1]        # T
n1 = 1
flowerbed2 = [1,0,0,0,1]        # F
n2 = 2
flowerbed3 = [0,1,0]            # F
n3 = 1
flowerbed4 = [1,0,0,0,0,1]      # F
n4 = 2
flowerbed5 = [1,0,0,0,1,0,0]    # T
n5 = 2
flowerbed6 = [0]                # T
n6 = 1
flowerbed7 = [1]                # T
n7 = 0
flowerbed8 = [0,0,1,0,0]        # T
n8 = 1


# Initial thought was to do a quick pure math check to see if it was even possible, but that 
# turned into more code than brute force checking would be. Although the other method could maybe be better for speed ups on larger lists. 
class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        planted = 0
        while planted < n:
            for i in range(len(flowerbed)):
                if planted == n:
                    return True
                if len(flowerbed) == 1:
                    if flowerbed[0] == 1 and n != 0:
                        return False
                    else:
                        return True
                else:
                    if i == 0:
                        if ( flowerbed[i] == 0 ) and ( flowerbed[i + 1] == 0 ):
                            flowerbed[i] = 1
                            planted += 1
                    elif i == ( len(flowerbed) - 1):
                        if ( flowerbed[i] == 1 or flowerbed[i - 1] == 1 ) and planted < n:
                            return False                       
                        elif ( flowerbed[i - 1] == 0 ) and ( flowerbed[i] == 0 ):
                            flowerbed[i] = 1
                            planted += 1
                    else: 
                        if ( flowerbed[i - 1] == 0 ) and ( flowerbed[i] == 0 ) and ( flowerbed[i + 1] == 0 ):
                            flowerbed[i] = 1
                            planted += 1
             
        return ( planted == n )

test = Solution()
print(test.canPlaceFlowers(flowerbed1, n1))
print(test.canPlaceFlowers(flowerbed2, n2))
print(test.canPlaceFlowers(flowerbed3, n3))
print(test.canPlaceFlowers(flowerbed4, n4))
print(test.canPlaceFlowers(flowerbed5, n5))
print(test.canPlaceFlowers(flowerbed6, n6))
print(test.canPlaceFlowers(flowerbed7, n7))
print(test.canPlaceFlowers(flowerbed8, n8))
