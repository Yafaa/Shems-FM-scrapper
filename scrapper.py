

# load packages
import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

page=1
base_url="https://www.shemsfm.net/fr/actualites/actualites/1/"
param_url = base_url  +str(page)
param_url

Type1="actualites_tunisie-news_news-nationales"
Type2="actualites_shems-news"
Type3="actualites_world-news"
Type4="agenda-culturel"

types=[Type1,Type2,Type3,Type4]

types

lenTotale=0

links=[]
while(page <10):
  response = requests.get(param_url) 
  print(param_url)
  response.status_code
  print(response.status_code)
  # get the HTML from the webpage
  html = response.content
  # convert the HTML to a Beautiful Soup object
  soup = BeautifulSoup(html, 'lxml')
  # Exporting the HTML to a file
  with open('page1.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))
  
  h= soup.find_all("h2", {"class" : "title" } )

  for element in h:
    a=element.find('a')
    links.append(a['href'])
  
  #for a in h.find_all('a', href=True):
  #   links.append(a['href'])
  
 
  
 
  print(page)
  page=page+1
  param_url = base_url  +str(page)

len(links)

links

type(links[0])

#Append needed Types to urlList
urlList =[]
for i in links:
  for t in types:
    if t in str(i):
     urlList.append(str(i))

urlList[:5]

#Check Url
for l in urlList:
  url="https://www.shemsfm.net"+l
  print(url)

#i=1


#while(i<50):
#  url1="/fr/actualites/actualites_world-news/"+str(i)
#  url2="/fr/actualites/actualites_shems-news/"+str(i)
#  if url1 in urlList or url2 in urlList:
#   urlList.remove(url1)
#    urlList.remove(url2)
#  i=i+1

#urlList

#urlList[0]

#urlList[1]

df= pd.DataFrame()
df

for l in urlList:
  url="https://www.shemsfm.net"+l
  response = requests.get(url) 
  print(url)
  response.status_code
  print(response.status_code)
  # get the HTML from the webpage
  html = response.content
  # convert the HTML to a Beautiful Soup object
  soup = BeautifulSoup(html, 'lxml')
  # Exporting the HTML to a file
  with open('page1.html', 'wb') as file:
    file.write(soup.prettify('utf-8'))

  dates=soup.find("div", {"class": "extraBar"})
  content=dates.find("span")
  #date done
  date=content.text
  Title=soup.find("h1",{"title lg-size color_til"})
  #Title Done
  titre=Title.text
  par=soup.find_all("p",{"style": "text-align: justify;"})
  contenu=""
  for p in soup.find_all('p'):
    contenu=contenu+p.text
  contenu = contenu.replace(u'\xa0',' ')
  a_row = pd.Series([url,date,titre,contenu])
  row_df = pd.DataFrame([a_row])
  df = pd.concat([row_df, df], ignore_index=True)

df.head()

#some_list = ['abc-123', 'def-456', 'ghi-789', 'abc-456','/////actualites_tunisie-news_news-nationale']
#matching = [s for s in some_list if "actualites_tunisie-news_news-nationale" in s]
#matching

df.shape

df.columns=["url","date","title","texte"]

df.head()

df['genre']=""

df.head()

df.to_csv('out.csv', index=False)
