from time import perf_counter as timer

def get_Data():
    data = []
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
    t0 = timer()
    for i in range(1000):
        data = get_Data()
        Input = [sum(vector) for vector in data]
        part1(Input)
        part2(Input)
    t1 = timer()-t0
    print(f"Code runs on: {t1} ms \nAnwser for First Star: {part1(Input)} cal.\
            \nAnswer for Second Star: {part2(Input)} cal.")
