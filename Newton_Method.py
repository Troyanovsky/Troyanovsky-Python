def newton_method(a):
    seq = [0,a]
    infunc = input('Input function(with x being the variable):    ')
    infuncp = input('''Input the first derivative of the function(with x being 
the variable):    ''')
    for n in range(2,101):
        seq.append(str(float(seq[n-1])-(float(eval(function(infunc,seq[n-1]))))/
(float(eval(functionp(infuncp,seq[n-1]))))))
    print ('Start:')
    for element in seq[1:]:
        print (element)
    print ('----------')

def function(func,sth):
    raw_func = list(func)
    for m,i in enumerate(raw_func):
        if i == 'x':
            raw_func[m] = sth
    return ''.join(raw_func)

def functionp(funcp,sth1):
    raw_funcp = list(funcp)
    for m1,i in enumerate(raw_funcp):
        if i == 'x':
            raw_funcp[m1] = sth1
    return ''.join(raw_funcp)

a1 = input('Input the first term of x:   ')
newton_method(a1)