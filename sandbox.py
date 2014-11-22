#!/usr/bin/python
# -*- coding: utf-8 -*-

import WAConstants as const

class Column:
    def __init__(self, attrib):
        self.pos = attrib[0]
        self.name = attrib[1]
        self.datatype = attrib[2]
        self.fieldlen = attrib [3]
        
   
    def __str__(self):
       return "Column is at position " + str(self.pos) \
           + " is "  + self.name \
           + " with datatype " + self.datatype \
           + " which has a fixed length of " + str(self.fieldlen)
   
    def draw(self):
        pass
    
    def drag(self):
        pass
       
class Cell(Column):
    def __init__(self):
        pass
    
    def parse(self):
        pass
               
       


maskCol01 = Column( const.WAMAP[0] )
maskCol02 = Column( const.WAMAP[1] )

for i in const.WAMAP:
    print i

print maskCol01
print maskCol02

# Open the CSV file and read the first line
# It should be the Header, so, read the next line

# Open the source file for reading
sourcefile = open(const.CSVFILENAME)
sourcefile.close()
#Overwrite any existing output and/or log file
with open(const.OUTPUTCSV,'wb') as outputfile:
    outputfile.close()
with open(const.LOGFILE,'wb') as logfile:
    logfile.close()    

#########UP TO HERE TRANSFERRING CODE BIT BY BIT FROM AVA.PY

