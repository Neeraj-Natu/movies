When deploying services on a Istio enabled cluster.
The recommended approach is to use automatic sidecar injection turned on.

`kubectl label namespace default istio-injection=enabled`