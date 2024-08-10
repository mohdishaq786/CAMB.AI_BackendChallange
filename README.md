

## First run  pip install -r requirement.txt file 

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

- `POST/apis/v1/store`:store key value in redis and run asyn task in hueyss

- `POST/apis/v1/store`:store key value in redis and run asyn task in hueys
- `GET/apis/v1/retrieve`:retrieve value form the store of given keys
- `DELETE/apis/v1/delete`:delete the key form store

## Some Img of FastApi redoc
when use  run all command then on browser and hit `localhost/redoc`

# POST REQUEST
![Alt text](Screenshot%20(11).png)

# GET REQUEST
![Alt text](Screenshot%202024-03-06%20031010.png)

# DELETE REQUEST
![Alt text](Screenshot%202024-03-06%20031107.png)


## Test Api endpoints with Postman
- URL for `http://localhost/apis/v1/ `
- add key-value `http://localhost/apis/v1/store`
- Fetch value `http://localhost/apis/v1/retrieve`
- Delete key `http://localhost/apis/v1/delete` 

## Images
#post
![Alt text](Screenshot%202024-03-06%20032911.png)

#get
![Alt text](Screenshot%202024-03-06%20033254.png)

##FOR DETAIL PLEASE READ DOCUMENTATION FILE

## Note
 - Take the assumption for Redis data type in this application  I accept string at this time.
