from csv2sqlite import convert
import sqlite3
import os
import sys

if __name__ == '__main__':
    dbpath = 'profile.db'
    if os.path.exists(dbpath):
        os.remove(dbpath)
    
    filename = sys.argv[1]
    table_name = filename
    if 1:
    #for table_name in ( 'bio', 'universities', 'education', 'groups' ):
        table = table_name
        fileobj = filename
        convert(fileobj, dbpath, table)
        conn = sqlite3.connect(dbpath)
        c = conn.cursor()
        c.execute('select count(*) from %s' % table);
        row = c.next()
    #assert row[0] == 3, row
