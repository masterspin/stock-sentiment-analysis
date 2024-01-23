import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

sentiment_score_csv = pd.read_csv("Sentiment_Score.csv").dropna()
from sklearn.model_selection import train_test_split

daily_returns = sentiment_score_csv[['dailyReturn']].values.reshape(-1,1)
sentiment_score = sentiment_score_csv[['Sentiment_Score']].values.reshape(-1,1)
X_train, X_test, y_train, y_test = train_test_split(
sentiment_score, daily_returns, test_size=0.30, random_state=42)

regressor = LinearRegression()
regressor.fit(X_train, y_train)

y_pred = regressor.predict(X_test)
print(np.sum(y_pred - y_test)/len(y_pred))