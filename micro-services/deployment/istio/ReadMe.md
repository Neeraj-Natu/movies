Probably you might know what Istion is and why should it be used if not please follow the below link to get familier with the service mesh technology that layers above the vanila Kubernetes deployments.

[What is Istio](https://istio.io/docs/concepts/what-is-istio/)


## Installing Istio

(incase of issues follow this [installation link](https://preliminary.istio.io/docs/setup/kubernetes/install/helm/).)
In case if you want to install a custom version of Istio (recommended 1.1 and above) follow the steps as mentioned below:

* First download/clone the release of Istio that you want to install this will contain the YAML files for Kubernetes, samples and istioctl for manual sidecar injection.

*   Second Ensure the kubenetes cluster has atleast 4 nodes and the ensure current user has admin permissions  this is done using following command:
  
      ` kubectl create clusterrolebinding cluster-admin-binding --clusterrole=cluster-admin    --user=$(gcloud config get-value core/account)`

* Make sure Helm is version 2.10 or above.
  
* In case you donot want to use the charts in release and want the Istio release Helm Chart repo instead just add them to helm using below command:
  
  `helm repo add istio.io https://storage.googleapis.com/istio-release/releases/1.2.0/charts/`

* change directory to the root of release. cd path to istio-(release_version).
  
* Now bootstrap all the istio CRDs using the below command to install `istio-init`

    `helm install install/kubernetes/helm/istio-init --name istio-init --namespace istio-system`

* For kiali there is an extra step to move back to plain_vanila folder and install the kiali secrets using 

    `kubectl apply -f kiali-deployment.yaml`


* Once that is done use below command to install istio:

    `helm install install/kubernetes/helm/istio --set kiali.enabled=true --name istio --namespace istio-system`


## Installing services on an Istio enabled cluster

When deploying services on a Istio enabled cluster.
The recommended approach is to use automatic sidecar injection turned on.

So when you create the Istio enabled GKE cluster the first command to apply is below:

`kubectl label namespace default istio-injection=enabled`

Now once cluster is ready move on with the usualy commands to first create services as below:

`kubectl apply -f ratings-deployment.yaml`

`kubectl apply -f predictions-deployment.yaml`

`kubectl apply -f movie-details-deployment.yaml`

`kubectl apply -f budget-deployment.yaml`

`kubectl apply -f popularity-deployment.yaml`

`kubectl apply -f revenues-deployment.yaml`

once the services are created the Virtual Services and the Gateway can be now created with below command

`kubectl apply -f ingress-deployment.yaml`

To understand more about Ingress gateway and Virtual Services in Istio please refer to below links:

[Istio Ingress Gateways](https://istio.io/docs/concepts/traffic-management/#gateways)

[Istio Virtual Service](https://istio.io/docs/reference/config/networking/v1alpha3/virtual-service/#Destination)


The above varient just scratches the surface with what Istio service mesh can do, I will be adding in more details and examples and variations that can be used with Istio as I explore them.
