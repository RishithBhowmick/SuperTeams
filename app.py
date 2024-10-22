from fastapi import FastAPI,HTTPException,Response
from image import ImageRequest,Image
from utils import setup


app = FastAPI()
config_vars = setup()

@app.get("/ping")
def ping():
    return "pong"


@app.post("/image/generate")
def generate(body: ImageRequest):
    try:        
        image_handler = Image(config_vars)
        image = image_handler.generate(body.prompt)        
        return Response(content=image,media_type="image/png")
    except Exception as e:
        print(e)
        raise HTTPException(status_code=500,detail=str(e.__traceback__.tb_lineno))
    


