import matplotlib
import xlrd
import numpy as np
import matplotlib.pyplot as plt

AGEGROUP = int(input("Enter AGEGROUP class: "))

workbook = xlrd.open_workbook("data.xls")
sheet = workbook.sheet_by_name('Sheet1')

data_values = [0,0,0]
data_labels = 'ISCED 0', 'ISCED 3', 'ISCED 5'

data_count = [0,0,0]
count = 0

for rownum in range(sheet.nrows):
    if sheet.cell(rownum, 3).value == AGEGROUP:
        if sheet.cell(rownum,4).value == 0: #ISCED 0
            if sheet.cell(rownum,5).value != 4: #USE
                data_values[0] += 1
            data_count[0] += 1
        elif sheet.cell(rownum,4).value == 3: #ISCED 3
            if sheet.cell(rownum,5).value != 4: #USE
                data_values[1] += 1
            data_count[1] += 1
        else: #ISCED 5
            if sheet.cell(rownum,5).value != 4: #USE
                data_values[2] += 1
            data_count[2] += 1

final_values = []
for x in range(3):
    final_values.append(100*data_values[x]/data_count[x])
    count +=final_values[x]


colors = ['yellowgreen', 'gold' , 'lightskyblue']#, 'lightcoral']
patches, texts = plt.pie(final_values, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels = ['%s : %1.1f%% , %1.1f%%' % (data_labels[x], 100*data_values[x]/data_count[x], 100*final_values[x]/count) for x in range(len(data_labels))], loc="best")
#plt.legend(patches, data_labels, loc="best")
plt.axis('equal')
plt.title("Proportional ISCED Internet usage, AGEGROUP " + str(AGEGROUP))
plt.tight_layout()
plt.show()