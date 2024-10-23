import json
from utils import setup
from fastapi import FastAPI, HTTPException, Response
from image import ImageRequest, TrainingRequest, Image


app = FastAPI()
config_vars = setup()


@app.get("/ping")
def ping():
    return "pong"


@app.post("/image/generate")
def generate(body: ImageRequest):
    try:
        if body.prompt == "":
            raise Exception("no prompt found")
        
        image_handler = Image(config_vars)
        image = image_handler.generate(body.prompt)

        return Response(content=image, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@app.post("/image/train")
def generate(body: TrainingRequest):
    try:
        if body.file_name=="" or body.new_model_name=="" or body.owner == "" or body.trigger_word == "":
            raise Exception("missing data in request",body)
        image_handler = Image(config_vars)
        training_status = image_handler.train(
            body.file_name, body.new_model_name, body.owner, body.trigger_word
        )
        
        return Response(
            content=json.dumps(training_status), media_type="application/json"
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
