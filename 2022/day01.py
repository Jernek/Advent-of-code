def get_Data(data = []):
    with open('day01.txt', 'r') as file:
        Data = file.read().split('\n\n')
        for groups in Data: 
            data.append([int(item) for item in groups.splitlines()])
    return data

def part1(Input):
    return max(Input)

def part2(Input): 
    return sum(sorted(Input)[-3:])


if __name__ == "__main__":
    data = get_Data()
    Input = [sum(vector) for vector in data]
    print(f"Anwser for First Star: {part1(Input)} cal.\
        \nAnswer for Second Star: {part2(Input)} cal.")
