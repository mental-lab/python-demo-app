#!/bin/bash

INGRESS=ingress-nginx
NAMESPACE=ingress-nginx

helm get all $INGRESS -n $NAMESPACE
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error: Could not find release $INGRESS in namespace $NAMESPACE, will try to install"
    helm upgrade --install $INGRESS ingress-nginx --repo https://kubernetes.github.io/ingress-nginx --namespace $NAMESPACE --create-namespace  --set controller.config.enable-real-ip='"true"' --set controller.config.use-forwarded-headers='"true"' --set controller.config.use-proxy-protocol='"true"' --set controller.service.externalTrafficPolicy='"Local"'
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo "Error: Could not install $INGRESS in namespace $NAMESPACE, Checking Logs:\n"
        kubectl logs $(kubectl get pods -n $NAMESPACE | grep $INGRESS-controller | awk '{print $1}')
        exit $retVal
    else
        # Sleep so that ingress service can pickup LoadBalancerIP. 
        # It only get's here if the ingress-controller is not installed.
        sleep 60
    fi
fi

kubectl rollout restart deployment $INGRESS-controller -n $NAMESPACE
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error: Could not restart deployment $INGRESS-controller in namespace $NAMESPACE, try describing the deployment\n"
    exit $retVal
fi

exit 0
