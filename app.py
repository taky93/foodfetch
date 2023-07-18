from Api.food import Nosalty

import logging
import argparse

#Object instatiate
app = Nosalty()
logging.basicConfig(format='%(levelname)s:%(message)s',level=logging.DEBUG)
keywords = ['save','single']
#App logic

parser = argparse.ArgumentParser()

parser.add_argument('-s','--single',metavar="",help="Fetch single food")

args = parser.parse_args()

if args.single:
    print(app.listOfFoods(args=args.single))