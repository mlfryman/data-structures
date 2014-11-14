__author__ = 'Melanie'

def radix_sort(unSortedList):
    maxCipher = len(unSortedList)
    mod = 10
    div = 1

    while True:
        sortedList = [list() for i in range(mod)]

        for val in unSortedList:
            least_digit = val % mod
            least_digit //= div
            sortedList[least_digit].append(val)
        #mod = mod * 10
        #div = div * 10

        if len(sortedList[0]) == maxCipher:
            return sortedList[0]
        unSortedList = []
        for x in sortedList:
            for y in x:
                unSortedList.append(y)
        return sortedList

data = [ 2, 10, 111, 565, 800 ]
print(radix_sort(data))

pass