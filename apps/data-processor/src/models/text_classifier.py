import torch
import torch.nn as nn
from transformers import AutoModel, AutoTokenizer
from .base_model import BaseModel

class TextClassifier(BaseModel):
    def __init__(self, model_name='bert-base-uncased', num_classes=2):
        super().__init__()
        self.bert = AutoModel.from_pretrained(model_name)
        self.tokenizer = AutoTokenizer.from_pretrained(model_name)
        self.classifier = nn.Linear(self.bert.config.hidden_size, num_classes)
        
    def predict(self, text):
        self.bert.eval()
        with torch.no_grad():
            inputs = self.tokenizer(text, return_tensors="pt", padding=True, truncation=True)
            outputs = self.bert(**inputs)
            logits = self.classifier(outputs.pooler_output)
            predictions = torch.softmax(logits, dim=1)
        return predictions.tolist()
    
    def train(self, texts, labels):
        # Training implementation
        pass 