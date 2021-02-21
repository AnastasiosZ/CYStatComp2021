import matplotlib
import xlrd
import numpy as np
import matplotlib.pyplot as plt

workbook = xlrd.open_workbook("data.xls")
sheet = workbook.sheet_by_name('Sheet1')

data_values = [0,0,0,0,0]
data_labels = 'IUPH1', 'IUSNET', 'IUNW1', 'IHIF', 'IUIF'


count = 0

for rownum in range(sheet.nrows):
    for x in range(7,12):
        try:
            data_values[x-7] += int(sheet.cell(rownum,x).value)
        except:
            continue

for value in data_values:
    count+=value

colors = ['yellowgreen', 'gold' , 'lightskyblue', 'lightcoral', 'darkorchid']
patches, texts = plt.pie(data_values, colors=colors, shadow=True, startangle=90)
plt.legend(patches, labels = ['%s : %1.1f%%' % (data_labels[x], 100*data_values[x]/count) for x in range(len(data_labels))], loc="best")
#plt.legend(patches, data_labels, loc="best")
plt.axis('equal')
plt.title("Act of Internet Activities from all AGEGROUP classes")
plt.tight_layout()
plt.show()
