## adsbib.py
## A tool for collecting BibTeX records from NASA ADS.
##
## Call with reference to a plaintext list of bibcodes,
##   separated by newlines. Output will be to the same
##   filename, appended with .bib
## >> python3 ads-bib.py bibcodes
##
## Note : To strip an existing BibTeX file down to bibcodes with vim,
##	:v/^@/d
##	:%s/@.*{//g
##	:%s/,//g

import ads

## Setup the argument parser
import argparse
parser = argparse.ArgumentParser(description='bibcode to import')
parser.add_argument('bibcode', help='A bibcode for input')
args = parser.parse_args()

## Read bibcode input from file if not specified
#bibcode = args.bibcode
with open(args.bibcode) as f:
	bibcode = f.read().splitlines()
f.close()

## Query ADS with the set of bibcodes
q = ads.ExportQuery(bibcodes=bibcode,format='bibtex')
bibtex = q.execute()

## Write BibTeX entries to file
with open(args.bibcode+'.bib', 'a') as bibfile:
	print(bibtex, file=bibfile)

bibfile.close()
