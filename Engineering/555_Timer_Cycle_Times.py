import math
from sigfig import round

while(True):
    r1 = eval(input('R1: '))
    r2 = eval(input('R2: '))
    c1 = eval(input('C1: '))
    td = r2*c1*math.log(2)
    tc = (r1+r2)*c1*math.log(2)
    print(f'Td = {round(td, sigfigs=3)}')
    print(f'Tc = {round(tc, sigfigs=3)}')
    print('The following don\'t actually include the initial charge time')
    print(f'state after 5 minutes: {round(300%(td+tc), sigfigs=3)}')
    print(round(td, sigfigs=3),
          round(td + tc, sigfigs=3),
          round(td + tc + td, sigfigs=3),
          round(td + tc + td + tc, sigfigs=3))
    print()
