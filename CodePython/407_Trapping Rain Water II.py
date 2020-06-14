class Solution:
    def trapRainWater(self, heightMap):

        #从四周边界开始，每次找最矮的柱子
        #遍历其四周，如果在边界内，且高度小于最矮的柱子，则一定会积水。
        import heapq
        if len(heightMap)==0:
            return 0
        rows, cols = len(heightMap), len(heightMap[0])
        visited = [[False]*cols for _ in range(rows)]
        min_heap = []
        for i in range(cols):
            heapq.heappush(min_heap, (heightMap[0][i], (0,i)))
            heapq.heappush(min_heap, (heightMap[rows-1][i], (rows-1,i)))
            visited[0][i] = True
            visited[rows-1][i] = True
        for i in range(rows):
            heapq.heappush(min_heap, (heightMap[i][0], (i,0)))
            heapq.heappush(min_heap, (heightMap[i][cols-1], (i,cols-1)))
            visited[i][0] = True
            visited[i][cols-1] = True
        ans = 0
        dx = [-1, 0, 1, 0]
        dy = [0, -1, 0, 1]
        while min_heap:
            heigh, pos = heapq.heappop(min_heap)
            for i in range(4):
                x, y = pos[0]+dx[i], pos[1]+dy[i]
                if 0<=x<rows and 0<=y<cols and not visited[x][y]:
                    visited[x][y] = True
                    ans += max(0, heigh-heightMap[x][y])
                    heapq.heappush(min_heap, (max(heightMap[x][y], heigh), (x,y)))
        return ans

        # #方法1：计算每个柱子上方积水高度
        # if len(heightMap)==0:
        #     return 0
        # rows, cols = len(heightMap), len(heightMap[0])
        # dp_left = [[0]*cols for _ in range(rows)]
        # dp_right = [[0]*cols for _ in range(rows)]
        # dp_up = [[0]*cols for _ in range(rows)]
        # dp_down = [[0]*cols for _ in range(rows)]
        # for c in range(1, cols):
        #     for r in range(rows):
        #         dp_left[r][c] = max(dp_left[r][c-1], heightMap[r][c-1])
        # for c in range(cols-2, -1, -1):
        #     for r in range(rows-1, -1, -1):
        #         dp_right[r][c] = max(dp_right[r][c+1], heightMap[r][c+1])
        # for r in range(1, rows):
        #     for c in range(cols):
        #         dp_up[r][c] = max(dp_up[r-1][c], heightMap[r-1][c])
        # for r in range(rows-2, -1, -1):
        #     for c in range(cols-1, -1, -1):
        #         dp_down[r][c] = max(dp_down[r+1][c], heightMap[r+1][c])
        # ans = 0
        # for r in range(1, rows-1):
        #     for c in range(1, cols-1):
        #         heigh = min(dp_left[r][c], dp_right[r][c], dp_down[r][c], dp_up[r][c])
        #         ans += max(0, heigh-heightMap[r][c])
        # return ans

s = Solution()
heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
#heightMap = [[12,13,1,12],[13,4,13,12],[13,8,10,12],[12,13,12,12],[13,13,13,13]]
print(s.trapRainWater(heightMap))