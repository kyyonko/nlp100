# cat ../hightemp.txt | python python2_1.py > col1.txt
# cat ../hightemp.txt | python python2_2.py > col2.txt

cat ../hightemp.txt | cut -f1 > col1_u.txt
cat ../hightemp.txt | cut -f2 > col2_u.txt

python python.py ../hightemp.txt 1  > col1.txt
python python.py ../hightemp.txt 2  > col2.txt

md5sum col1.txt
md5sum col1_u.txt

md5sum col2.txt
md5sum col2_u.txt
