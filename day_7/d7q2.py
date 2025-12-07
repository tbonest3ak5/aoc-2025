def main():
    file = open("paths.txt", "r")
    str_lines = file.readlines()

    all_lines = []
    for line in str_lines:
        all_lines.append(list(line.strip()))

    w = len(all_lines[0])
    h = len(all_lines)
    ret = -1

    dp = [[-1 for _ in range(w)] for _ in range(h+1)]

    for col in range(w):
        if all_lines[0][col] == 'S':
            ret = dfs(all_lines, 1, col, dp)
            break
    print(ret)


def dfs(grid, row, col, dp):
    h = len(grid)

    print(f"row: {row}, col: {col}")
    if dp[row][col] != -1:
        return dp[row][col]

    if row == h-1:
        return 1
    if grid[row][col] == '^':
        value = dfs(grid, row, col-1, dp) + dfs(grid, row, col+1, dp)
        dp[row][col] = value
        return value
    elif grid[row][col] == '|':
        value = dfs(grid, row+1, col, dp)
        dp[row][col] = value
        return value
    else:
        print("unlucky :(")
    
main()