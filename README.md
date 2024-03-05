# CAMB.AI_BackendChallange

## first run Requirement.txt file 

## Run commands

- `kubectl -apply f .\redis.yaml`
- `kubectl -apply f .\fastApi.yaml`
- `kubectl -apply f .\fastapi-hpa.yaml`

## Additional K8s cmd for help
 - logs `kubectl logs`
 - All deployment `kubectl get deployment`
 - All service `kubectl get service`
 - All pods `kubectl pods`
 - Delete deployment `kubectl delete deployment <name>`
 - Delete service `kubectl delete service <name>`

## API Endpoints :

- `POST/apis/v1/store`:store key value in redis and run asyn task in huey
- `GET/apis/v1/retrieve`:retrieve value form the store of given key
- `DELETE/apis/v1/delete`:delete the key form store

## Some Img of FastApi redoc


