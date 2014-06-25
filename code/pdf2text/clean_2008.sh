DATA_FOLDER="../../data/FOMC2008"

for directory in `ls -d ../../data/FOMC2008/FOMC*`
do
    #echo $f
    meeting_name="${directory##*/}"
    echo $meeting_name
    bash extract_fomc_pages.sh $DATA_FOLDER $meeting_name  #/$filename.pdf
    python cleanup_FOMC_parser.py $DATA_FOLDER $meeting_name

    #bash cleanup_FOMC_parser/
done