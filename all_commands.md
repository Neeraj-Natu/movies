## Initial Setup

    go to keys folder in desktop and run below command:
    `docker login -u _json_key -p "$(cat neeraj-arena-8ab6102d6c75.json)" https://gcr.io`

    To build the docker image use: (do this in docker toolbox)
    `docker build -t gcr.io/neeraj-arena/[Image Name] .`
    `docker push [HOSTNAME]/[PROJECT-ID]/[IMAGE]`


    Now move to google SDK:
    Run below command to check if the image is correctly updated in google container registry
    `gcloud container images list`


    from gcloud sdk run the below command to get credentials from neeraj-cluster: (This is needed only once every cluster)
    `gcloud container clusters get-credentials neeraj-cluster --zone us-central1-a --project neeraj-arena`
    the above command can also be copied from GKE when u click on connect for connecting to the desired cluster.


    Now move to each deployment file and deploy the services one by one.
    `kubectl create -f deployment.yaml`


# Deployment type: NODE_PORT:

    Next once the NodePort type service is created check for the node-port and open the port from firewall as below:
    `gcloud compute firewall-rules create test-node-port --allow tcp:[NODE_PORT]`

    TO find out the IP address of the node check which node the service is running from console.
    Then go to VPN networks to find the external IP address of the node.

    The request now will be http://[External-IP]:[Node-Port]

# Deployment type: Ingress
    
    For Ingress type you'll need to ensure that Http load balancing add-on has been enabled in GKE else the ingress is not created and there is usually no clue what is happening in backend. (https://stackoverflow.com/questions/51223937/ingress-is-not-getting-address-on-gke-and-gce).

    incase of issues with ingress not getting address use the below command to check what happened:
    `kubectl describe ing neeraj-ingress -n default`

    For Ingress type service remeber to have the service give a 200 response back on endpoint `/` as the rediness check is done on this endpoint by the internal rediness check which is created when we create the ingress for more refer:(https://serverfault.com/questions/809824/http-load-balancer-on-google-container-engine-using-ingress).

    The ingress is actually implemented via a third party Ingress Controller which has different implementations.
    gce, ambassasor,nginx etc.. these all are different implementations of ingress controllers.
    Amongst these all the most well known and used is the nginx one. This can expose the services of type clusterIP.
    Although you must first install this type of Ingress controller as it doesnot come in pre installed.
    
    
    So all these issues are resolved in the current code and seem to work fine so to create Ingress all the services need to first created as a nodeport or as loadbalancer as Ingress can only talk to these. Once that is done you can run the command to create Ingress which is:
    `kubectl create -f ingress-deployment.yaml`


# Deployment using helm charts    
	
	For using helm first you need to install the same on your local machine.
	For installing it on windows the easiest option is via choclatey which is a package manager for windows.
	 first install choclatey using below comand on an admin cmd prompt:
	 `@"%SystemRoot%\System32\WindowsPowerShell\v1.0\powershell.exe" -NoProfile -InputFormat None -ExecutionPolicy Bypass -Command "iex ((New-Object System.Net.WebClient).DownloadString('https://chocolatey.org/install.ps1'))" && SET "PATH=%PATH%;%ALLUSERSPROFILE%\chocolatey\bin"`
	 
	 
	Once done use the below command to install helm:
	`choco install kubernetes-helm`
	
	it will take a few seconds to be installed. Once done you can use helm on your local machine.
	Now go to google cloud sdk console and check if you have helm available by using `helm --help`
	If done right there should be no issues there.

    To start off follow the instructions listed at:
    
    Ensure your user account has the cluster-admin role in your cluster.
    `kubectl create clusterrolebinding user-admin-binding --clusterrole=cluster-admin --user=$(gcloud config get-value account)`

    Create a service account that Tiller, the server side of Helm, can use for deploying your charts.
    `kubectl create serviceaccount tiller --namespace kube-system`

    Grant the Tiller service account the cluster-admin role in your cluster:
    `kubectl create clusterrolebinding tiller-admin-binding --clusterrole=cluster-admin --serviceaccount=kube-system:tiller`

    Initialize Helm to install Tiller in your cluster:
    `./helm init --service-account=tiller`
    `./helm update`


    verify that helm and tiller is installed in the cluster
    `kubectl get deploy,svc tiller-deploy -n kube-system`
    `helm ls` empty result as we haven't installed anything

    