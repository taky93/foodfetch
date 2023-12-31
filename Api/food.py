from bs4 import BeautifulSoup
import requests
import pandas as pd
import random
import numpy as np
from yaspin import yaspin

class Nosalty:

    def __init__(self):
        self.url = 'https://www.nosalty.hu/kereses/recept/'
        
    def fetch_data(self,args):
        if args == "random":
            response = requests.get(self.url+self.randomizeFood())
        else:
            response = requests.get(self.url+args)
        with yaspin(text='Fetching...') as spinner:
            soup = BeautifulSoup(response.content,'html.parser')
            titles = soup.find_all('a', class_='m-articleCard__headline -smallArticle a-link mb-6')
            urls = soup.find_all('a', class_='m-articleCard__headline -smallArticle a-link mb-6')
  
        return titles , urls

    def fetchFood(self,args):
        title = []
        url = []
        
        titles , urls = self.fetch_data(args)
        for t in titles:
            title.append(t.text)
        for u in urls:
            url.append(str(self.url + u['href'][8:]))

        df = pd.DataFrame({'Title': title, 'Url': url})
        return df

    def singleFood(self,args):
        raw_url = 'https://www.nosalty.hu'
        i = 1
        title = []
        url = []
        ingredientz = []
        titles , urls = self.fetch_data(args)
        for t in titles:
            title.append(t.text)
        for u in urls:
            url.append(self.url + u['href'][8:])
        for pick in title:
            print(f"{str(i)}.{pick}")
            i = i + 1
        try:
            selection = int(input(">>>")) - 1
            portions = int(input("Portions:"))
            
        except ValueError:
            return 'Only numbers allowed!!!'
        raw_res = requests.get(url[selection])
        raw_soup = BeautifulSoup(raw_res.content,"html.parser")
        food_url = raw_soup.find('a', class_='position-relative d-block')['href']

        res = requests.get(raw_url+food_url + f"?adag={portions}")
        soup = BeautifulSoup(res.content,'html.parser')
 
        single_title = soup.find('h1' , class_='p-article__title -recipe pt-8 mb-5 d-block').get_text(separator=" ")
        ingredients = soup.find_all('li',class_='m-list__item p-2 -dotted -fontSize-16 d-flex justify-content-between pl-5')
        
        for i in ingredients:
            ingredientz.append(i.get_text(separator=" ",strip=True))
        return single_title , np.unique(ingredientz)
        #---------------#
    def randomizeFood(self):
        food_list = ['paprikás' , 'csirke' , 'kacsa', 'sertés', 'palacsinta','torta','gulyás','pörkölt','leves','hal','tészta','pizza','hús','ramen','burger','rántott']
        return random.choice(food_list)
    
