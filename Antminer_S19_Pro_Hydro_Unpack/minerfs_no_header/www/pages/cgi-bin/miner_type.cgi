echo
echo
if [ -f /etc/subtype ]
then
    subtype=`cat /etc/subtype`
else
    if [ -f /etc/topol.conf ]
    then
        tpuid=`cat /etc/topol.conf | jq -r .machine`
        id=${tpuid:3:${#tpuid}}
        chip=`cat /etc/topol.conf | jq -r .processor.type | tr 'A-Z' 'a-z'`
        subtype=${chip}_${id}
    else
        subtype="unknown"
    fi
fi

miner_type=`cat /usr/bin/compile_time  | sed -n '2p'`

fw_version=`cat /usr/bin/compile_time  | sed -n '1p'`

echo "{\"miner_type\": \"$miner_type\", \"subtype\": \"$subtype\", \"fw_version\": \"$fw_version\"}"
