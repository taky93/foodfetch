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
        
    def fetch_data(self,args=sys.argv):
        if len(args) > 3:
            self.search = args[1]
            print(f"Given argument: {str(args[1])}")
        elif args[1] == 'single':
            print('You picked single search!')
            self.search = input('Search term:')
        else:
            print('Give "random" command for random search or write in any food for search.')
            self.search = input("Search term:")
        if self.search == 'random':
            res = requests.get(self.url + self.randomizeFood())
        else:
            res = requests.get(self.url + self.search)
        soup = BeautifulSoup(res.content, 'html.parser')

        titles = soup.find_all('a', class_='m-articleCard__headline -smallArticle a-link mb-6')
        urls = soup.find_all('a', class_='m-articleCard__headline -smallArticle a-link mb-6')
        return titles , urls


    def listOfFoods(self):
        title = []
        url = []
        
        titles , urls = self.fetch_data()
        for t in titles:
            title.append(t.text)
        for u in urls:
            url.append(str(self.url + u['href'][8:]))

        df = pd.DataFrame({'Title': title, 'Url': url})


        print(df)
        return df.to_csv()

    def singleFood(self):
        raw_url = 'https://www.nosalty.hu'
        i = 1
        title = []
        url = []
        ingredient = []
        titles , urls = self.fetch_data()
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
        single_title = soup.find('h1' , class_='p-article__title -recipe pt-8 mb-5 d-block').text
        ingredients = soup.find_all('li',class_='m-list__item p-2 -dotted -fontSize-16 d-flex justify-content-between pl-5')
        print("anyád")
        return single_title , ingredients
        #---------------#
    def randomizeFood(self):
        food_list = ['paprikás' , 'csirke' , 'kacsa', 'sertés','palacsinta']
        return random.choice(food_list)

    def save_recepies(self,recepies,args=sys.argv):
        try:
            if args[2] == 'save':
                file_name = str(date.today()) + str(self.search).capitalize().strip() + '.csv'
                full_path = os.path.join("Receptek" , file_name)

                with open(full_path,"w") as file:
                    file.write(recepies)
                print(f'Saved as {file_name}')
        except IndexError:
            return 'Fetch without save'
#app = Nosalty()

#print(app.singleFood())