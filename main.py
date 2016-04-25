import timeit

start = timeit.default_timer()

sum = 0
x = 1
while x <= 100:
    sum = sum + 1/(2*x)+3/(x*(x+5))
    x = x + 1
print ('%.4f' % sum)

sum = 0
for x in range(1,101):
    sum += 1/(2*x)+3/(x*(x+5))
print ('%.4f' % sum)

print('---------------Run Time--------------')
stop = timeit.default_timer()

print (stop - start)