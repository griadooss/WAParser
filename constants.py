#!/usr/bin/python
# -*- coding: utf-8 -*-
#
# constants.py
#
#CONSTANTSCONSTANTSCONSTANTSCONSTANTS
PREID='AVA'
COYNAME='The Australian Veterinary Assoc Ltd'
CSVFILENAME='input.csv'
OUTPUTCSV=CSVFILENAME[0:CSVFILENAME.find('.')] + '_processed.csv'
LOGFILE=CSVFILENAME[0:CSVFILENAME.find('.')] + '_process_LOG.txt'
#Max length of data in each field - goverened by Touchpaper
FIELDLENGTH=["20","30","30","30","40","40","20","40","40","20","20","20","20","20","40","1"]
#Description of data in each colomn             
COLDESC={1:'Mem Num',2:'First Name',3:'Surname',4:'Coy Name',5:'Street1',6:'Street2',7:'PCode',8:'City',9:'State',10:'Wk Num',11:'Fax Num',12:'Hm Num',13:'Mobile',14:'Email',15:'Assoc',16:'EOL Char'}
#State Area Codes
WAMAP = { 0 : (1, 'cust_id', 'digit', 20), 
          1 : (2, 'first_name', 'alpha', 30),
          2 : (3, 'surname', 'alpha', 30),
          3 : (4,'company', 'alpha', 30),
          4 : (5, 'street1', 'alphanumeric', 40),
          5 : (6, 'street2', 'alphanumeric', 40) }   
AREACODE={'NSW':'02','ACT':'02','VIC':'03','TAS':'03','QLD':'07','WA':'08','SA':'08','NT':'08'}

##########################
#Max length of each column
COLLEN={1:20,2:30,3:30,4:30,5:40,6:40,7:20,8:40,9:40,10:20,11:20,12:20,13:20,14:'',15:40,16:1}
###################################
#Tuple of most URL domain extensions
URLEXT=('.com', '.co', '.net', '.org', '.biz', '.info', '.us', '.mobi', '.tv', '.ws', '.cc', '.name', '.de', '.jp', '.be', '.at', '.asia', '.co.uk', '.me.uk', '.org.uk', 'co.nz', '.net.nz', '.org.nz', '.cn', '.com.cn', '.org.cn', '.net.cn', '.tw', '.com.tw', '.org.tw', '.idv.tw', '.jobs', '.fm', '.ms', '.me', '.nu', '.tc', '.tk', '.vg', '.com.au', '.org.au', '.net.au', '.co.nz', '.au.com', '.id.au', '.net.nz', '.asn.au', '.asia', '.org.nz', '.geek.nz', '.gen.nz', '.gov.au', '.edu.au', 'csiro.au', '.edu', '.gov', '.ac.nz', '.ca', 'alice.it', 'free.fr', 'hotmail.it', '.ac.uk', 'yahoo.es', 'live.hk', '.ch')
