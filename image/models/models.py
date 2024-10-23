from pydantic import BaseModel

class ImageRequest(BaseModel):
    prompt:str

class TrainingRequest(BaseModel):
    file_name:str
    new_model_name:str
    owner:str
    trigger_word:str