import math
import sys
from bs4 import BeautifulSoup
import requests
import pandas as pd
from datetime import date
import random
import os
import time



class Nosalty:

    def __init__(self):
        self.url = 'https://www.nosalty.hu/kereses/recept/'
        
    def fetch_data(self,args):
        if args == "random":
            response = requests.get(self.url+self.randomizeFood())
        else:
            response = requests.get(self.url+args)
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
    
    #In progress
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
        except ValueError:
            return 'Only numbers allowed!!!'
        raw_res = requests.get(url[selection])
        raw_soup = BeautifulSoup(raw_res.content,"html.parser")
        food_url = raw_soup.find('a', class_='position-relative d-block')['href']

        res = requests.get(raw_url+food_url)
        soup = BeautifulSoup(res.content,'html.parser')
        #Working on this#
        single_title = soup.find('h1' , class_='p-article__title -recipe pt-8 mb-5 d-block').get_text(separator=" ")
        ingredients = soup.find_all('li',class_='m-list__item p-2 -dotted -fontSize-16 d-flex justify-content-between pl-5')
        
        for i in ingredients:
            ingredientz.append(i.get_text(separator=" ",strip=True))
        return single_title , ingredientz
        #---------------#
    def randomizeFood(self):
        food_list = ['paprikás' , 'csirke' , 'kacsa', 'sertés','palacsinta']
        return random.choice(food_list)
