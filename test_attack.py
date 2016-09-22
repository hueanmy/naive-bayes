import sys
import os, os.path
from sys import argv
import apache_log_parser
from apache_log_parser import *
import csv
import pprint, StringIO
from pprint import pprint

script, filename = argv

with open(filename) as f:
   ofile  = open('attack_log.csv', "wb")
   outputWriter = csv.writer(ofile)
   for line in f:
        line_parser = apache_log_parser.make_parser("%h %l %u %t \"%r\" %>s %b \"%{Referer}i\" \"%{User-agent}i\"")
        log_line_data = line_parser(line)

        time_received = StringIO.StringIO()
        pprint(log_line_data['time_received'],time_received)
        time_receivedcsv = time_received.getvalue().replace("\n","").replace("'","")
        time_receivedcsv = time_receivedcsv [14:22]
        t0 = float(time_receivedcsv[0])
        t2 = float(time_receivedcsv[2:3])
        t5 = float(time_receivedcsv[5:6])
        time_receivedcsv = (t0 * 3600 + t2* 60 + t5)/86400
        # print time_receivedcsv

        method = StringIO.StringIO()
        pprint(log_line_data ['request_method'],method)
        method_csv = method.getvalue().replace("\n","").replace("'" , "")
        if method_csv == 'GET':
           method_csv = 0
        if method_csv == 'POST':
           method_csv = 1
        if method_csv == 'HEAD':
           method_csv = 2
        if method_csv == 'DELETE':
           method_csv = 3
        if method_csv == 'PUT':
           method_csv = 4
        if method_csv == 'HEAD':
           method_csv = 5
        if method_csv == 'OPTIONS':
           method_csv = 6
        if method_csv == 'TRACE':
           method_csv = 7
        # print method_csv

        path = StringIO.StringIO()
        pprint(log_line_data ['request_url'],path)
        path_csv = path.getvalue().replace("\n","").replace("'", "")
        # path_csv = '/dvwa-1.9/dvwa/css/\"980610%40'
        # print path_csv
        list = '%, ", ?, _, $, &, *, /, \\, \., \|'
        symbol_in_request = 0
        for i in range(0, len(path_csv)):
          if path_csv[i] in list:
            symbol_in_request +=1
            x = float(len(path_csv))
        p_symbol = symbol_in_request / x
        status = StringIO.StringIO()
        pprint(log_line_data['status'],status)
        status_csv = status.getvalue().replace("\n","").replace("'","")
        status_csv = float(status_csv)/500
        # print status_csv
        outputWriter.writerow([ time_receivedcsv, method_csv, p_symbol, status_csv, 1])
   ofile.close()
