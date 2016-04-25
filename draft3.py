import copy
def sumOfOdds(n):
    if n < 10:
        if n % 2 != 0:
            return n
        else:
            return 0
    else:
        if (n % 10) % 2 != 0:
            return n % 10 + sumOfOdds(n//10)
        else:
            return sumOfOdds(n//10)

def bubbleSort(L, swapped = False, index = 0):
    L = copy.deepcopy(L)
    if len(L) < 2:
        return L
    else:
        if index < len(L) - 1:
            if L[index+1] < L[index]:
                swapped = True
                L[index],L[index+1] = L[index+1],L[index]
            return bubbleSort(L,swapped,index+1)
        else:
            if swapped == False:
                return L
            else:
                return bubbleSort(L)


