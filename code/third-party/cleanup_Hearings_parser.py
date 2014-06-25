#Broken up code from new Stack Over Flow Question
#http://stackoverflow.com/questions/20385262/type-error-when-running-a-large-function-in-python/20387063?noredirect=1#20387063

from bs4 import BeautifulSoup
from collections import namedtuple
import csv
from itertools import tee, izip
import os, os.path
import re
from shutil import copy2

#C:\Users\SSWPHD\Dropbox\Qualifying Paper\Congressional Hearings\NHTF Project\Test Set
#C:\Users\mboogie\Dropbox\Qualifying Paper\Congressional Hearings\NHTF Project\Test Set

DIR       = '/home/sethtren/fc_mapping/scraped_pdfs/download/'
HEARINGS = os.listdir(DIR)
HEARINGS = [hearing for hearing in HEARINGS if ".htm" in hearing]
HARD_WRAP = re.compile(r'\n(?!    )')
SPEAKERS  = re.compile(r'^    (Senator|Ms.|Mr.|Mrs.|Mr.|Congressman|Congresswoman|Chairman|Chairwoman|Secretary|The) ([A-z]{2,40})\.', re.MULTILINE)
NAME      = lambda m: '{0} {1}'.format(*m.groups())
Speaker   = namedtuple('Speaker', ['name', 'name_start', 'name_end'])

def load_hearing_response(fname, split_on='    Present:'):
    with open(fname, 'rU') as inf:
        html = inf.read()
    txt  = BeautifulSoup(html).get_text()
    return txt.rsplit(split_on, 1)[-1]     # return everything after last occurrence of split_on

def un_hard_wrap(txt, reg=HARD_WRAP):
    return reg.sub('', txt)

def pairwise(iterable):
    a,b = tee(iterable)
    next(b, None)
    return izip(a, b)

def get_speeches(txt):
    speakers = [Speaker(NAME(sp), sp.start(), sp.end()) for sp in SPEAKERS.finditer(txt)]
    speakers.append(Speaker('', len(txt), None))    # tail sentinel for pairwise processing
    return [(this.name, txt[this.name_end:nxt.name_start]) for this,nxt in pairwise(speakers)]

def write_csv(DIR, file, data, stem, header=None):
    folder_name = '/home/sethtren/fc_mapping/scraped_pdfs/nhearings_new/' + stem
    os.mkdir(folder_name)
    os.chdir(folder_name)
    with open(file, 'wb') as outf:
        out_csv = csv.writer(outf)
        if header is not None:
            out_csv.writerow(header)
        out_csv.writerows(data)
    os.chdir(DIR)
 
def main(HEARINGS):
    for hearing in HEARINGS:
    # get text of Congressional hearing responses
        print hearing
    stem = hearing.split('.')[0]
    csv_name = stem + ".csv"
    txt = load_hearing_response(os.path.join(DIR, hearing))
    txt = un_hard_wrap(txt)
    # break into speeches
    speeches = get_speeches(txt)
    # write (speaker, speech) pairs to a .csv file
    write_csv(DIR, csv_name, speeches, stem, ['Speaker', 'Speech'])
    # write paragraphs of speeches to a .csv file
   # paragraphs = ([para.strip()] for speaker,speech in speeches for para in speech.split('\n') if para.strip())
   # write_csv(os.path.join(DIR, 'Paragraphs.csv'), paragraphs, ['Paragraphs'])

if __name__=="__main__":
    main(HEARINGS)

#Brilliant!! works perfectly!
#Code acknowledgment - Hugh Bothwell (http://stackoverflow.com/users/33258/hugh-bothwell)
