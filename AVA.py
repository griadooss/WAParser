# -*- coding: utf-8 -*-
################ Spreadsheet Parser ########################
############# by griadooss@qdoss.com.au ####################
################ Version 0.00 ##############################

'''This program has two purposes
1. to take an input spread sheet and have its column types 
match a predetermined mapping by allowing the user to 
remove, insert and move columns as required

2. To purge/remove/replace characters in the data that are
inconsistent with the user's requirements
'''

############ FUNCTION DECLARATION AREA #####################

#USER DEFINED FUNCTIONS

def ForceFieldLength(s, n):
    if len(s) > n:
        s = s[0:n]
    return s
    
def Logit(s):
    with open(LOGFILE,'ab') as logf:
        wrtr = csv.writer(logf)
        wrtr.writerow([s])
        
def CheckNumeric(s,b):
#Check field is only full of numeric characters 0-9  
    b = 'True'
    if not s.isdigit():
        Logit("CheckNumeric: LineNo - " + str(ln+1) + " | Mem ID - " + curline[0] + " |" + COLDESC[(i+1)] +" - " + s + " :: Not a numeric!")  
        b = 'False'
    return b
    
def CheckAlpha(s):
    if len(s) > 0:
        s=FixString(s)
        if not s.replace(" ","").isalpha() and len(s) > 0:
            Logit("CheckAlpha: LineNo - " + str(ln+1) + " | Mem ID - " + curline[0] + " |" + COLDESC[(i+1)] +" - " + s + " :: Not a alphabetic letter.")  
    return s          

def CheckAlphaNum(s):
    if len(s) > 0:
        #Set dubugging point
        #pdb.set_trace()
        s=FixString(s)
        if not s.replace(" ","").isalnum() and len(s) > 0:           
            Logit("CheckAlphaNum: LineNo - " + str(ln+1) + " | Mem ID - " + curline[0] + " |" + COLDESC[(i+1)] +" - " + s + " contains other than alpha numerics!!" )  
    return s    

      
def CheckEmail(s):
    #Check email string has at '@' and is a valid URL extension  
    ext = True
    if s=='':
        return
    #pdb.set_trace()
    for item in URLEXT:
        if s.find(item) > 0 :
            #pdb.set_trace()
            ext = True
            break
        ext = False
        
    if s.find('@') == -1:
        #pdb.set_trace()
        Logit("CheckEmail:  LineNo - " + str(ln+1) + " | Mem ID - " + curline[0] + " |" + COLDESC[(i+1)] +" - " + s + " no chiocciola!!")  
    
    if not ext:
        Logit("CheckEmail:  LineNo - " + str(ln+1) + " | Mem ID - " + curline[0] + " |" + COLDESC[(i+1)] +" - " + s + " not a known email ext.")  
    
    return
 
def FixString(s):
    #Strip anything that is not a number or a letter - FIND A BETTER WAY > DYNAMICALLY
    s=s.replace('/', '')
    s=s.replace('(', '')
    s=s.replace(')', '')
    s=s.replace('-', '')
    s=s.replace('+', '')
    s=s.replace('.', '')
    s=s.replace(',', '')
    s=s.replace('"', '')
    s=s.replace("'", "")
    s=s.replace('^', '')
    s=s.replace(':', '')
    s=s.replace('@', '')
    s=s.replace('[', '')
    s=s.replace(']', '')
    s=s.replace('_', ' ')
    s=s.replace('<', '')
    s=s.replace('>', '')
    s=s.replace('#', '')
    s=s.replace('\\', '')
    s=s.replace('!', '')
    s=s.replace('`', '') 
    s=s.replace('é', 'e')
    s=s.replace('ë', 'e')
    s=s.replace('é', 'e')
    s=s.replace('ô', 'o')
    s=s.replace('&', 'and')
    s=s.strip()
    
    return s



def FixPhoneNumber(s):
    #Strip anything that is not a number - FIND A BETTER WAY > DYNAMICALLY
    s=s.replace(' ', '')
    s=s.replace('(', '')
    s=s.replace(')', '')
    s=s.replace('+', '')
    s=s.replace('.', '')
    s=s.replace('-', '')
    s=s.replace('O', '0')
    
    if len(s) > 0:
        if not s.isdigit():
            s=''
            Logit("FixNumbersA - LineNo - " + str(ln+1) + " | Mem ID - " + curline[0] + " |" + COLDESC[(i+1)] +" - " + s +" Contains Alphas! No. set to Null") 
            return s
            
        if len(s) < 8:
            Logit("FixNumbersB - LineNo - " + str(ln+1) + " | Mem ID - " + curline[0] + " |" + COLDESC[(i+1)] +" - " + s + " less than 8 digits") 
            s=''
            return s    
        
        if len(s) == 8:
            if curline[8] == '':
                Logit("FixNumbersC - LineNo - " + str(ln+1) + " | Mem ID - " + curline[0] + " |" + COLDESC[(i+1)] +" - " + s + " 8 digits") 
                s=''
            else:
                s = AREACODE[curline[8]] + s
            return s
            
        #This def gets called for four seperate phone numbers
        #I have just used one LENGTH constant to compare as they all are the same
        #length .. but if they vary in the future .. change this to accomodate.
        if not (len(s) == 10 and (s[0:1] == '0') or s == ''): #10 digit AUS number with STD code
            if not (len(s) == 10 and s[0:4]=='1300'): #10 digit 1300 number
                if not (len(s) == 10 and s[0:4]=='1800'): #10 digit 1800 number
                    if not (len(s) == 10 and s[0:2]=='66'): #11 digit +66 numbers in internat format 
                        if not (len(s) == 11 and s[0:2]=='61'): #11 digit AUS number in internat format 
                            if len(s) == 9:
                                s=s.rjust(10,'0')
                                Logit("FixNumbersD - LineNo - " + str(ln+1) + " | Mem ID - " + curline[0] + " |" + COLDESC[(i+1)] +" - " + s + ' just added a zero')  
                            else:
                                #str(i+1) because the counters i & ln are zero based ..
                                #whereas 0 equates to column #1 or line #1, as the case may be
                                Logit("FixNumbersE - LineNo - " + str(ln+1) + " | Mem ID - " + curline[0] + " |" + COLDESC[(i+1)] +" - " + s + " => unknown format")  
    return s

######################## END - FUNCTION DECLARATION AREA #######################


############################ START - RESOURCES & CONSTANTS #####################
#Module import section
import sys # Import the sys module
import csv # Import the csv module
import pdb # Import the python debugger
#import os

#Set dubugging point
#pdb.set_trace()


#Manually check customer Excel file is in the standard TouchPaper format as below:
#If format conforms then set global FORMAT to 'OK', else leave it as ''.

            ########################################
            #          TOUCHPAPER FORMAT           # 
            # Col  # Description          # Length #
            #--------------------------------------# 
            #  1   # Member Number        # 20     #
            #  2   # Member First Name    # 30     #    
            #  3   # Member Surname       # 30     #   
            #  4   # Company Name         # 30     # 
            #  5   # Address1             # 40     # 
            #  6   # Address2             # 40     # 
            #  7   # Postcode             # 20     # 
            #  8   # City                 # 40     # 
            #  9   # State                # 40     # 
            #  10  # Work Phone Number    # 20     # 
            #  11  # Work Fax Number      # 20     # 
            #  12  # Home Phone Number    # 20     # 
            #  13  # Mobile Number        # 20     # 
            #  14  # EMail Address        #        # 
            #  15  # Association Name     # 40     # 
            #  16  # Line End Char - (*)  # 1      # 
            ########################################

#TOUCHPAPER DATA STRUCTURE
#Columns B,C,D,E,F,G,H,I are allowed NO punctuation 
#COlums J,K,L should have the area code and then the number .. no spaces or other puctuation .. just numbers
#Column M is a mobile number, again without any spaces or punctuation
#Column N a valid e-mail address ... must contain the '@' and at least one "." [is validation worth while here?]
#Column O ... Organisation Name as supplied from 'touchpaper' ... get mish to supply!!

###################################

#####################################
#CONSTANTSCONSTANTSCONSTANTSCONSTANTS
PREID='AVA'
COYNAME='The Australian Veterinary Assoc Ltd'
CSVFILENAME='AVA_Orig_Alt.csv'
OUTPUTCSV=CSVFILENAME[0:CSVFILENAME.find('.')] + '_processed.csv'
#OUTPUTCSV=CSVFILENAME[0:CSVFILENAME.find('.')] + '_TouchPaperFormat.txt'
LOGFILE=CSVFILENAME[0:CSVFILENAME.find('.')] + '_process_LOG.txt'
#Max length of data in each field - goverened by Touchpaper
FIELDLENGTH=["20","30","30","30","40","40","20","40","40","20","20","20","20","20","40","1"]
#Description of data in each colomn             
COLDESC={1:'Mem Num',2:'First Name',3:'Surname',4:'Coy Name',5:'Street1',6:'Street2',7:'PCode',8:'City',9:'State',10:'Wk Num',11:'Fax Num',12:'Hm Num',13:'Mobile',14:'Email',15:'Assoc',16:'EOL Char'}
#State Area Codes
AREACODE={'NSW':'02','ACT':'02','VIC':'03','TAS':'03','QLD':'07','WA':'08','SA':'08','NT':'08'}

##########################
#Max length of each column
COLLEN={1:20,2:30,3:30,4:30,5:40,6:40,7:20,8:40,9:40,10:20,11:20,12:20,13:20,14:'',15:40,16:1}
###################################
#List of most URL domain extensions
URLEXT=['.com', '.co', '.net', '.org', '.biz', '.info', '.us', '.mobi', '.tv', '.ws', '.cc', '.name', '.de', '.jp', '.be', '.at', '.asia', '.co.uk', '.me.uk', '.org.uk', 'co.nz', '.net.nz', '.org.nz', '.cn', '.com.cn', '.org.cn', '.net.cn', '.tw', '.com.tw', '.org.tw', '.idv.tw', '.jobs', '.fm', '.ms', '.me', '.nu', '.tc', '.tk', '.vg', '.com.au', '.org.au', '.net.au', '.co.nz', '.au.com', '.id.au', '.net.nz', '.asn.au', '.asia', '.org.nz', '.geek.nz', '.gen.nz', '.gov.au', '.edu.au', 'csiro.au', '.edu', '.gov', '.ac.nz', '.ca', 'alice.it', 'free.fr', 'hotmail.it', '.ac.uk', 'yahoo.es', 'live.hk', '.ch']

########################### START OF CODING PROPER ###########################
#VVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVVV

#FORMAT=''
FORMAT='OK'
if not FORMAT:
    sys.exit("\n\
    #######################################################################\n\
                       WENTWORTH HR parser \n\
                 a python script by QDOSS Pty Ltd \n\
    \n\
    \n\
    This code is for converting client provided spreadsheet data into a format \n\
    that can be imported into Touchpaper.\n\
    \n\
    First check that the customer Excel file's column count and sequence conforms \n\
    with the TouchPaper specification! [see documentation in this file]\n\
    \n\
    If it doesn't conform you my need to ask the customer to resubmit their data, \n\
    or if you can MANUALLY ajust it yourself in Excel, then do so. \n\
    \n\
    After the Excel file conforms with the column layout and sequence \n\
    required by Touchpaper, save the file in 'CSV' format and place that file \n\
    in the same directory as this python script file.\n\
    \n\
    Then change the following values in the coded script inside this file. \n\
    Open it with any text editor and change: \n\
    \n\
    Line 159: PREID='' to PREID='FAPRO', for example; the 'PREID' is the code \n\
    that is appended to the front of the customer id supplied by the client.\n\
    \n\
    Line 160: COYNAME='' to COYNAME='Fitness Australia', for \n\
    example, as dictated by the clients company name already in Touchpaper.\n\
    \n\
    Line 161: CSVFILENAME='' to CSVFILENAME='FA_PRO.csv', for example, but the \n\
    'xxxxxx.csv' filename you just saved the Excel spreadsheet as.\n\
    \n\
    Line 179: FORMAT='' to  FORMAT='OK'\n\
    \n\
    Then re-run this python code!\n\
    #######################################################################")
    
#########################
#Set Global Boolean FALSE
b=False
#Set HasHeader Boolean TRUE
hh=True

print OUTPUTCSV
print LOGFILE


#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!#!
#CODE STARTS HERE:

#Open the CSV file and read the first line
#It should be the Header, so, read the next line

#Set dubugging point
#pdb.set_trace()

# Open the source file for reading
sourcefile = open(CSVFILENAME)



#Overwrite any existing output and/or log file
with open(OUTPUTCSV,'wb') as outputfile:
    outputfile.close
with open(LOGFILE,'wb') as logfile:
    logfile.close    



#OPERATIONAl LOOPING STARTS HERE
try:
    #Create the reader and writer instances
    reader = csv.reader(sourcefile)
    
    #Read the Header line if it exists    
    if hh == True:
        curline = reader.next()
                   
    #Initiate counter for the lines
    ln = 0
    #Setup the loop
    while True:
        
        #Read the next line of the csv file
        curline = reader.next()
        ln = ln + 1
        
        #Initiate counter for the columns
        i=0
        print "Line Number " + str(ln) +":"
        while i < len(curline):
#            pdb.set_trace()        
            print str(i) + " " + FIELDLENGTH[i] + " " + curline[i]
            
            #there appears to be NO SWITCH/CASE in Python ..
            #switch(i) { 
            #    case 0:
            #        print("Processed first cell.");
            #        break;
            #    case 1:
            #        print("Processed second cell.");
            #        break;
            #    }
            
            #so must use if-next stack
            if i == 0:
                #CUST ID Column
#                pdb.set_trace()            
                #Concatenate OrgID + TheirCustID + IfPrincipal
                CheckNumeric(curline[i],b)
                if b == 'FALSE':
                    curcell_01 = curline[i] 
                else:
                    #curcell_01 = PREID + curline[0] + curline[7]
                    curcell_01 = PREID + curline[0]
                curcell_01 = ForceFieldLength(curcell_01, COLLEN[i+1])         
            elif i == 1:
#                pdb.set_trace()
                curcell_02 = curline[i]             
                curcell_02 = CheckAlpha(curcell_02)
                curcell_02 = ForceFieldLength(curcell_02, COLLEN[i+1]) 
            elif i == 2:
#                pdb.set_trace()
                #CheckAlpha(curline[i])
                curcell_03 = curline[i]
                curcell_03 = CheckAlpha(curcell_03)
                curcell_03 = ForceFieldLength(curcell_03, COLLEN[i + 1])
            elif i == 3:
#                pdb.set_trace()
                #CheckAlphaNum(curline[i])
                curcell_04 = curline[i]
                curcell_04 = CheckAlphaNum(curcell_04)
                curcell_04 = ForceFieldLength(curcell_04, COLLEN[i + 1])
            elif i == 4:
#                pdb.set_trace()
                #CheckAlphaNum(curline[i])
                curcell_05 = curline[i]
                curcell_05 = CheckAlphaNum(curcell_05)
                curcell_05 = ForceFieldLength(curcell_05, COLLEN[i + 1])
            elif i == 5:
                #CheckAlphaNum(curline[i])
                curcell_06 = curline[i]
                curcell_06 = CheckAlphaNum(curcell_06)
                curcell_06 = ForceFieldLength(curcell_06, COLLEN[i + 1])
            elif i == 6:
                if len(curline[i]) > 0:
                    CheckNumeric(curline[i],b)
                curcell_07 = curline[i]
                curcell_07 = ForceFieldLength(curcell_07, COLLEN[i + 1]) 
            elif i == 7:
                #CITY column - contains IfPrincipal in AOA data
                #this char [either 'P' or 'E' gets appended to CustID 
                #under 'If i == 0, so remove it here
                #CheckAlpha(curline[i])
                curcell_08 = curline[i]
                curcell_08 = CheckAlpha(curcell_08)
                curcell_08 = ForceFieldLength(curcell_08, COLLEN[i + 1])
                #curcell_08 = ''
            elif i == 8:
                #CheckAlpha(curline[i])
                curcell_09 = curline[i]
                curcell_09 = CheckAlpha(curcell_09)
                curcell_09 = ForceFieldLength(curcell_09, COLLEN[i + 1])
            elif i == 9:
#                pdb.set_trace()
                curcell_10 = curline[i]
                curcell_10 = FixPhoneNumber(curcell_10)
                curcell_10 = ForceFieldLength(curcell_10, COLLEN[i + 1])
            elif i == 10:
#                pdb.set_trace()
                curcell_11 = curline[i]
                curcell_11 = FixPhoneNumber(curcell_11)
                curcell_11 = ForceFieldLength(curcell_11, COLLEN[i + 1])
            elif i == 11:
#               pdb.set_trace()
                curcell_12 = curline[i]
                curcell_12=FixPhoneNumber(curcell_12)
                ForceFieldLength(curcell_12, COLLEN[i + 1])
            elif i == 12:
#               pdb.set_trace()
                curcell_13 = curline[i]
                curcell_13 = FixPhoneNumber(curcell_13)
                curcell_13 = ForceFieldLength(curcell_13, COLLEN[i + 1])
            elif i == 13:
#                pdb.set_trace()
                curcell_14 = curline[i]
                curcell_14 = ForceFieldLength(curcell_14, COLLEN[i + 1])
                CheckEmail(curcell_14)
            elif i == 14:
                curcell_15 = COYNAME
                curcell_15 = ForceFieldLength(curcell_15, COLLEN[i + 1])
            elif i == 15:
                curcell_16 = '*'
                ForceFieldLength(curcell_16, COLLEN[i + 1])
            else:
                print "Error: Should not have got to line 401"
                break    
            #Advance the counter                
            i = i + 1
        
        
        #Write the LINE!
        with open(OUTPUTCSV,'ab') as outputfile:
            wrtr = csv.writer(outputfile, delimiter=',', quotechar='"')
            wrtr.writerow([curcell_01]+[curcell_02]+[curcell_03]+[curcell_04]+[curcell_05]+[curcell_06]+[curcell_07]+[curcell_08]+[curcell_09]+[curcell_10]+[curcell_11]+[curcell_12]+[curcell_13]+[curcell_14]+[curcell_15]+[curcell_16])

finally:
    sourcefile.close()

  
