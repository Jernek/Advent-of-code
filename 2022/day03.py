import string

with open("day03.txt", "r") as file: 
    Data = [line.strip('\n') for line in file]

Map = dict(zip(string.ascii_letters,range(1,len(string.ascii_letters)+1)))

def score(Intersection, Score): 
    for elemnt in Intersection:
        Score += Map.get(elemnt)
    return Score

def part1(Score = 0):
    for rucksack in Data:
        length = (len(rucksack)//2)
        Intersect = set(rucksack[:length]).intersection(rucksack[length:])
        Score = score(Intersect, Score)
    return Score

def part2(Score = 0):
    for x in range(0,len(Data),3):
        Intersect = (set(Data[x]) & set(Data[x+1]) & set(Data[x+2]))
        Score = score(Intersect, Score)
    return Score


if __name__ == "__main__":
    print(f"Answer for First Star: {part1()} \
         \nAnswer for Second Star: {part2()}")
