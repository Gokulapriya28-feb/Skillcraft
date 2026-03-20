grid = [
[5,3,0,0,7,0,0,0,0],
[6,0,0,1,9,5,0,0,0],
[0,9,8,0,0,0,0,6,0],
[8,0,0,0,6,0,0,0,3],
[4,0,0,8,0,3,0,0,1],
[7,0,0,0,2,0,0,0,6],
[0,6,0,0,0,0,2,8,0],
[0,0,0,4,1,9,0,0,5],
[0,0,0,0,8,0,0,7,9]
]

def valid(grid, r, c, n):
    for i in range(9):
        if grid[r][i] == n or grid[i][c] == n:
            return False

    sr = r - r % 3
    sc = c - c % 3

    for i in range(3):
        for j in range(3):
            if grid[sr+i][sc+j] == n:
                return False

    return True


def solve(grid):
    for r in range(9):
        for c in range(9):
            if grid[r][c] == 0:

                for n in range(1, 10):
                    if valid(grid, r, c, n):
                        grid[r][c] = n

                        if solve(grid):
                            return True

                        grid[r][c] = 0

                return False
    return True


solve(grid)

for row in grid:
    print(row)
