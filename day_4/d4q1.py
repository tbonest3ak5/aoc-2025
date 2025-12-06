def main():
    file = open("input.txt", "r")
    all_lines = file.readlines()
    
    line_list = []

    acc = 0

    for line in all_lines:
        line = list(line.strip())
        line_list.append(line)

    w = len(line_list[0])
    h = len(line_list)

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
                    acc += 1
    
    print(acc)
                        
                        

if __name__ == "__main__":
    main()