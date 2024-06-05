rooms1 = [[1],[2],[3],[]] #True
rooms2 = [[1,3],[3,0,1],[2],[0]] #False







class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        visited = set()
        def dfs(room):
            visited.add(room)
            for key in rooms[room]:
                if key not in visited:
                    dfs(key)
        dfs(0)
        return len(visited) == len(rooms)


test = Solution()
print(test.canVisitAllRooms(rooms1))
print(test.canVisitAllRooms(rooms2))