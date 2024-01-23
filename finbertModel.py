from transformers import BertTokenizer, BertForSequenceClassification

# Load FinBERT model
model_name = "ProsusAI/finbert"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# Tokenize and encode text
text = "Your financial text goes here."
inputs = tokenizer(text, return_tensors="pt")

# Inference
outputs = model(**inputs)
logits = outputs.logits

# Interpret logits for classification results
print(logits)
