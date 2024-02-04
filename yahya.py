#WEB SCRAPING

from bs4 import BeautifulSoup
import requests
import pandas as pd


link=("https://m.islamqa.info/en/answers/448903/repetition-of-stories-in-the-quran-with-different-wording")
r = requests.get(link)
htmlContent = r.content
print(htmlContent)
soup = BeautifulSoup(htmlContent, 'html.parser')
#print(soup)
print(soup.prettify)
title = soup.find_all(class_="title is-4 is-size-5-touch")
print(title)
print(soup.getText())

Question=soup.find_all(class_="single_fatwa__question text-justified")
print(Question)
print(soup.getText())

Answer=soup.find_all(class_="single_fatwa__answer")
print(Answer)
print(soup.getText())

data=[[title,Question,Answer]]
data

df=pd.DataFrame(data,columns=["title","Question","Answer"])
print(df)
df.to_csv("demo.csv")
print("ok")