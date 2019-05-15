Probably you might know what Istion is and why should it be used if not please follow the below link to get familier with the service mesh technology that layers above the vanila Kubernetes deployments.

[What is Istio](https://istio.io/docs/concepts/what-is-istio/)


When deploying services on a Istio enabled cluster.
The recommended approach is to use automatic sidecar injection turned on.

So when you create the Istio enabled GKE cluster the first command to apply is below:


`kubectl label namespace default istio-injection=enabled`

Now once cluster is ready move on with the usualy commands to first create services as below:

`kubectl apply -f ratings-deployment.yaml`

`kubectl apply -f predictions-deployment.yaml`

`kubectl apply -f movie-details-deployment.yaml`

`kubectl apply -f movies-deployment.yaml`

once the services are created the Virtual Services and the Gateway can be now created with below command

`kubectl apply -f ingress-deployment.yaml`

To understand more about Ingress gateway and Virtual Services in Istio please refer to below links:

[Istio Ingress Gateways](https://istio.io/docs/concepts/traffic-management/#gateways)

[Istio Virtual Service](https://istio.io/docs/reference/config/networking/v1alpha3/virtual-service/#Destination)


The above varient just scratches the surface with what Istio service mesh can do, I will be adding in more details and examples and variations that can be used with Istio as I explore them.
