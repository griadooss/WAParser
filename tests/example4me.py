#!/usr/bin/env python

"""
An executable Python script illustrating the use of the CSVValidator module.

This script illustrates some, but not all, of the features available. For a 
complete account of all features available, see the tests.py module.
"""

import argparse
import os
import sys
import csv
from csvvalidator import CSVValidator, enumeration, number_range_inclusive,\
    write_problems, datetime_string, RecordError




def create_validator():
    """Create an example CSV validator for patient demographic data."""
#                                     

    def CheckAlpha(s=''):
        if len(s) > 0:
        #        s=FixString(s)
            if not s.replace(" ","").isalpha() and len(s) > 0:
                return False
        #            Logit("CheckAlpha: LineNo - " + str(ln+1) + " | Mem ID - " + curline[0] + " |" + COLDESC[(i+1)] +" - " + s + " :: Not a alphabetic letter.")  
        return True          


    field_names = (
                   'CUSTID', 
                   'FIRSTNAME', 
                   'LASTNAME', 
                   'CUSTNM', 
                   'ADDRESS1',
                   'ADDRESS2',
                   'POSTCODE',
                   'CITY',
                   'STATE',
                   'WORKPHONE',
                   'WORKFAX',
                   'PHONE',
                   'MOBILE',
                   'EMAIL',
                   'ORGANISATION',
                   'EOL'
 
                   )
    validator = CSVValidator(field_names)
    
    # basic header and record length checks
    validator.add_header_check('EX1', 'bad header')
    validator.add_record_length_check('EX2', 'unexpected record length')
    
    # some simple value checks
    validator.add_value_check('CUSTID', int, 
                              'EX3', 'CUSTID must be an integer')
    validator.add_value_check('FIRSTNAME', CheckAlpha, 
                              'EX4', 'FIRSTNAME must be an integer')
    validator.add_value_check('LASTNAME', str, 
                              'EX5', 'invalid LASTNAME')
    validator.add_value_check('CUSTNM', str, 
                              'EX6', 'invalid CUSTNM')
    validator.add_value_check('ADDRESS1', str, 
                              'EX7', 'invalid ADDRESS1')
    validator.add_value_check('ADDRESS2', str, 
                              'EX8', 'invalid ADDRESS2')
    validator.add_value_check('POSTCODE', int, 
                              'EX9', 'invalid POSTCODE')
    validator.add_value_check('CITY', str, 
                              'EX10', 'invalid CITY')
    validator.add_value_check('STATE', str, 
                              'EX11', 'invalid STATE')
    validator.add_value_check('WORKPHONE', int, 
                              'EX12', 'invalid WORKPHONE')
    validator.add_value_check('WORKFAX', int, 
                              'EX13', 'invalid WORKFAC')
    validator.add_value_check('PHONE', int, 
                              'EX14', 'invalid PHONE')
    validator.add_value_check('MOBILE', int, 
                              'EX15', 'invalid MOBILE')
    validator.add_value_check('EMAIL', str, 
                              'EX16', 'invalid EMAIL')
    validator.add_value_check('ORGANISATION', str, 
                              'EX17', 'invalid ORGANISATION')
    validator.add_value_check('EOL', str, 
                              'EX18', 'invalid EOL')
    
    # a more complicated record check
    def check_age_variables(r):
        CUSTNM = int(r['CUSTNM'])
        ADDRESS1 = int(r['ADDRESS1'])
        valid = (ADDRESS1 >= CUSTNM * 12 and 
                 ADDRESS1 % CUSTNM < 12)
        if not valid:
            raise RecordError('EX8', 'invalid age variables')
    validator.add_record_check(check_age_variables)
    
    return validator

   

def main():
    """Main function."""

    # define a command-line argument parser
    description = 'Validate a CSV data file.'
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument('file', 
                        metavar='FILE', 
                        help='a file to be validated')
    parser.add_argument('-l', '--limit',
                        dest='limit',
                        type=int,
                        action='store',
                        default=0,
                        help='limit the number of problems reported'
                        )
    parser.add_argument('-s', '--summarize',
                        dest='summarize',
                        action='store_true',
                        default=False,
                        help='output only a summary of the different types of problem found'
                        )
    parser.add_argument('-e', '--report-unexpected-exceptions',
                        dest='report_unexpected_exceptions',
                        action='store_true',
                        default=False,
                        help='report any unexpected exceptions as problems'
                        )
    
    # parse arguments
    args = parser.parse_args()
    
    # sanity check arguments
    if not os.path.isfile(args.file):
        print '%s is not a file' % args.file
        sys.exit(1)

    with open(args.file, 'r') as f:

        # set up a csv reader for the data
        data = csv.reader(f, delimiter='\t')
        
        # create a validator
        validator = create_validator()
        
        # validate the data from the csv reader
        # N.B., validate() returns a list of problems;
        # if you expect a large number of problems, use ivalidate() instead
        # of validate(), but bear in mind that ivalidate() returns an iterator
        # so there is no len()
        problems = validator.validate(data, 
                                      summarize=args.summarize,
                                      report_unexpected_exceptions=args.report_unexpected_exceptions,
                                      context={'file': args.file})

        # write problems to stdout as restructured text
        write_problems(problems, sys.stdout, 
                       summarize=args.summarize, 
                       limit=args.limit)
        
        # decide how to exit
        if problems: # will not work with ivalidate() because it returns an iterator
            sys.exit(1)
        else:
            sys.exit(0)
    

if __name__ == "__main__":
    main()

