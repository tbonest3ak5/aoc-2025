def inRange(zones, ind):
    for zone in zones:
        if ind >= zone[0] and ind <= zone[1]:
            return True

    return False

def main():
    file = open("input.txt", "r")
    all_lines = file.readlines()

    acc = 0
    maxm = 0

    pairs = []
    ings = []

    i = 0
    while i < len(all_lines):
        line = all_lines[i].strip()
        if line == "":
            i += 1
            break
        
        nums = line.split("-")
        pairs.append((int(nums[0]), int(nums[1])))
        maxm = max(maxm, int(nums[1]))
        i += 1

    while i < len(all_lines):
        line = int(all_lines[i])
        ings.append(line)
        i += 1
    
    # print(maxm)
    acc = 0

    pairs.sort()
    merged = []

    for start, end in pairs:
        if not merged or merged[-1][1] < start:
            merged.append([start, end])
        else:
            merged[-1][1] = max(end, merged[-1][1])
    
    for ing in ings:
        if (inRange(merged, ing)):
            acc += 1


    # psa = [0] * (maxm + 2)

    # for pair in pairs:
    #     # print(f"first: {pair[0]},   second: {pair[1]}")
    #     psa[pair[0]] += 1
    #     psa[pair[1] + 1] -= 1
    
    # for i in range(1, len(psa)):
    #     psa[i] += psa[i-1]

    # acc = 0
    # for ing in ings:
    #     if ing <= maxm and psa[ing] > 0:
    #         acc += 1
    
    print(acc)

if __name__ == "__main__":
    main()