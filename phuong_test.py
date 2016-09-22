import csv
import sys
from pprint import pprint
from collections import Counter

c1 = 0
c2 = 0
attack_list = []
time_list_c1 = []
time_list_c2 = []
counttime_c1 = []
counttime_c2 = []
with open('log.csv' , "r+") as csvlogfile:
	reader_log = csv.reader(csvlogfile)
	for line in reader_log:
		attack_list.append(str(line[4]))
	for x in range(len(attack_list)):
		if attack_list[x] == '1':
			c1 += 1
		if attack_list[x] == '0':
			c2 +=1
	count_attack = c1 + c2
	Pc1 = float(c1)/float(count_attack)
	Pc2 = float(c2)/float(count_attack)
	csvlogfile.close()

with open('attack_log.csv' , "r+") as csv_attackfile:
	reader_attacklog = csv.reader(csv_attackfile)
	for line in reader_attacklog:
		time_list_c1.append(str(line[0]))
	counttime_c1.append(Counter(time_list_c1).items())
	# pprint (counttime_c1)
	csv_attackfile.close()

with open('normal_log.csv' , "r+") as csv_normalfile:
	reader_normallog = csv.reader(csv_normalfile)
	for line1 in reader_normallog:
		time_list_c2.append(str(line1[0]))
		#time_list_c2 IS AN ARRAY
pprint (Counter(time_list_c2).values()) #WHAT DOES IT RETURN?
# pprint (Counter('phuongg'))

	# counttime_c2.append(str(Counter(time_list_c2).items()))
	#
	# for i in counttime_c2:
	# 	pprint (i)
	# 	pprint ("\n")
	# csv_normalfile.close()
	# # pprint(time_list_c2)
