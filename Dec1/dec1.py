
def solution1():

    maxCal = 0
    cursum = 0

    with open("input.txt", "r") as f:

        for i, l in enumerate(f):

            if l == "\n":
                maxCal = max(maxCal, cursum)
                cursum = 0
            else:
                cursum += int(l)

    return maxCal

def solution2():

    maxCal = [0,0,0]
    cursum = 0

    with open("input.txt", "r") as f:

        for l in f:

            if l == "\n":
                
                if min(maxCal) < cursum:
                    maxCal[maxCal.index(min(maxCal))] = cursum
                cursum = 0
            else:
                cursum += int(l)

    return sum(maxCal)

print(solution2())
