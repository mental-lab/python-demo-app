#!/bin/bash

ECHO=echo
NAMESPACE=default

kubectl get deploy $ECHO -n $NAMESPACE
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error: Could not find deployment $ECHO in namespace $NAMESPACE, will try to install"
    kubectl apply -f scripts/yamls/echo/deploy.yaml
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo "Error: Could not install deployment $ECHO in namespace $NAMESPACE, Checking Logs:\n"
        kubectl logs $(kubectl get pods -n $NAMESPACE | grep $ECHO | awk '{print $1}')
        exit $retVal
    fi
fi

kubectl get service $ECHO -n $NAMESPACE
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error: Could not find service $ECHO in namespace $NAMESPACE, will try to install"
    kubectl apply -f scripts/yamls/echo/service.yaml
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo "Error: Could not install service $ECHO in namespace $NAMESPACE"
        exit $retVal
    fi
fi

kubectl get ingress $ECHO -n $NAMESPACE
retVal=$?
if [ $retVal -ne 0 ]; then
    echo "Error: Could not find ingress $ECHO in namespace $NAMESPACE, will try to install"
    kubectl apply -f scripts/yamls/echo/ingress.yaml
    retVal=$?
    if [ $retVal -ne 0 ]; then
        echo "Error: Could not install ingress $ECHO in namespace $NAMESPACE"
        exit $retVal
    fi
fi

exit 0
