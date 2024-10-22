import replicate
import pickle
import json
import base64
import io
from PIL import Image as ImageParser

class Image:
    def __init__(self, data):
        self.model = data.get("MODEL")

    def generate(self, prompt: str):
        output = replicate.run(self.model, input={"prompt": prompt})        
        return self.convert_to_image(output[0].read())
    
    def convert_to_image(self,byts:bytes):
        image_io = io.BytesIO(byts)
        image = ImageParser.open(image_io)        

        png_byte_arr = io.BytesIO()
        image.save(png_byte_arr, format='PNG')          
        
        png_byte_arr.seek(0)        
        png_bytes = png_byte_arr.getvalue()
        return png_bytes

        
