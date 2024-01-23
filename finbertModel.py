from transformers import BertTokenizer, BertForSequenceClassification
import pandas as pd

# Load FinBERT model
model_name = "ProsusAI/finbert"
tokenizer = BertTokenizer.from_pretrained(model_name)
model = BertForSequenceClassification.from_pretrained(model_name)

# torch.save(model.state_dict(), 'model.pt')

mergedData = pd.read_csv("mergedData.csv")
headlines_list = mergedData['headline'].tolist()

output = []
batch_size = 32  # Adjust this based on your available memory
for i in range(0, len(headlines_list), batch_size):
    batch_headlines = headlines_list[i:i+batch_size]
    inputs = tokenizer(batch_headlines, padding=True, truncation=True, return_tensors='pt')
    outputs = model(**inputs)

    outputs_list = outputs.logits.tolist()
    for index in range(len(outputs_list)):
        sentiment_score = outputs_list[index][0] + outputs_list[index][2]*-1
        mergedData.loc[index+i, 'Sentiment_Score'] = sentiment_score
    
mergedData.to_csv("Sentiment_Score.csv", index=False)

    

