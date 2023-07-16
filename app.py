from Api.food import Nosalty
import os
import sys
import time
import logging
import datetime

#Object instatiate
app = Nosalty()
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)
keywords = ['save','single']
#App logic

def main_menu():
    
    print('Food API by Taky \n')
    #Bullshit
    print(app.listOfFoods())
    input() #hahahah :D
    


    
main_menu()
