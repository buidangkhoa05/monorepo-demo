from abc import ABC, abstractmethod
import torch

class BaseModel(ABC):
    def __init__(self):
        self.model = None
        
    @abstractmethod
    def predict(self, input_data):
        pass
    
    @abstractmethod
    def train(self, training_data):
        pass
    
    def save(self, path):
        if self.model is not None:
            torch.save(self.model.state_dict(), path)
    
    def load(self, path):
        if self.model is not None:
            self.model.load_state_dict(torch.load(path)) 