# sample-project

> A simple Flask web service running via Docker Compose. It provides RESTful api to work with user information.

### Reqirements
* Docker 19.03.0+
* Docker Compose 

### How to run?
1. Clone or download the project.
```
git clone https://github.com/dcfrost71/sample-project.git
```
2. Change directory into the project.
3. Use Docker Compose to start the web service.
```
docker compose --env-file ./env.example up
```
> `--env-file ./env.example` The file includes environment variables for docker-compose.yml.
4. Nice! You can get the service run-time information from your terminal.
You can access http://localhost:8123/user_list to get all of the users.

### API Reference
* Get all users
> $USER_ID is the key of the result dictionary. 
```
curl -X GET \
  http://localhost:8123/user_list
```

* Create a user
```
curl -X POST \
  http://localhost:8123/user_list \
  -H 'content-type: application/json' \
  -d '{	
	"name": "dawson",
    "job_title": "devops",
    "communicate_information": {
        "email": "dawson@email.addr",
        "mobile": "0900000000"
    }
}'
```

* Get a user information
```
curl -X GET \
  http://localhost:8123/user/${USER_ID}
```

* Update a user information
```
curl -X PUT \
  http://localhost:8123/user/${USER_ID} \
  -H 'content-type: application/json' \
  -d '{
    "name": "dawson",
    "job_title": "DevOps",
    "communicate_information": {
        "email": "dawson@my.email",
        "mobile": "0911111111"
    }
}'
```

* Delete a user information
```
curl -X DELETE \
  http://localhost:8123/user/${USER_ID}
```

### Docker Compose Environment
`flask`
* APP_PORT `default:80` Flask web service port
* APP_HOST `default:0.0.0.0` Flask web service host
* APP_ENV `default:development` Flask web service env, same as FLASK_ENV

`host`
* HOST_PORT `default:8123` The port exposes on the host machine
* CONTAINER_NAME `default:dawson-sample-project` The name of the container
* IMAGE_NAME `default:dawson-sample-project` The docker image name of the container
* IMAGE_TAG `default:LATEST` The docker image tag of the container