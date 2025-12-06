def get_blank_cols(number_lines):
    w = len(number_lines[0])
    h = len(number_lines)

    ret = []
    for col in range(w):
        emp = True
        for i in range(h):
            if number_lines[i][col] != ' ':
                emp = False
                break
        if emp:
            ret.append(col)
    
    return ret

def num_from_col(number_lines, col):
    acc = 0
    exp = 0
    for i in range(len(number_lines)-1, -1, -1):
        ch = number_lines[i][col]
        if ch != ' ':
            dig = int(ch)
            acc += dig * (10 ** exp)
            exp += 1

    return acc

def main():
    file = open("input.txt", "r")
    all_lines = file.readlines()

    acc = 0

    number_lines = []
    op_line = []

    for i in range(len(all_lines)):
        line = all_lines[i].strip("\n")

        if line[0][0] != '+' and line[0][0] != '*':
            number_lines.append(line)
        else:
            op_line = line.split()
            break

    breaks = get_blank_cols(number_lines)

    prev = -1
    for i in range(len(breaks)+1):
        op = op_line[i]
        end = 0
        if i == len(breaks):
            end = len(number_lines[0])
        else:
            end = breaks[i]
        
        j = prev +1

        nums = []
        while j < end:
            nums.append(num_from_col(number_lines, j))
            j += 1
        
        if op == '+':
            temp = 0
            for num in nums:
                temp += num
            acc += temp
            
        elif op == '*':
            temp = 1
            for num in nums:
                temp *= num
            acc += temp

        prev = end
    
    print(acc)

main()

