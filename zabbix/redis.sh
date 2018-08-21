#!/bin/bash
#
#此脚本只用于 info;cluster info 收集状态信息
#此脚本只适用于主进程
REDISCLI="/usr/local/bin/redis-cli -a admin"
HOST="127.0.0.1"
Flag=`date +%s -d '2018-07-06 12:00:00'`
Now=`date +%s`
Last_hit=
Last_miss=

let remainder=($Now - $Flag)%1


function redis_info(){
    $REDISCLI -h $HOST -p $1 info | grep -w $2 | awk -F: '{print $2}'
}

function redis_cluster(){
    $REDISCLI -h $HOST -p $1 cluster info | grep -w $2 | awk -F: '{print $2}'
}


echo $2 |grep -o cluster 2&>/dev/null
result=$?

if [ $2 == "hits" ];then
    hits=`$REDISCLI -h $HOST -p $1 info | grep -w keyspace_hits | awk -F: '{printf "%d",$2}'`
    miss=`$REDISCLI -h $HOST -p $1 info | grep -w keyspace_misses | awk -F: '{printf "%d",$2}'`
    let Hit_temp="${hits}"-"$Last_hit"
    let temp="${hits}"-"$Last_hit"+"${miss}"-"$Last_miss"
   # let Hiter="$Hit_temp"/"$temp"\*100
    Hiter=`awk 'BEGIN{printf "%.3f",('$Hit_temp'/'$temp'*100)}'`
    echo $Hiter

elif [ "$2"=="cluster_enabled" ];then
   redis_info $1 $2
elif [ $result -ne 0 ];then
   redis_info $1 $2
else
   redis_cluster $1 $2
fi

if [ "$remainder" -eq 0 ];then
    sed -i s/^Last_hit.*/Last_hit="$hits"/ $0
    sed -i s/^Last_miss.*/Last_miss="$miss"/ $0
fi

