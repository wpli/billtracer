import os
import json

STATE_ABBREVS = [u'al', u'ak', u'az', u'ar', u'ca', u'co', u'ct', u'de', u'dc', u'fl', u'ga', u'hi', u'id', u'il', u'in', u'ia', u'ks', u'ky', u'la', u'me', u'md', u'ma', u'mi', u'mn', u'ms', u'mo', u'mt', u'ne', u'nv', u'nh', u'nj', u'nm', u'ny', u'nc', u'nd', u'oh', u'ok', u'or', u'pa', u'pr', u'ri', u'sc', u'sd', u'tn', u'tx', u'ut', u'vt', u'va', u'wa', u'wv', u'wi', u'wy']

DATA_PATH = '/Users/wli/Dropbox/states/data/json/'

def get_state_abbbreviations():
    return STATE_ABBREVS

def get_state_bill_urls( state ):
    state_bill_urls = []

    state_path = os.path.join( DATA_PATH, state )
    metadata_file = os.path.join( state_path, 'metadata.json' )
    with open( metadata_file ) as f:
        x = json.load( f )

    bills_path = os.path.join( state_path, 'bills', state )
    for root, dirs, files in os.walk(bills_path):
        if len( dirs ) == 0 and len( files ) != 0:
            for bill in files:
                bill_full_path = os.path.join( root, bill )
                with open( bill_full_path ) as f:
                    bill_json = json.load( f )

                versions = bill_json['versions']
                for v in versions:
                    state_bill_urls.append( v['url'] )

    return state_bill_urls


def get_all_bill_urls( state_abbreviations = STATE_ABBREVS ):
    all_bill_urls = []
    for state in state_abbreviations:
        all_bill_urls += get_state_bill_urls( state )


def main():
    bill_urls = get_bill_urls()

if __name__ == '__main__':
    main()


