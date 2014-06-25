#!/bin/bash
OUTPUT=raw-pages
VERSION=2.0.0-SNAPSHOT
TMP=tmp
INPUTFILE=$1
echo "Extracting individual pages from PDF..."

if [ ! -d $TMP ]
then
    mkdir $TMP
    java -jar pdfbox-app-$VERSION.jar PDFSplit $INPUTFILE $TMP/
fi

if [ ! -d $OUTPUT ]
then
    echo "    Making directory: $OUTPUT"
    mkdir $OUTPUT
fi

for (( PAGE=1; PAGE<=$TOTAL_PAGES; PAGE++ ))
do
    echo "    Extracting page $PAGE..."
    java -jar pdfbox-app-$VERSION.jar ExtractText -html -encoding utf-8 -startPage $PAGE -endPage $PAGE fcic_final_report_full.pdf $OUTPUT/fcic_final_report_full--$PAGE.html
done

rm -rf $TMP