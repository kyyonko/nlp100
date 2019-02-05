cat ../hightemp.txt | cut -f1 | sort | uniq -c | sort -k1 -r | awk '{print $2}'
