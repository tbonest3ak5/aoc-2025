def main():
    file = open("input.txt", "r")
    all_lines = file.readlines()
    
    line_list = []

    acc = 0

    for line in all_lines:
        line = list(line.strip())
        line_list.append(line)

    # w = len(line_list[0])
    # h = len(line_list)

    while True:
        new_line_list, change = remove_rolls(line_list)
        if change == 0:
            break
        line_list = new_line_list
        acc += change
    
    print(acc)
                        

def remove_rolls(line_list):
    w = len(line_list[0])
    h = len(line_list)

    change = 0

    for i in range(h):
        for j in range(w):
            if line_list[i][j] == '@':
                temp = 0
                if i > 0:
                    if line_list[i-1][j] == '@':
                        temp += 1
                    if j > 0 and line_list[i-1][j-1] == '@':
                        temp += 1
                    if j < w-1 and line_list[i-1][j+1] == '@':
                        temp += 1

                if j > 0 and line_list[i][j-1] == '@':
                    temp += 1
                if j < w-1 and line_list[i][j+1] == '@':
                    temp += 1
                
                if i < h-1:
                    if line_list[i+1][j] == '@':
                        temp += 1
                    if j > 0 and line_list[i+1][j-1] == '@':
                        temp += 1
                    if j < w-1 and line_list[i+1][j+1] == '@':
                        temp += 1
                
                if temp < 4:
                    change += 1
                    line_list[i][j] = '.'
        
    return line_list, change
                        

if __name__ == "__main__":
    main()