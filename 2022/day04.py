data = []
with open('day04.txt','r') as file: 
    Data =  file.read().split()
    for item, pair in enumerate(Data): 
        temp = ([line for line in Data[item].split(',')])
        data.append((list(map(int,temp[0].split('-'))), list(map(int,temp[1].split('-')))))


def part1(count = 0):
    for pair in data: 
        if pair[0][0] <= pair[1][0] and pair[0][1] >= pair[1][1]:
            count += 1
        elif pair[1][0] <= pair[0][0] and pair[1][1] >= pair[0][1]:
            count += 1 
    return count

def part2(count = 0):
    for pair in data: 
        if pair[0][0] <= pair[1][0] and pair[1][0] <= pair[0][1]:
            count += 1
        elif pair[1][0] <= pair[0][0] and pair[0][0] <= pair[1][1]:
            count += 1
    return count
    
if __name__== "__main__": 
    print(f"Answer to First Star: {part1()}\
          \nAnswer to Second Star: {part2()}")
    