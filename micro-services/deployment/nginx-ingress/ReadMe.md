Ingress is an API object that manages external access to the K8s cluster. It is mainly used to provide single point of entry into the cluster, provide SSL termination, Load Balancing and name based virtual hosting.
To read more about Ingress please visit below link:

[Ingress concepts](https://kubernetes.io/docs/concepts/services-networking/ingress/)


Nginx Ingress Controller is amongst the most popular implementations of Ingress controllers today.
To learn more about it please visit the below links:

[Official documentation](https://kubernetes.github.io/ingress-nginx/)

[gitHub project](https://github.com/kubernetes/ingress-nginx)


Also the following does a good work to explain how it works behind the scenes.

[How it works](https://itnext.io/kubernetes-ingress-controllers-how-to-choose-the-right-one-part-1-41d3554978d2)


## Working with Nginx Ingress Gateway

  * When using an nginx Ingress Gateway the first thing to do is install nginx-ingress controller in the cluster.
    This is not done by default and use the below commands to do it.

  `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/mandatory.yaml`

  `kubectl apply -f https://raw.githubusercontent.com/kubernetes/ingress-nginx/master/deploy/provider/cloud-generic.yaml`
  
    The above commands are specific for GKE but similar commands for other clouds can be found at:

  [ingress-nginx deploy](https://kubernetes.github.io/ingress-nginx/deploy)

  [contd...](https://github.com/kubernetes/ingress-nginx/blob/master/docs/deploy/index.md)

[The entire tutorial can be found by click this link.](https://cloud.google.com/community/tutorials/nginx-ingress-gke)

  * Once the ingress-nginx and the related config maps are deployed carry on with regular steps with creating the services first and then the ingress gateway.

`kubectl apply -f ratings-deployment.yaml`

`kubectl apply -f predictions-deployment.yaml`

`kubectl apply -f movie-details-deployment.yaml`

`kubectl apply -f movies-deployment.yaml`

once the services are created then the ingress gateway is created with below command:

`kubectl apply -f ingress-deployment.yaml`



