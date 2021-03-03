#### kubernetes note

  [High avaliable for kubernetes](https://github.com/kubernetes/kubeadm/blob/master/docs/ha-considerations.md#options-for-software-load-balancing "rely on kubeadm tool")</br>
 
  [Level Triggering and Reconciliation in Kubernetes](https://hackernoon.com/level-triggering-and-reconciliation-in-kubernetes-1f17fe30333d "Events driven trigger")</br>
   
  [kubernetes programming](./kubernetes-dev "kubernetes programming")</br>  
  
[SDN website](https://sdn.feisky.xyz/ "kubernetes SDN")</br>  
#### AWS ElasticSearch Service  
[AWS elasticsearch service docs](https://opendistro.github.io/for-elasticsearch-docs/docs/ism/ "es")

[CloudWatch to ES](LambdaVPCLogsToES.js "Javascript Script Realize Demo")

### Redis 
[Redis Source Code Analyces](https://redissrc.readthedocs.io/en/latest/index.html "Redis源码解析")



#### Shell note
  Here is a method that to set host time serise
```bash
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
```
#### Jenkins note
###### pipeline demo 
```jenkins
pipeline {
    agent any
    options{
        timestamps()
    }
    stages {
        stage('Hello') {
            input{
                message "Should we cotinue? "
                ok "No, we should not."
            }
            steps {
                echo 'Hello World'
                script{
                    ip = sh(returnStdout:true, script:'bash /get_ip.sh ${component} ${index}').trim()
                }
                sh "echo IP is: ${ip}"
                sh "sed -i /${ip}/d /etc/ansible/hosts"
            }
        }
    }
}
```
