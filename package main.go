package main

import (
    "context"
    "fmt"
    metav1 "k8s.io/apimachinery/pkg/apis/meta/v1"
    "k8s.io/client-go/kubernetes"
    "k8s.io/client-go/tools/clientcmd"
)

func main() {
    kubeconfig := "/path/to/your/kubeconfig"
    config, err := clientcmd.BuildConfigFromFlags("", kubeconfig)
    if err != nil {
        panic(err)
    }

    clientset, err := kubernetes.NewForConfig(config)
    if err != nil {
        panic(err)
    }

    deployment, err := clientset.AppsV1().Deployments("default").Get(context.TODO(), "myapp-deployment", metav1.GetOptions{})
    if err != nil {
        panic(err)
    }

    *deployment.Spec.Replicas = 5

    _, err = clientset.AppsV1().Deployments("default").Update(context.TODO(), deployment, metav1.UpdateOptions{})
    if err != nil {
        panic(err)
    }

    fmt.Println("Scaled deployment successfully")
}