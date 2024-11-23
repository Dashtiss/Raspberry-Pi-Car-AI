from ollama import Client

class CarAI:
    def __init__(self):
        self.client = Client("http://192.168.1.187:11434")
        
    def Get