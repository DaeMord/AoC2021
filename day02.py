#https://adventofcode.com/2021/day/2
from AoC import inputData

dataInput = inputData('data/day02.txt', t="rex", r="^([\w]+) (\d*)")
#dataInput = inputData('data/test02.txt', t="rex", r="^([\w]+) (\d*)")

def main():
    newData = {}
    output = {}
    forward = 0
    aim = 0
    depth = 0
    for idx in dataInput:
        newData.setdefault(idx[0], []).append(int(idx[1]))
        if idx[0] == "forward":
            forward += int(idx[1])
            depth = (int(idx[1]) * aim) + depth
        elif idx[0] == "down":
            aim += int(idx[1])
        elif idx[0] == "up":
            aim -= int(idx[1])
    for i in newData:
        output[i] = sum(newData[i])
    output["downtotal"] = output["down"] - output["up"]
    return output["forward"] * output["downtotal"], depth * forward


data = main()
answer1,answer2 = data[0],data[1]
print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)