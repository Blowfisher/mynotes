package main

import (
        "flag"
        "fmt"
        "context"
        metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
        "k8s.io/client-go/kubernetes"
        "k8s.io/client-go/rest"
        "k8s.io/client-go/tools/clientcmd"
        "os"
)

var kubeconfig = flag.String("kubeconfig", "/root/.kube/config", "kubeconfig file")

func init() {
        flag.Parse()
}

func main() {
        config, err := rest.InClusterConfig()
        if err != nil {
                if envar := os.Getenv("KUBECONFIG"); len(envar) > 0 {
                        kubeconfig = &envar
                }
                config, err = clientcmd.BuildConfigFromFlags("", *kubeconfig)
                if err != nil {
                        fmt.Println("Config err: ", err)
                        os.Exit(1)
                }
        }
        config.AcceptContentTypes = "application/vnd.kubernetes.protobuf, application/json"
        config.ContentType = "application/vnd.kubernetes.protobuf"

        clientset, err := kubernetes.NewForConfig(config)
        if err != nil {
                fmt.Println("Config Set: ", err)
                os.Exit(1)
        }
        pod, err := clientset.CoreV1().Pods("default").Get(context.Background(),"svoice-asr-6785f46bc5-7wpwv", metav1.GetOptions{})
        if err != nil {
                fmt.Println("Get Err: ", err)
                os.Exit(1)
        }
        fmt.Println(pod)
}
