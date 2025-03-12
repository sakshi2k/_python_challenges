# https://leetcode.com/problems/rotting-oranges/

class Solution(object):

    def find_all_rotten(self, grid, m, n):
        res = []
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    res.append((i, j))

        return res
    
    def check_and_enqueue(self, grid, q, i, j, m, n):
        if i >= 0 and i < m and j >= 0 and j < n:
            if (i, j) not in q and grid[i][j] == 1:
                q.append((i, j))
                grid[i][j] = 2
                return True
        
        return False

    def any_orange_still_good(self, grid, m, n):
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    return True

        return False


    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        res = self.find_all_rotten(grid, m, n)

                
        if len(res) == 0:
            if self.any_orange_still_good(grid, m, n):
                return -1
            return 0


        count = -1

        q = []
        v = []

        for (a,b) in res:
            q.append((a,b))

        while len(q) != 0:
            for _ in q:
                # dequeue 
                curr = q[0]
                q = q[1:]
                if curr not in v:
                    v.append(curr)
                    i, j = curr
                    self.check_and_enqueue(grid, q, i+1, j, m, n)
                    self.check_and_enqueue(grid, q, i, j+1, m, n)
                    self.check_and_enqueue(grid, q, i-1, j, m, n)
                    self.check_and_enqueue(grid, q, i, j-1, m, n)
            count += 1

        if self.any_orange_still_good(grid, m, n):
            return -1

        return count

if __name__ == '__main__':
    s = Solution()

    grid_1 = [[2,1,1],[1,1,0],[0,1,1]]
    grid_2 = [[2,1,1],[0,1,1],[1,0,1]]
    grid_3 = [[0,2]]
    grid_4 = [[2,1,1],[1,1,1],[0,1,2]]
    grid_5 = [[0]]
    grid_6 = [[0], [0]]
    grid_7 = [[1]]
    grid_8 = [[1], [0]]
    grid_9 = [[1], [1]]

    print(s.orangesRotting(grid_1))
    print(s.orangesRotting(grid_2))
    print(s.orangesRotting(grid_3))
    print(s.orangesRotting(grid_4))
    print(s.orangesRotting(grid_5))
    print(s.orangesRotting(grid_6))
    print(s.orangesRotting(grid_7))
    print(s.orangesRotting(grid_8))
    print(s.orangesRotting(grid_9))


    print(" -- END OF PROGRAM --")