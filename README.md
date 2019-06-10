# Movies

This repository is to try out different technologies related to microservices and api gateway
This repository is solely for my own learning and understanding purpose.

So far I have readup and used:
    
  * Micro-Services
    * [Ingress](https://github.com/nginxinc/kubernetes-ingress)
    * [Nginx-Ingress](https://kubernetes.github.io/ingress-nginx/)
    * [Istio](https://istio.io/)
    * [Node-Port](https://kubernetes.io/docs/concepts/services-networking/service/)
    * [helm](https://helm.sh/)
  
  * API-Gateway
    * [Apigee Edge](https://docs.apigee.com/)
  
The Technologies listed above under micro services are all used with Kubernetes and docker. For a generic use case I preferred using Google Cloud and it's GKE product to try out different use cases.

For API Gateway I preferred Apigee as I use it in my day job and also cause it's by far the most mature solution albiet a bit costly.

## Pre requisites

	To get started with trying out these different technologies you'll need to first install the below:

	* Docker for Kubernetes (Mac OS or Windows 10 Pro)
	* Google Cloud SDK
	* kubectl command line
	* VS Code (or any other IDE)
	* Python 3.5+
	* helm
	* Istio
	* Create an Account on Google Cloud

### Initialize SDK  

	Once the above dependencies are installed setup the google cloud sdk using below command:

`gcloud init`

	and then follow the instructions to setup the account as in the [link.](https://cloud.google.com/sdk/gcloud/reference/init)


### Authenticate Docker to use docker container registry

	As we are using google container registry we will require to configure docker to use the google container registry.
	To do that use the below command:

`gcloud auth configure-docker`

	If you are on windows and using docker toolbox then you would need to complete the authentication configure process using Json file the steps for the same are in the following [link.](https://cloud.google.com/container-registry/docs/advanced-authentication#json_key_file)

### Start the Kubernetes cluster
	
	Now move on to google cloud console and navigate to kubernetes engine dashboardto create a kubernetes cluster with 4 nodes in same zone located in us-central-1a region (any US region would do). Leave all the configurations as they are and choose the latest version of kubernetes engine and click create. Wait for the cluster to be created. Once the cluster is created click on the connect button and copy the command to run on google cloud shell.

	Run that command on google sdk to generate credentials for the cluster.

 
## Getting Started

	Once the pre-requisites are installed and setup then clone this repository and navigate to services folder.

### Create Docker Images and push to Docker registry

	From services folder within each service is a micro-service create the docker images of each services and push them to google container registry as per the instructions written in respective ReadMe files.

### Deploy services and other components to Kubernetes Engine

	Once pushed move on back to google sdk and navigate to deployments folder and from there every folder contains a different scenario setup to deploy the services. Follow the instructions in respective ReadMe files to deploy the services and other components.



