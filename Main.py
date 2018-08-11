
import random
import time
import Jumbling_Char
import JumbDec_Test
from P1 import division
import timeit
ency_total_time = 0
file = division()
start_time = timeit.default_timer()
for key,chunk in file.items():
    for line in chunk:
        rl = Jumbling_Char.length
        '''Adding characters from character set'''

        JumbledCVV = Jumbling_Char.JumblingBlock(line,rl)

        '''Salting'''
        CurrDate = str(time.strftime('%Y%m%d'))
        CurrTime = str(time.strftime('%H%M%S'))
        SaltedLINE = JumbledCVV+CurrDate+CurrTime

        print('\n')
        print('Salted string: ',SaltedLINE)
        print('\n')

        SLINE = SaltedLINE

        print('Encrypted string: ', SLINE)
        print('\n')
        line_time = timeit.default_timer()-start_time
        ency_total_time = ency_total_time + line_time

        startdec = timeit.default_timer()
        DSL=list(SLINE)

        u=JumbDec_Test.RevJumblingBlock(DSL,rl)
        print('Time for decrpytion: ',timeit.default_timer()-startdec)
        print('\n')

print("Total time for encryption", ency_total_time)
print('\n')
