def get_Data():
    data = []
    with open('day01.txt', 'r') as file:
        Data = file.read().split('\n\n')
        for groups in Data: 
            data.append([int(item) for item in groups.splitlines()])
    return data


def part1(p1_Data):
    Solution_1 = max([sum(vector) for vector in p1_Data])
    return Solution_1

def part2(p2_Data): 
    Solution2 = [sum(vector) for vector in p2_Data]
    return (sum(sorted(Solution2)[-3:]))


if __name__ == "__main__":
    data = get_Data()
    print(f"Solution to First star: {part1(data)}")
    print(f"\nSolution to Second star: {part2(data)}")