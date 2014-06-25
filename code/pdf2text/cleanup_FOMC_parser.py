from __future__ import division
#!/usr/bin/env python


import sys
import os

DATA_FOLDER = sys.argv[1]
MEETING_NAME = sys.argv[2]

INPUT_FOLDER = 'raw-pages'
OUTPUT_FOLDER = 'clean-pages'

REPLACEMENTS = {
        "&#63043;" : "0",
        "&#63044;" : "1",
        "&#63045;" : "2",
        "&#63046;" : "3",
        "&#63047;" : "4",
        "&#63048;" : "5",
        "&#63049;" : "6",
        "&#63050;" : "7",
        "&#63051;" : "8",
        "&#63052;" : "9",
        "&#8220;" : "``",
        "&#8221;" : "''",
        "&#8217;" : "'",
        "&#63059;" : "$",
        "&#63042;" : "%",
        "&#8212;" : "---",
        "&#8226;" : "*"
}

##==-----------------------------------------------------------------------==##
from bs4 import BeautifulSoup 
import os
import glob
import re
import csv

def readHtml( path ):
        with open( path, 'r' ) as f:
                content = f.read().decode( 'utf-8' )
        return content

def writeHtml( path, content ):
        with open( path, 'w' ) as f:
                f.write( content.encode( 'utf-8' ) )

def sortPaths(path):
	path = path.split('/')[-1]
	path = path.split('.')[0]
	path = int( path )
	#path = path.split("-")[1]
	#path = path.split(".")[0]
	#path = int(path)
	return path
	

##==-----------------------------------------------------------------------==##

# Document-specific cleanup
print "Cleaning up all extracted pages..."

broken = []
# Loop through all pages

input_folder_full_path = os.path.join( DATA_FOLDER, MEETING_NAME, INPUT_FOLDER )

paths = glob.glob( '{}/*.html'.format(input_folder_full_path) )

print paths
paths = sorted(paths, key=sortPaths)

transcript = []

for path in paths :
        # Read from disk
	filename = path[len(INPUT_FOLDER)+1:]
	content = readHtml( path )
	content = BeautifulSoup(content)
	print "    Processing {}".format( filename )
	content = content.find_all('p')
	
	#import ipdb
	#ipdb.set_trace()
	#try:
	#	content = [p.string.strip() for p in content]
	#except:
	#	pass
	content = [ p.getText().strip() for p in content ]
	#if sortPaths(path) not in [1, 2]:       
	#	transcript += content[0:-1]
	transcript += content[0:-1]

#print transcript[0:5]

for t in transcript:
	if "CHAIRMAN" not in t:
		transcript = transcript[1:]
	else:
		break
		
#transcript = [re.sub('\[[A-Z][a-z]+\]', '', t) for t in transcript]
transcript = [s for s in transcript if len(s)!=0]
#transcript = transcript [1:]


#regex

#print transcript[0:5]
speaker_list = []
speech = []
for s in transcript:
	speaker = re.findall("MR. [A-Z]+\.|MRS. [A-Z]+\.|MS. [A-Z]+\.|[A-Z]+ [A-Z]+\.|[A-Z]+ [A-Z]+ [A-Z]+\.", s)		
	if len(speaker)>0:
		speaker_list.append(speaker[0])
		#print speaker_list
		s = s.replace(speaker[0], '')
		speech.append(s)
		#print speech
	else:
		speech[-1] += ' '
		speech[-1] +=  s


#speech = [s.replace('2019', "'") for s in speech]
#print speech[0:10]

speech = [s.encode('utf8', 'ignore') for s in speech]

discourse_number = range(len(speaker_list))

document = zip(discourse_number, speaker_list, speech)

#print document[0]
#print document[1]

#print len(speaker_list)
#print len(speech)
#print len(discourse_number)



import sys
print paths[0]
#filename = paths[0].split('/')[1]
#filename = filename.split('-')[0]
#print filename
#with open('FOMC20070807meeting.csv', 'wb') as f:

output_file = os.path.join( DATA_FOLDER, MEETING_NAME, MEETING_NAME + ".csv" )

with open(output_file, 'wb') as f:
	w = csv.writer(f)
	w.writerow(['Discourse Number', 'Speaker', 'Speech'])
	for row in document:
		w.writerow(row)


