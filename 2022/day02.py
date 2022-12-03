with open("day02.txt", "r") as file: 
    Data = [line.splitlines() for line in file]

def part1(Score = 0):
    Map = {"X":("C","B",1), "Y":("A","C",2), "Z":("B","A",3)}
    for game in Data: 
        opponent = game[0][0]
        pick = game[0][-1]
        if Map.get(pick)[0] == opponent:    # Win
            Score += 6 + Map.get(pick)[-1]
        elif Map.get(pick)[1] == opponent:  # Lose
            Score += Map.get(pick)[-1]
        else:                               # Draw
            Score += 3 + Map.get(pick)[-1] 
    return Score

def part2(Score = 0): 
    Map = {"X":{"A":3, "B":1, "C":2},
       "Y":{"A":1+3, "B":2+3, "C":3+3},
       "Z":{"A":2+6, "B":3+6, "C":1+6}}
    for game in Data: 
        Score += Map.get(game[0][-1]).get(game[0][0])
    return Score 


if __name__ == "__main__":
    print(f"Answer for First Star: {part1()} \
          \nAnswer for Second Star: {part2()}")

