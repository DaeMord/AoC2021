#https://adventofcode.com/2021/day/3
from AoC import inputData

dataInput = inputData('data/day03.txt')
#dataInput = inputData('data/test03.txt')

def main():
    output = ""
    output2 = ""
    for i in range(len(dataInput[0])):
        count = 0
        for idx in dataInput:
            count += int(idx[i])
        if count > len(dataInput) / 2:
            output = output + str(1)
            output2 = output2 + str(0)
        else:
            output = output + str(0)
            output2 = output2 + str(1)
    return int(output, 2) * int(output2, 2)

def checkPos(inputArray, pos, chk):
    lst = []
    outputArray = []
    if len(inputArray)>1:
        for num in inputArray:
            lst.append(num[pos])
        if lst.count(chk) > len(inputArray) / 2:
            chkval = "1"
        elif lst.count(chk) == len(inputArray) / 2:
            chkval = chk
        else:
            chkval = "0"
        for i in inputArray:
            if i[pos] == chkval:
                outputArray.append(i)
    else:
        outputArray = inputArray
    return outputArray


def main2():
    inputArray = dataInput
    for i in range(len(dataInput[0])):
        inputArray = checkPos(inputArray, i, "1")
    inputArray2 = dataInput
    for i in range(len(dataInput[0])):
        inputArray2 = checkPos(inputArray2, i, "0")
    return int(inputArray[0], 2) * int(inputArray2[0], 2)


data = main()
data2 = main2()
answer1 = data
answer2 = data2
print("Answer 1")
print(answer1)
print("Answer 2")
print(answer2)