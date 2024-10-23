# SuperTeams Assignment 
This repository contains the assignment required as part of the Backend Developer role hiring process

This repository is a FastAPI application which implements 3 routes, namely:

1. Ping
2. Image Generation
3. Image model training

The repository is structured as follows:
```
SuperTeams
├──utils
│   ├── secrets.json
│   └── setup.py
├──image
│   ├── image.py
│   └──models
|       └──models.py
├──app.py
├──.gitignore
├──package.json
├──requirements.txt
├──data.zip
├──response.png
└──README.md
```

### Things to note:
The following application will required a replicate API token that needs to be generated on the `replicate` website. This will have to be added in `utils/secrets.json`

### Steps to run
1. Clone this repository:
```
git clone https://github.com/RishithBhowmick/SuperTeams.git
```

2. Navigate to this directory
```
cd ~/SuperTeams
```
3. Install the requirements
```
pip install requirements.txt
```
4. Start the application
```
fastapi dev app.py
```



## API Routes
### 1. Ping

**GET** `/ping`

- **Description:** Route to verify if the application is up and running


#### Example Request:
```bash
GET /ping
```
#### Response
```
pong
```

### 2. Image Generation
**POST** `/image/generate`
- **Description:** Generates and image given a prompt message
- **Request body:** 
  - `prompt` (required) - A string with the text of what kind of image needs to be generated

 Example Request
 ```
 POST /image/generate
 ```
 Request Body
 ```
 {
    "prompt": "cat driving a car in traffic"
 }
 ``` 
Response:
The response is an image sent via HTTP
![Logo](./response.png)


## 3. Training model with given data

This route trains a FLUX model given the data passed in the request.

**POST** `/image/train`
- **Description:** Trains a model given the data
- **Request body:** 
  - `file_name` (required) - The file name which contains all the data in zip form, present at the same level as app.py
  - `new_model_name` (required) - The model name where the trained model will be stored
  - `owner` (required) - Owner of the model. This will be the replicate account owner's github username
  - `trigger_word` (required) - A trigger word for required by the model to understand that the desired input images need to be trained against this word. 

 ### Example Request
 ```
 POST /image/train
 ```
 ### Request Body
 ```
 {
    "file_name":"",
    "new_model_name":"superteams-4",
    "owner":"rishithbhowmick",
    "trigger_word":"PATSY"
}
 ``` 

### Sample Response
```
{
    "id": "8n13jh44v5rm60cjpm9b06dhym",
    "model": "ostris/flux-dev-lora-trainer",
    "version": "e440909d3512c31646ee2e0c7d6f6f4923224863a6a10c494606e79fb5844497",
    "input": {
        "input_images": "https://api.replicate.com/v1/files/YzAwYjY5ZjQtZTI3OS00ZTU0LWI5YWItY2RiNWE0ZjY0MTFm/download?expiry=1729618342&owner=rishithbhowmick&signature=wfYrizthw%252BZt%252FQCZzUihFoGdeVswMHioHyHuZlg73UE%253D",
        "trigger_word": "PATSY"
    },
    "logs": "",
    "output": null,
    "data_removed": false,
    "error": null,
    "status": "starting",
    "created_at": "2024-10-22T16:32:22.745Z",
    "urls": {
        "cancel": "https://api.replicate.com/v1/predictions/8n13jh44v5rm60cjpm9b06dhym/cancel",
        "get": "https://api.replicate.com/v1/predictions/8n13jh44v5rm60cjpm9b06dhym"
    }
}
```