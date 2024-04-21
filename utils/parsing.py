from bs4 import BeautifulSoup
from operator import attrgetter, itemgetter
from tqdm import tqdm
import requests 
import re 

def getHTMLdocument(url):   
    response = requests.get(url) 
    return response.text 

def parsePageArticles(url):
    doc = getHTMLdocument(url)
    soup = BeautifulSoup(doc, 'html.parser') 
    desc = soup.find_all('div', itemprop='d4d7f9cef4 df068f8f97')
    texts=[]
    for paragraph in soup.find_all('div',  attrs={'class': 'd4d7f9cef4 df068f8f97'}): 
        if paragraph.find('p') is None:
            continue
        else:
            cleaned_text = re.sub(r'[^\w\s]', '', paragraph.text) 
            cleaned_text = re.sub(r'\s+', ' ', cleaned_text) 
            texts.append(cleaned_text)

    return '. '.join(texts)
