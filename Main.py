
import random
import time
import Jumbling_Char
import JumbDec_Test
from P1 import division
import timeit
# import xlwt
# from xlwt import Workbook
import xlsxwriter

def encryption(file,start_time):
    ency_total_time = 0
    encrypted_file = {}
    for key, chunk in file.items():

        for line in chunk:
            rl = Jumbling_Char.length
            Jumbledline = Jumbling_Char.JumblingBlock(line, rl)

            '''Salting'''
            CurrDate = str(time.strftime('%Y%m%d'))
            CurrTime = str(time.strftime('%H%M%S'))
            SaltedLINE = Jumbledline + CurrDate + CurrTime

            SLINE = SaltedLINE

            encrypted_file.update({key: SLINE})

            line_time = timeit.default_timer() - start_time
            ency_total_time = ency_total_time + line_time

    return(encrypted_file,SLINE,rl,ency_total_time)


def decryption(encrypted_file,SLINE,rl):
    decrypted_file = {}
    total_dec = 0
    # decryption
    startdec = timeit.default_timer()
    decryted_file = {}
    for key, chunk in encrypted_file.items():
        DSL = list(SLINE)

        u = JumbDec_Test.RevJumblingBlock(DSL, rl)
        dec_time = timeit.default_timer() - startdec

        total_dec = total_dec + dec_time

        decrypted_file.update({key: u})
    return (total_dec)

def main ():
    workbook = xlsxwriter.Workbook('JSE.xlsx')
    sheet1 = workbook.add_worksheet()
    sheet2 = workbook.add_worksheet()
    sheet1.write(0, 1, 'CHUNK SIZE')
    sheet1.write(0, 2, 'PLAINTEXT SIZE')
    sheet1.write(0, 3, 'CIPHER TEXT SIZE')
    sheet1.write(0, 4, 'ENCRYPTION TIME ')
    sheet1.write(0, 5, 'DECRYPTION TIME')
    sheet1.write(0, 6, 'THROUGHPUT')
    row = 0
    for k in range(1,500,2):
        file = division(ch_line=k)
        start_time = timeit.default_timer()
        u, v, x,tim = encryption(file, start_time)
        dec = decryption(u, v, x)
        row = row + 1

        for did in range(0,6):
            if did == 0:
                sheet1.write(row, 1, k)
            elif did == 2:
                sheet1.write(row, 2, "plaintext size")
            elif did == 3:
                sheet1.write(row, 3, "ciphertext size")
            elif did == 4:
                sheet1.write(row, 4,tim)
            elif did == 5:
                sheet1.write(row, 5, dec)
            else:
                sheet1.write(row, 6, dec + tim)

    chart = workbook.add_chart({'type': 'line'})
    chart.add_series({'name': '=Sheet1!$G$1','values': '=Sheet1!$G$2:$G$250'})
    chart.add_series({'name': '=Sheet1!$F$1', 'values': '=Sheet1!$F$2:$F$250'})
    chart.add_series({'name': '=Sheet1!$E$1', 'values': '=Sheet1!$E$2:$E$250'})
    sheet1.insert_chart('C1', chart)
    chart.set_title({'name': 'Throughput with increase in chunk size'})
    chart.set_x_axis({'name': 'Chunk Size', })
    chart.set_y_axis({'name': 'Throughput', })
    workbook.close()

    # multiple file size

    sheet2.write(0, 1, 'FILE SIZE')
    sheet2.write(0, 2, 'CIPHER TEXT SIZE')
    sheet2.write(0, 3, 'ENCRYPTION TIME ')
    sheet2.write(0, 4, 'DECRYPTION TIME')
    sheet2.write(0, 5, 'THROUGHPUT')
    sheet2.write(0, 6, 'CHANGE')
    with open("testfle.txt", "r") as myfile:
        data = myfile.readlines()
    dta = str(data)
    size = 500
    prev_dec = 0
    row2 = 0
    for xp in range (0,10):

        f = open('multifile.txt', 'w')
        size = size *dta
        p = xp * dta
        f.write(p)

        file = division(ch_line=10,file_name=f)

        start_time = timeit.default_timer()

        u, v, x, tim = encryption(file, start_time)

        dec = decryption(u, v, x)



        dec_change = dec - prev_dec

        prev_dec = dec

        for did in range(0, 6):
            if did == 0:
                sheet2.write(row2, 0,size)

            elif did == 1:
                sheet2.write(row2, 1, tim)
            elif did == 2:
                sheet2.write(row2, 2, dec)
            elif did == 3:
                sheet2.write(row2, 2, dec)
            elif did == 4:
                sheet2.write(row2, 2, dec)

            else:
                sheet2.write(row2, 3, dec + tim)
        row2 = row2 + 1
        f.close()


if __name__ == "__main__":
    main()
