## adsbib.py
## A tool for collecting BibTeX records from NASA ADS.
##
## bibcodes can either be specified as command line arguments,
## 	>> python3 adsbib.py bibcode1 bibcode2 bibcode3
## or as a series of lines within a file bibcodes
##
## BibTeX data will be collected and output to bib-lib.bib
##
## Note : To strip an existing BibTeX file down to bibcodes with vim,
##	:v/^@/d
##	:%s/@.*{//g
##	:%s/,//g

import ads

## Disable this bit until sorting out optional arguments...
## Setup the argument parser
#import argparse
#parser = argparse.ArgumentParser(description='bibcode to import')
#parser.add_argument('bibcode', help='A bibcode for input')
#parser.add_argument('bibcode', metavar='N', type=str, nargs='+', help='A bibcode for input')
#args = parser.parse_args()

## Read bibcode input from file if not specified
#bibcode = args.bibcode
#if len(bibcode) == 0:
with open('bibcodes') as f:
	bibcode = f.read().splitlines()
f.close()

## Query ADS with the set of bibcodes
q = ads.ExportQuery(bibcodes=bibcode,format='bibtex')
bibtex = q.execute()

## Write BibTeX entries to file
with open('bib-lib.bib', 'a') as bibfile:
	print(bibtex, file=bibfile)

bibfile.close()
