import cPickle
import collections
import os
import sys
sys.path.append( '../utils' )
import utils_schema
import ipdb

HOME = os.path.expanduser("~")
FILEPATH = "Dropbox/projects/unshared/data/processed"

fomc_schema = [ 'meeting_id' ] + ['Discourse_Number', 'Speaker', 'Speech']
FOMC = collections.namedtuple( 'FOMC', fomc_schema )

ch_schema = ['hearing_category', 'folder', 'Discourse_Number', 'Speaker', 'Speech']
CongressionalHearings = collections.namedtuple( 'CongressionalHearings', ch_schema )


def main():

    # Load our datasets
    with open( os.path.join( HOME, FILEPATH, 'fomc_namedtuples.pkl' ) ) as f:
        fomc_namedtuples = cPickle.load( f )

    with open( os.path.join( HOME, FILEPATH, 'congressionalhearings_namedtuples.pkl' ) ) as f:
        congressionalhearings_namedtuples = cPickle.load( f )
    


    ipdb.set_trace()

if __name__ == '__main__':
    main()
