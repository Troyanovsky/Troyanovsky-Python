import random

def deMeresProblem(t):
    fourOdd = 0
    twentyFourOdd = 0
    for trial in range(t):
        if throwFour() == True:
            fourOdd += 1
        if throwTwentyFour() == True:
            twentyFourOdd += 1
    if fourOdd/t > twentyFourOdd/t:
        return True

def throwFour():
    for roll in range(4):
        if random.randint(1,6) == 6:
            return True
    return False

def throwTwentyFour():
    for roll in range(24):
        if random.randint(1,6) == 6 and random.randint(1,6) == 6:
            return True
    return False

#http://www.cs.cmu.edu/~112/notes/notes-recursion-part1.html
def gcd(x, y):
    if (y == 0): return x
    else: return gcd(y, x%y)

def randomCoprimeOdds(t):
    success = 0
    for trial in range(t):
        if gcd(random.randint(2,1000000000),random.randint(2,1000000000)) == 1:
            success += 1
    return success/t

print(randomCoprimeOdds(9999))