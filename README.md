# kubernetes-ejedzenie

## A simple application to order products 

### Getting started

Run this command in this directory to build and run the component:
          
          kubectl apply -f <component_path>



Run this command to see which components are running currently
        
         
         kubectl get all



To start application using minikube make sure that minikube has access to image

        
        minikube image load <container:tag>


To show list of containers in minikube run

        
        minikube image ls --format table

***