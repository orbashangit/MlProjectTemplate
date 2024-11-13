import torch
from transformers import BertTokenizer, BertForSequenceClassification

class BERTModel:
    def __init__(self, model_path):
        self.tokenizer = BertTokenizer.from_pretrained('bert-base-uncased')
        self.model = BertForSequenceClassification.from_pretrained('bert-base-uncased')
        self.model.load_state_dict(torch.load(model_path))

    def predict(self, text):
        inputs = self.tokenizer(text, return_tensors='pt')
        outputs = self.model(**inputs)
        return outputs.logits.argmax(dim=1).item()