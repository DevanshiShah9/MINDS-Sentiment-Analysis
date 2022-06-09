import numpy as np
from flair.models import TextClassifier
from flair.data import Sentence
import pandas as pd
from tqdm import tqdm
def text_sentiment_flair(text):
    classifier = TextClassifier.load('en-sentiment')
    sentence = Sentence(text)
    classifier.predict(sentence)
    if len(sentence.labels)>0:
        return sentence.labels[0].value
    else:
        return str(0)

def sentiment_analyzer(news_df):
    for i in tqdm(range(0, 100), initial = 0,
              desc ="Running Sentiment Analysis"):
        sentiment=[]
        for index,row in news_df.iterrows():
            article=row['article']
            positive=0
            negative=0
            sentences=article.split('.')
            sentences = pd.Series(list(filter(None, sentences)))
            predictions = sentences.map(lambda x : text_sentiment_flair(x))
            for i in predictions:
                if(i!='0'):
                    if(i=='POSITIVE'):
                        positive+=1
                    else:
                        negative+=1
            if(positive<negative):
                sentiment.append(-1)
            elif (positive==negative):
                sentiment.append(0)
            else:
                sentiment.append(1)
        news_df['sentiment']=sentiment
    return news_df
