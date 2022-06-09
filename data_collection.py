from bs4 import BeautifulSoup
from dateutil.parser import parse
import requests
import pandas as pd
import os
import re
import json
from tqdm import tqdm

def get_dataframe():
    url="https://www.aljazeera.com/where/mozambique/"
    html_content = requests.get(url).text
    soup = BeautifulSoup(html_content, "lxml")
    #print(soup)

    for i in tqdm(range(0, 100), initial = 50,
              desc ="Web Scraping"):
        news_web= soup.find_all("h3", attrs={"class": "gc__title"})
        news_dates=soup.find_all("div",attrs={"class": "date-simple css-1yjq2zp"})
        news_df=pd.DataFrame(columns=["article_link", "article_title", "published_date"])
        i=0
        for news in news_web:
            data_dict = {"article_link": [news.a["href"]],"article_title": [news.text.encode("ascii", "ignore")],  "published_date": [parse(news_dates[i].select("span")[1].text)]}
            df = pd.DataFrame (data_dict)
            news_df= pd.concat([news_df, df], ignore_index=True)
            i+=1
        news_df=news_df.sort_values(by="published_date",ascending=False)[:10]   
    return news_df    

def add_articles():
    news_df=get_dataframe()
    articles=[]
    i=0
    for link in news_df["article_link"]:
        html_content = requests.get("https://www.aljazeera.com"+link).text
        soup = BeautifulSoup(html_content, "lxml")
        article_web=soup.find("div",attrs={"class": re.compile("wysiwyg wysiwyg--all-content css-[a-z0-9]")})
        s=""
        for p in article_web.select("p"):
            s+=p.text
        articles.append(s)
        i+=1
    news_df["article"]=articles 
    return news_df

def convert_to_json(news_df):
    news_df_json=news_df.drop(["article_link","published_date"], axis = 1)
    #path= os.path.abspath(os.getcwd())+"/articles.json"
    with open('articles.json', 'w', encoding='utf-8') as file:
        news_df_json.to_json(file,orient="records", force_ascii=False)
    print("Conversion to json successful")
    return