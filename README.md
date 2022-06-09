# MINDS-Sentiment-Analysis

The project extracts the latest 10 news articles from https://www.aljazeera.com/where/mozambique/ and performs sentiment analysis (determining the emotional value of a given expression in natural language) on them using Flair. 

Choice of sentiment analysis library:
Flair was chosen as it functions better than Rule-based sentiment analysis which basically works based on a known database of words and the frequency of occureences. On the other hand Flair, is able to represent each word insides a vector space and correlate them. This inturn means that the sentiment is predicted based not just on the word but the context in which the word is used in the sentence i.e. Flair focusses on the meaning of the sentence.

Instructions to run the code:
1. install the requirements.txt using:
   pip install -r requirements.txt
2. run the main_file.py using:
   python main_file.py

Information about the dataframe and json file:
1. The dataframe was created using web scraping and extracting: article_link,article_title,published_date and article.
2. The dataframe was then sorted in descending order using the published_date to obtain the 10 latest articles.
3. The new dataframe comprising 10 articles is used to generate a json file comprising the article_title and the article.
