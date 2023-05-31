import requests

from .base import Model


class Starcoder(Model):
    """
    Class that implements starcoder LLM code generation
    """

    def run(self, prompt):
        response = ""
        for _ in range(10):
            response = self.post(prompt)
            if response.count("</end>") > 1:
                break
        response.replace(str(prompt), "")
        return response

    _API_URL = "https://api-inference.huggingface.co/models/bigcode/starcoder"

    @property
    def model(self):
        return "starcoder"

    def post(self, prompt):
        header = {"Authorization": f"Bearer {self._secrets.get('starcoder_api_key')}"}
        payload = {"inputs": str(prompt)}
        print(payload)
        response = requests.post(self._API_URL, json=payload, headers=header)
        print(f"Response: {response.json()}")
        return response.json()[0]["generated_text"]
