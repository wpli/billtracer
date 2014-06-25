#!/bin/bash
DATA_FOLDER=$1
MEETING_NAME=$2
OUTPUT=$1/$2/raw-pages
VERSION=2.0.0-SNAPSHOT
TMP=tmp

INPUTFILE_NAME=$2.pdf

echo "Extracting individual pages from PDF..."
if [ ! -d $OUTPUT ]
then
    echo "    Making directory: $OUTPUT"
    mkdir $OUTPUT
fi

#if [ ! -d $TMP ]
#then
#    mkdir $TMP
#    echo $TMP/$INPUTFILE
#    cp $INPUTFILE $TMP/$INPUTFILE
#    java -jar pdfbox-app-$VERSION.jar PDFSplit $TMP/$INPUTFILE 
#fi

if [ ! -d $TMP ]
then
    mkdir $TMP
    pdftk $DATA_FOLDER/$MEETING_NAME/$INPUTFILE_NAME burst output $TMP/%02d.pdf
    rm $TMP/doc_data.txt
fi

#rm $TMP/$INPUTFILE

for f in `ls $TMP`
do
    echo $f
    java -jar pdfbox-app-$VERSION.jar ExtractText -html -encoding utf-8 $TMP/$f $OUTPUT/$f.html
done

rm -rf $TMP

