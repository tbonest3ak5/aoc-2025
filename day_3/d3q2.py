
def main():
    file = open("input.txt", "r")
    all_lines = file.readlines()
    
    acc = 0

    for line in all_lines:
        line = line.strip()
        slen = len(line)
        lList = [0] * slen
        rList = [0] * slen
        tempArr = [0] * 12
        tempInds = [0] * 12

        lineSum = 0

        for dig in range(12):
            if dig == 0:
                tempD = int(line[0])
                tempInd = 0

                for ind in range(slen-12+dig, -1, -1):
                    if int(line[ind]) >= tempD:
                        tempD = int(line[ind])
                        tempInd = ind
                tempArr[dig] = tempD
                tempInds[dig] = tempInd
                # print(f"dig: {dig},  tempD: {tempD},  tempInd: {tempInd}")
            else:
                tempD = int(line[tempInds[dig-1]+1])
                tempInd = tempInds[dig-1]+1

                for ind in range(slen-12+dig, tempInds[dig-1], -1):
                    if int(line[ind]) >= tempD:
                        tempD = int(line[ind])
                        tempInd = ind
                tempArr[dig] = tempD
                tempInds[dig] = tempInd
                # print(f"dig: {dig},  tempD: {tempD},  tempInd: {tempInd}")

        for ind in range(12):
            lineSum += tempArr[ind] * (10 ** (11-ind))

        # print(f"line: {line},  line sum: {lineSum}")
        acc += lineSum
    
    print(acc)


if __name__ == "__main__":
    main()