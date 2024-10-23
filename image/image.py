import replicate
import pickle
import json
import base64
import io
import os
import requests
from PIL import Image as ImageParser


class Image:
    def __init__(self, data):
        self.model = data.get("MODEL")
        self.upload_url = data.get("UPLOAD_URL")
        self.model_creation_url = data.get("MODEL_CREATION_URL")
        self.training_URL = data.get("TRAINING_URL")

    def generate(self, prompt: str):
        output = replicate.run(self.model, input={"prompt": prompt})
        return self.convert_to_image(output[0].read())

    def convert_to_image(self, byts: bytes):
        image_io = io.BytesIO(byts)
        image = ImageParser.open(image_io)

        png_byte_arr = io.BytesIO()
        image.save(png_byte_arr, format="PNG")

        png_byte_arr.seek(0)
        png_bytes = png_byte_arr.getvalue()
        return png_bytes

    def train(self, file_name: str, new_model_name: str, owner: str, trigger_word: str):
        try:
            file_url = self.upload_data(file_name)
            self.create_model(owner, new_model_name)

            payload = json.dumps(
                {
                    "destination": "%s/%s" % (owner, new_model_name),
                    "input": {"input_images": file_url, "trigger_word": trigger_word},
                }
            )
            headers = {
                "Authorization": "Bearer %s" % os.environ["REPLICATE_API_TOKEN"],
                "Content-Type": "application/json",
            }

            response = requests.request(
                "POST", self.training_URL, headers=headers, data=payload
            )
            response.raise_for_status()
            return response.json()

        except Exception as e:
            raise e

    def upload_data(self, file_path):
        payload = {}
        files = [
            ("content", ("file", open(file_path, "rb"), "application/octet-stream"))
        ]
        headers = {"Authorization": "Bearer %s" % os.environ["REPLICATE_API_TOKEN"]}

        response = requests.request(
            "POST", self.upload_url, headers=headers, data=payload, files=files
        )

        response.raise_for_status()
        return response.json().get("urls").get("get")

    def create_model(self, owner, new_model_name):
        payload = json.dumps(
            {
                "owner": owner,
                "name": new_model_name,
                "description": "Creating a model named %s" % new_model_name,
                "visibility": "private",
                "hardware": "gpu-t4",
            }
        )

        headers = {
            "Authorization": "Bearer %s" % os.environ["REPLICATE_API_TOKEN"],
            "Content-Type": "application/json",
        }

        response = requests.request(
            "POST", self.model_creation_url, headers=headers, data=payload
        )
        response.raise_for_status()
