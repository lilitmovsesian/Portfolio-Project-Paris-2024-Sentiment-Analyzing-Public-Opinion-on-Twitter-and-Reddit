import sqlite3
import pandas as pd
from textblob import TextBlob
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from sklearn import metrics

db = sqlite3.connect('./Reddit/posts.db')

df = pd.read_sql_query("SELECT * FROM posts", db)

# Convert to datetime
df['created_at'] = pd.to_datetime(pd.to_numeric(df['created_at']),  unit='s')

# Exclude Reddit posts that were created earlier than 22.07.2024
cutoff_date = pd.to_datetime('2024-07-22 00:00:00')
df = df[df['created_at']>=cutoff_date]

# Exclude Reddit posts that do not contain "Paris" or "2024" in 
# their title or text fields to narrow down the dataset to relevant posts only
df = df[df['title'].str.contains('paris', case=False) |
        df['title'].str.contains('2024') |
        df['text'].str.contains('paris', case=False) |
        df['text'].str.contains('2024')]

if df['text'].empty:
    df['sentiment_polarity'] = df['title'].apply(lambda x: TextBlob(x).sentiment.polarity  if pd.notnull(x) else 0)
    df['sentiment_subjectivity'] = df['title'].apply(lambda x: TextBlob(x).sentiment.subjectivity if pd.notnull(x) else 0)
    
else:
    df['sentiment_polarity'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity if pd.notnull(x) else 0)
    df['sentiment_subjectivity'] = df['text'].apply(lambda x: TextBlob(x).sentiment.subjectivity if pd.notnull(x) else 0)

average_polarity = df['sentiment_polarity'].mean()

print('Mean Polarity: ',average_polarity)
print('Mean Absolute Error:', metrics.mean_absolute_error(df['sentiment_polarity'], [average_polarity] * len(df)))
print('Mean Squared Error:', metrics.mean_squared_error(df['sentiment_polarity'], [average_polarity] * len(df)))
print('Root Mean Square Error:', np.sqrt(metrics.mean_squared_error(df['sentiment_polarity'], [average_polarity] * len(df))))

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.xlabel('Sentiment Polarity Score')
plt.ylabel('Frequency')
plt.title('Sentiment Polarity Distribution')
plt.hist(df['sentiment_polarity'], bins=50)
plt.grid(True)

plt.subplot(1, 2, 2)
plt.xlabel('Sentiment Subjectivity Score')
plt.ylabel('Frequency')
plt.title('Sentiment Subjectivity Distribution')
plt.hist(df['sentiment_subjectivity'], bins=50)
plt.grid(True)

plt.tight_layout()
plt.show()

plt.figure(figsize=(14, 6))

plt.subplot(1, 2, 1)
plt.scatter(df['sentiment_polarity'], df['sentiment_subjectivity'], alpha=0.7)
plt.xlabel('Sentiment Polarity')
plt.ylabel('Sentiment Subjectivity')
plt.title('Sentiment Polarity vs. Subjectivity')
plt.grid(True)

plt.subplot(1, 2, 2)
sns.regplot(x='sentiment_polarity', y='sentiment_subjectivity', data=df, scatter_kws={'alpha':0.5}, line_kws={'color':'red'})
plt.xlabel('Sentiment Polarity')
plt.ylabel('Sentiment Subjectivity')
plt.title('Sentiment Polarity vs. Subjectivity with Regression Line')
plt.grid(True)

plt.tight_layout()
plt.show()
