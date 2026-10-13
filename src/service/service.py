import requests
class Service: 
   
    _instance = None
    def __init__(self): 
        raise RuntimeError("This is a Singleton. Call instance()")

    @classmethod
    def instance(cls):
        if cls._instance is None:
            cls._instance = cls.__new__(cls)
        return cls._instance

    def postJobDescription(self, prompt:str): 
        response = requests.post(
            "http://localhost:11434/api/generate", 
            json={
                "model": "qwen3:8b",
                "prompt": prompt,
                "think": False,
                "stream": False,
                "options": {
                    "temperature": 0,
                    "num_ctx": 4096,
                },
            },
            timeout=(5, 120),
        )
        response.raise_for_status()
        print(response.json()["response"])


        