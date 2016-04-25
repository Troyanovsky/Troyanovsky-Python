# antoine_constants = {'CCL4':{'a':6.89410,'b':1219.580,'c':227.170},
# 'H2O':{'a':8.0731,'b':1730.63,'c':233.426},
# 'CO2':{'a':9.8106,'b':1347.79,'c':273.0},
# 'CO':{'a':6.2402,'b':230.27,'c':260.01},
# 'CF4':{'a':6.97230,'b':540.500,'c':260.100},
# 'C2H4O2':{'a':7.38782,'b':1533.313,'c':222.309},
# 'NH3':{'a':7.55466,'b':1002.711,'c':247.885},
# 'C6H6':{'a':6.89272,'b':1203.531,'c':219.888},
# 'C2H6O':{'a':8.11220,'b':1592.864,'c':226.184},
# 'CH3OH':{'a':8.08097,'b':1582.271,'c':239.726},
# 'C3H6O':{'a':7.11714,'b':1210.595,'c':229.664},
# 'N2':{'a':255.68,'b':266.55,'c':63.20},
# 'O2':{'a':3.81634,'b':319.01,'c':266.697},
# 'C3H8':{'a':3.92828,'b':803.997,'c':247.04},
# 'C4H10':{'a':3.93266,'b':935.773,'c':238.789}
# }

def get_Pressure(antoine_constants, called, t):
    const_a = antoine_constants[called]['a']
    const_b = antoine_constants[called]['b']
    const_c = antoine_constants[called]['c']
    mini = antoine_constants[called]['min']
    maxi = antoine_constants[called]['max']
    if t > mini and t < maxi:
        print ('--------\n','{0} at'.format(called),t,'Celsius')
        print ('Vapor pressure = ',10**(const_a-(const_b/(const_c+t))),'mmHg')
        print ('--------')
    else:
        print ('Sorry, out of range.')

def get_Chart(antoine_constants, called):
    const_a = antoine_constants[called]['a']
    const_b = antoine_constants[called]['b']
    const_c = antoine_constants[called]['c']
    mini = antoine_constants[called]['min']
    maxi = antoine_constants[called]['max']
    chem_name = antoine_constants[called]['chemical name']
    chrt = print ('\nVapor pressure chart of {0} ({1}) from {2} Celsius to {3} Celsius'.format(called,chem_name, mini, maxi))
    t = mini
    while t <= maxi:
        print ('--------\n',t,'Celsius')
        print ('vapor pressure = ',10**(const_a-(const_b/(const_c+t))),'mmHg')
        t += 1
