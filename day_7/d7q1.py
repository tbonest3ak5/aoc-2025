def main():
    file = open("input.txt", "r")
    str_lines = file.readlines()

    all_lines = []
    for line in str_lines:
        all_lines.append(list(line.strip()))

    acc = 0

    w = len(all_lines[0])

    for i in range(len(all_lines)):
        line = all_lines[i]
        if i%2 == 0:
            if i ==0:
                for j in range(w):
                    if line[j] == 'S':
                        all_lines[1][j] = '|'
                        break
            else:
                for j in range(w):
                    if line[j] == '^' and all_lines[i-1][j] == '|':
                        acc += 1
                        all_lines[i][j-1] = '|'
                        all_lines[i][j+1] = '|'
                    elif line[j] == '.' and all_lines[i-1][j] == '|':
                        all_lines[i][j] = '|'
        else:
            for j in range(w):
                if all_lines[i-1][j] == '|':
                    all_lines[i][j] = '|'
    
    print(acc)
    
    # for debug and part 2
    filename = "paths.txt"
    with open(filename, 'w') as file:
        for line in all_lines:
            file.write("".join(line) + '\n') 

    

main()