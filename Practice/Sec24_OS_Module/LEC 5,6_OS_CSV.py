# # CSV.Writer:

# import csv
# Covid05 = [('Country','Doses','People','Percenage'),
# ('India','186Cr','84Cr',61),
# ('China','330Cr','184Cr',88.1),
# ('United','56.8Cr','59Cr',66.4),
# ('Brazil','42.4Cr','76Cr',76.4),
# ('Indonesia','39Cr','16.2Cr',59.3)]

# f = open('Covid05.csv', 'w', newline='')
# wrtr = csv.writer(f)

# for tup in Covid05:
#     wrtr.writerow(tup)

# f.close()



# CSVDictonary Writer:
import csv
Dict06covid = [
{'Country':'India','Doses':'186Cr','People':'84Cr','Persentage':61},
{'Country':'China','Doses':'330Cr','People':'184Cr','Persentage':88.1},
{'Country':'United','Doses':'56.8Cr','People':'59Cr','Persentage':66.4},
{'Country':'Brazil','Doses':'42.4Cr','People':'76Cr','Persentage':76.4},
{'Country':'Indonesia','Doses':'39Cr','People':'16.2Cr','Persentage':59.3}]

f = open('Dict06covid.csv', 'w', newline='')

fields = ['Country','Doses','People','Persentage']
wrtr = csv.DictWriter(f,fields)

wrtr.writeheader() # It give the Headding:

for d in Dict06covid:
    wrtr.writerow(d)

f.close()