def problem15():
    grid = []
    for i in range(0, 21):
        grid.append([])
        if i == 0:
            grid[i] = [1] * 21
        else:
            for j in range(0, 21):
                if j == 0:
                    grid[i].append(1)
                else:
                    grid[i].append(grid[i][j-1] + grid[i-1][j])

    print(grid[20][20])

problem15()
