

def main():
    file = open("input.txt", "r")
    all_lines = file.readlines()
    
    acc = 0

    for line in all_lines:
        line = line.strip()
        # lList: largest number in list left of and including current ind
        # rList: largest number in list right of current ind
        slen = len(line)
        lList = [0] * slen
        rList = [0] * slen

        for i in range(slen):
            if i == 0:
                lList[i] = int(line[i])
            else: 
                lList[i] = max(lList[i-1], int(line[i]))
        
        for i in range(slen-2, -1, -1):
            if i == slen-2:
                rList[i] = int(line[i+1])
            else:
                rList[i] = max(rList[i+1], int(line[i+1]))
        jolt = 0
        for i in range(slen-1):
            temp = 10 * lList[i] + rList[i]
            jolt = max(jolt, temp)
        
        print(f"line: {line} ,     jolt: {jolt}")
        acc += jolt
    
    print(acc)      

if __name__ == "__main__":
    main()
