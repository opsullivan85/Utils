import math

while(True):
    r1 = eval(input('R1: '))
    r2 = eval(input('R2: '))
    c1 = eval(input('C1: '))
    td = r2*c1*math.log(2)
    tc = (r1+r2)*c1*math.log(2)
    print(f'Td = {td}')
    print(f'Tc = {tc}')
    print(300%(td+tc))
