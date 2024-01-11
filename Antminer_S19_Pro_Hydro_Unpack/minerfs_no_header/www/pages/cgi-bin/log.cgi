echo
echo
dmesg
echo -e "\n"
echo "===========================================Miner log==========================================="
logfiles=`ls -r /var/log/miner.log*`
for logfile in $logfiles;
do
    cat $logfile | sed '/^$/d'
done