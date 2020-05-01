#!/bin/bash

#设定时区
#ansible kube  -m command -a "ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime"
ln -sf /usr/share/zoneinfo/Asia/Shanghai /etc/localtime
yum -y install ntpdate
ntpdate ntp1.aliyun.com

#设定时间
cmd="date --date=@`date +%s`"
data=`${cmd}`
ansible kube -m command -a "date -s '$data'"
