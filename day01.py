#https://adventofcode.com/2021/day/1
from AoC import inputData

dataInput = inputData('data/day01.txt', t="int")
#dataInput = inputData('data/test01.txt', t="int")

def main():
    up = 0
    down = 0
    threeup = 0
    for i in range(1, len(dataInput)):
        if dataInput[i] > dataInput[i-1]:
            #print(dataInput[i-1], dataInput[i], "increase")
            up += 1
        elif dataInput[i] < dataInput[i-1]:
            #print(dataInput[i-1], dataInput[i], "decrease")
            down += 1
        else:
            print("ERROR")
        if(len(dataInput[i:i+3]) == 3):
            if (sum(dataInput[i-1:i+2]) < sum(dataInput[i:i+3])):
                #print(sum(dataInput[i:i+3]),sum(dataInput[i-1: i+2]))
                threeup += 1
    return up, threeup

data = main()
answer1,answer2 = data[0],data[1]
print("Answer 1")
print(answer1)
#1399 low
print("Answer 2")
print(answer2)