#!/usr/bin/python
# -*- coding: utf-8 -*-

import sys # Import the sys module
import csv # Import the csv module
import constants as c # Import the project specific constants.py file
from csvvalidator import *

# Both of the follow globals will eventually come from the GUI part of the program as
# entered by the user
gFILEPATH = "/home/griadooss/Projects/WA/Nov2014/AVA/Workplace/AVA_Orig_Alt.csv"
gHASHEADER = True
gCLIENT = "AVA"


class Spreadsheet():
    def __init__(self, fp, hh, cn):
        self.file_path = fp
        self.has_header = hh
        self.client_name = cn
         
    def __str__(self):
        return "Spreadsheet at " + self.file_path + " of hearder state " + str(self.has_header) + " is being processed!"
# 
# class Column:
#     def __init__(self, attrib):
#         self.pos = attrib[0]
#         self.name = attrib[1]
#         self.datatype = attrib[2]
#         self.fieldlen = attrib [3]
#         
#    
#     def __str__(self):
#        return "Column is at position " + str(self.pos) \
#            + " is "  + self.name \
#            + " with datatype " + self.datatype \
#            + " which has a fixed length of " + str(self.fieldlen)
#    
#     def draw(self):
#         pass
#     
#     def drag(self):
#         pass
#        
# class Cell(Column):
#     def __init__(self):
#         pass
#     
#     def parse(self):
#         pass
#                
#        
# 
# 
# maskCol01 = Column(c.WAMAP[0])
# maskCol02 = Column(c.WAMAP[1])
# 
# for i in c.WAMAP:
#     print i
# 
# print maskCol01
# print maskCol02


#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
#CODE STARTS HERE:
# Get input file name from filepath, eventually provided by the user via the Tkinter UI 
spsht = Spreadsheet( gFILEPATH, gHASHEADER, gCLIENT)


#Overwrite any existing output and/or log file. Ready for a new pass
with open(c.OUTPUTCSV,'wb') as outputfile:
    outputfile.close()
with open(c.LOGFILE,'wb') as logfile:
    logfile.close()    

#OPERATIONAl LOOPING STARTS HERE
# Open the source file for reading



try:
    sourcefile = open(spsht.file_path)
    reader = csv.reader(sourcefile)

#     print c.WAMAP.get(0)
#     print c.WAMAP.get(0)[1]
#     
#     print c.WAMAP.keys()
#     print c.WAMAP.values()
#     print c.WAMAP.items()
# 
# 
#     for key in c.WAMAP:
#             print key
#               
#     for k in c.WAMAP:
#         print c.WAMAP[k]
#           
# #     for k, v in c.WAMAP.items():
# #         print ": ".join((k, v))
# 


    field_names = (
                   'CUSTID',
                   'FIRSTNAME',
                   'LASTNAME',
                   'CUSTNM',
                   'ADDRESS1',
                   'ADDRESS2'
                   'POSTCODE'
                   'CITY'
                   'STATE'
                   'WORKPHONE'
                   'WORKFAX'
                   'PHONE'
                   'MOBILE'
                   'EMAIL'
                   'ORGANISATION'
                   'EOL'
                   )
    
    validator = CSVValidator(field_names)
    
    # basic header and record length checks
    validator.add_header_check('EX1', 'bad header')
    validator.add_record_length_check('EX2', 'unexpected record length')
    
    # some simple value checks
    validator.add_value_check('CUSTID', int,
                              'EX3', 'study id must be an integer')
    validator.add_value_check('FIRSTNAME', int,
                              'EX4', 'patient id must be an integer')
    validator.add_value_check('LASTNAME', enumeration('M', 'F'),
                              'EX5', 'invalid gender')
    validator.add_value_check('CUSTNM', number_range_inclusive(0, 120, int),
                              'EX6', 'invalid age in years')
    validator.add_value_check('ADDRESS1', datetime_string('%Y-%m-%d'),
                              'EX7', 'invalid date')
    
    # a more complicated record check
    def check_age_variables(r):
        age_years = int(r['age_years'])
        age_months = int(r['age_months'])
        valid = (age_months >= age_years * 12 and
                 age_months % age_years < 12)
        if not valid:
            raise RecordError('EX8', 'invalid age variables')
    validator.add_record_check(check_age_variables)
    
    # validate the data and write problems to stdout
    data = csv.reader('/path/to/data.csv', delimiter='\t')
    problems = validator.validate(data)
    write_problems(problems, sys.stdout)












except IOError, e:
    print 'Error opening file'
    print "Message:", e.message
    print "Class:", e.__class__
    print "I/O error({0}): {1}".format(e.errno, e.strerror)
except:
    print "Unexpected error:", sys.exc_info()[0]
    raise

# except IOError as e:
#     print "I/O error({0}): {1}".format(e.errno, e.strerror)
# except ValueError:
#     print "Could not convert data to an integer."
# except:
#     print "Unexpected error:", sys.exc_info()[0]
#     raise

finally:
    sourcefile.close()

#########UP TO HERE TRANSFERRING CODE BIT BY BIT FROM AVA.PY

