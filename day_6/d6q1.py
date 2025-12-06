def main():
    file = open("input.txt", "r")
    all_lines = file.readlines()

    acc = 0

    number_lines = []
    opp_line = []

    i = 0
    while i < len(all_lines):
        line = all_lines[i].strip().split()

        if line[0][0] >= '0' and line[0][0] <= '9':
            number_lines.append(line)
        else:
            opp_line = line
            break
        i += 1
    
    for i in range(len(number_lines[0])):
        temp = 0
        opp = opp_line[i]
        if opp == "+":
            for j in range(len(number_lines)):
                temp += int(number_lines[j][i])
            acc += temp
        elif opp == "*":
            temp = 1
            for j in range(len(number_lines)):
                temp *= int(number_lines[j][i])
            acc += temp
    
    print(acc)

main()

