# sed
sed -e s/$'\t'/" "/g ../hightemp.txt

# tr
cat ../hightemp.txt | tr '\t' ' ' | less

# expand
expand -t 1 ../hightemp.txt
