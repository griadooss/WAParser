############# DEDUPE CSV FILE BASED ON FIRST COLUMN SCRIPT ##################
#############################################################################

#Manually check customer Excel file has been sorted by the column you want to 
#dedupe by and place that column as the first column. Save as CSV file
#
##### READ THIS WHEN REVISITING THIS CODE ##### 
#Before running this code manually sort the file, first by MemberID and then so 
#that any duplicates that have the column 'STATE' as 'OS' [Overseas] DO NOT 
#appear as the first duplicate of that particular memeber after being sorted, 
#or else the OS record will be the record that appears in the de-duped or 
#clean file, while the AUSSIE records will be shunted to the DUPLICATES file, 
#and consequently left out of the auto import


############################ START - RESOURCES & CONSTANTS #####################
#Module import section
import sys # Import the sys module
import csv # Import the csv module
import pdb # Import the python debugger
#import os
#####################################
#CONSTANTSCONSTANTSCONSTANTSCONSTANTS
#CSVFILENAME='ADA_Orig_Adj.csv'
CSVFILENAME='AVA_test.csv'
DUPESCSV=CSVFILENAME.__getslice__(0,CSVFILENAME.find('.')) + '_dupes.csv'
CLEANCSV=CSVFILENAME.__getslice__(0,CSVFILENAME.find('.')) + '_clean.csv'
LOGFILE=CSVFILENAME.__getslice__(0,CSVFILENAME.find('.')) + '_dedupe_LOG.txt'
##########################
print DUPESCSV
print CLEANCSV
print LOGFILE

#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
#CODE STARTS HERE:

#Set dubugging point
#http://docs.python.org/2/library/pdb.html#debugger-commands
#pdb.set_trace()

# Open the source file for reading
sourcefile = open(CSVFILENAME)

#Overwrite any existing output and/or log file
with open(DUPESCSV,'wb') as dupesfile:
    dupesfile.close
with open(CLEANCSV,'wb') as cleanfile:
    cleanfile.close
with open(LOGFILE,'wb') as logfile:
    logfile.close
 
#OPERATIONAl LOOPING STARTS HERE
try:
    #Create the reader and writer instances
    reader = csv.reader(sourcefile)
   
    #Initiate counter for the lines    
    ln = 0
    i = 0
    prevID = ''
    currID = ''
    
     #Setup the loop
    while True:
        #Remember previous ID
        prevID = currID 
        #Read the next line of the csv file
        curline = reader.next()
        ln = ln + 1
        currID = curline[i]
              
        if prevID == currID:
            with open(DUPESCSV,'ab') as dupesfile:
                wrtr = csv.writer(dupesfile, delimiter=',', quotechar='"')
                wrtr.writerow(curline) 
        else:  
                   
            with open(CLEANCSV,'ab') as cleanfile:
                wrtr = csv.writer(cleanfile, delimiter=',', quotechar='"')
                wrtr.writerow(curline)
         
finally:
    sourcefile.close()
    cleanfile.close()
    dupesfile.close()   
