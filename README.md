# api-utils
Utilities exposed as a REST API, motorized by FastAPI.

# Configure workspace
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Run locally
This code runs locally:
* as "raw" Python code (FastApi only, no Azure function, no container)
* as an Azure function (embedding FastApi, no container)
* as a container (embedding Azure function code, embedding FastApi)


## As "raw" Python code (dev)
```
python runlocal.py
```
The code will run one worker. It will reload on file modification.

Url is: `http://localhost:8000/`

## As an Azure Function
```
func start
```
Url is: `http://localhost:7071/`

## As a container
```
docker build --tag apiutils .

docker run -p 8000:80 -it apiutils
```
Url is `http://localhost:8000/`

# API Docs
Browse `http://localhost:8000/docs`, `http://localhost:7071/docs` or `http://localhost:8080/`


# Run on Azure
This code runs on Azure:
* as an Azure function
* as an Azure function in a container

## 
1. init

   ` sh azure-init.sh`
2. deploy local code to azure function

   `sh deploy.sh`
3. destroy the resource group

   `sh azure-clean.sh`

## TODO ajouter les commandes pour déployer le conteneur dans Azure






