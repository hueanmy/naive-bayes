import csv
import sys
from pprint import pprint
from collections import Counter

attack = 0
normal = 0
attack_list = []
query_list = []
time_list_attack = []
time_list_normal = []
ptime_attack = []
ptime_normal = []
method_list_attack = []
method_list_normal = []
pmethod_attack = []
pmethod_normal = []
query_list_attack = []
query_list_normal = []
pquery_attack = []
pquery_normal = []
status_list_attack = []
status_list_normal = []
pstatus_attack = []
pstatus_normal = []
status_label_attack = []
time_label_attack = []
method_label_attack = []
query_label_attack = []
status_label_normal = []
time_label_normal = []
method_label_normal = []
query_label_normal = []
pm_attack = []
pq_attack = []
ps_attack = []
pt_attack = []
pm_normal = []
pq_normal = []
ps_normal = []
pt_normal = []
p_attack  = []
p_normal  = []
c1_pattack = []
c2_pnormal = []
compare = []
line_pro = []
with open('log.csv' , "a+") as csvlogfile:
	reader_log = csv.reader(csvlogfile)
	write_pr = csv.writer(csvlogfile)
	for line in reader_log:
		attack_list.append(str(line[4]))
	for x in range(len(attack_list)):
		if attack_list[x] == '1':
			attack += 1
		if attack_list[x] == '0':
			normal +=1
	count_attack = attack + normal
	Pc1 = float(attack)/float(count_attack)
	Pc2 = float(normal)/float(count_attack)
csvlogfile.close()

with open('attack_log.csv' , "r+") as csv_attackfile:
	reader_attacklog = csv.reader(csv_attackfile)
	for line in reader_attacklog:
		time_list_attack.append(str(line[0]))
		method_list_attack.append(str(line[1]))
		query_list_attack.append(str(line[2]))
		status_list_attack.append(str(line[3]))
counttime_attack = Counter(time_list_attack).values()
countmethod_attack = Counter(method_list_attack).values()
countquery_attack = Counter(query_list_attack).values()
countstatus_attack = Counter(status_list_attack).values()
countstatus_attack_items = Counter(status_list_attack).items()
countmethod_attack_items = Counter(method_list_attack).items()
countquery_attack_items = Counter(query_list_attack).items()
counttime_attack_items = Counter(time_list_attack).items()
for i in counttime_attack:
	#xac xuat cua truong thoi gian cho c1
	ptime_attack.append(float(i)/float(attack))
for i in countmethod_attack:
	#xs cua method cho c1
	pmethod_attack.append(float(i)/float(attack))
for i in countquery_attack:
	#xs query cho c1
	pquery_attack.append(float(i)/float(attack))
for i in countstatus_attack:
	#xs status cho c1
	pstatus_attack.append(float(i)/float(attack))
for i in countstatus_attack_items:
	status_label_attack.append(i[0])
for i in counttime_attack_items:
	time_label_attack.append(i[0])
for i in countquery_attack_items:
	query_label_attack.append(i[0])
for i in countmethod_attack_items:
	method_label_attack.append(i[0])

Label_pstatus = dict(zip(status_label_attack,pstatus_attack))
Label_pmethod = dict(zip(method_label_attack,pmethod_attack))
Label_pquery = dict(zip(query_label_attack,pquery_attack))
Label_ptime = dict(zip(time_label_attack,ptime_attack))
for i in status_list_attack:
	for j in range(len(Label_pstatus)):
		if i == Label_pstatus.keys()[j]:
			ps_attack.append(Label_pstatus.values()[j])                                 # xac suat p(status/attack)
for i in time_list_attack:
	for j in range(len(Label_ptime)):
		if i == Label_ptime.keys()[j]:
			pt_attack.append(Label_ptime.values()[j])
			         # xac suat p(time/attack)

for i in method_list_attack:
	for j in range(len(Label_pmethod)):
		if i == Label_pmethod.keys()[j]:
			pm_attack.append(Label_pmethod.values()[j])                                 # xac suat p(method/attack)

for i in query_list_attack:
	for j in range(len(Label_pquery)):
		if i == Label_pquery.keys()[j]:
			pq_attack.append(Label_pquery.values()[j])                                   # xac suat p(query/attack)
csv_attackfile.close()

with open('normal_log.csv' , "r+") as csv_normalfile:
	reader_normallog = csv.reader(csv_normalfile)
	for line1 in reader_normallog:
		time_list_normal.append(str(line1[0]))
		method_list_normal.append(str(line1[1]))
		query_list_normal.append(str(line[2]))
		status_list_normal.append(str(line[3]))
counttime_normal = Counter(time_list_normal).values()
countmethod_normal = Counter(method_list_normal).values()
countquery_normal = Counter(query_list_normal).values()
countstatus_normal = Counter(status_list_normal).values()
countstatus_normal_items = Counter(status_list_normal).items()
countmethod_normal_items = Counter(method_list_normal).items()
countquery_normal_items = Counter(query_list_normal).items()
counttime_normal_items = Counter(time_list_normal).items()
         # xs tung truong /normal
for i in counttime_normal:
	ptime_normal.append(float(i)/float(normal))
for i in countmethod_normal:
	pmethod_normal.append(float(i)/float(normal))
for i in countquery_normal:
	pquery_normal.append(float(i)/float(normal))
for i in countstatus_normal:
	pstatus_normal.append(float(i)/float(normal))
for i in countstatus_normal_items:
	status_label_normal.append(i[0])
for i in counttime_normal_items:
	time_label_normal.append(i[0])
for i in countquery_normal_items:
	query_label_normal.append(i[0])
for i in countmethod_normal_items:
	method_label_normal.append(i[0])

Label_pstatus2 = dict(zip(status_label_normal,pstatus_normal))
Label_pmethod2 = dict(zip(method_label_normal,pmethod_normal))
Label_pquery2 = dict(zip(query_label_normal,pquery_normal))
Label_ptime2 = dict(zip(time_label_normal,ptime_normal))
for i in status_list_normal:
	for j in range(len(Label_pstatus2)):
		if i == Label_pstatus2.keys()[j]:
			ps_normal.append(Label_pstatus2.values()[j])                               # xac suat p(status/normal)
for i in time_list_normal:
	for j in range(len(Label_ptime2)):
		if i == Label_ptime2.keys()[j]:
			pt_normal.append(Label_ptime2.values()[j])                                   # xac suat p(time/normal)

for i in method_list_normal:
	for j in range(len(Label_pmethod2)):
		if i == Label_pmethod2.keys()[j]:
			pm_normal.append(Label_pmethod2.values()[j])                                 # xac suat p(method/normal)

for i in query_list_normal:
	for j in range(len(Label_pquery2)):
		if i == Label_pquery2.keys()[j]:
			pq_normal.append(Label_pquery2.values()[j])                                   # xac suat p(query/normal)

csv_normalfile.close()
group_p_attack = zip(pt_attack, pm_attack , ps_attack, pq_attack)
for i in group_p_attack:
	p_attack.append(i[0]*i[1]*i[2]*i[3])
group_p_normal = zip(pt_normal, pm_normal, ps_normal,pq_normal)
for i in group_p_normal:
	p_normal.append(i[0]*i[1]*i[2]*i[3])

for i in p_attack:
	c1_pattack.append(Pc1 * i)
for i in p_normal:
	c2_pnormal.append(Pc2 *i)

group_c1_c2 = zip(c1_pattack,c2_pnormal)
for i in group_c1_c2:
	if i[0] > i[1]:
		compare.append("1")
	# if i[0] < i [1]:
	# 	compare.append("0")
with open('log.txt' , "r+") as f:
	for line in f:
		line_pro.append(line)
	group_pr_txt = zip(line_pro, compare)
	pprint(group_pr_txt)
