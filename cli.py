from Api.food import Nosalty
import logging
import argparse
import pandas as pd
class Cli:
    def __init__(self):
        self.app = Nosalty()
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
        self.keywords = ['save', 'single']
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-f', '--fetch', metavar="", help="Fetch list of food")
        self.parser.add_argument(
         '-s', '--single', help="Pick single food", action='store_true')
        self.parser.add_argument('-sv' , '--save', help='Save to csv',action='store_true')
        self.args = self.parser.parse_args()

    def run(self):

        if self.args.fetch and self.args.single:
            title, ingredients = self.app.singleFood(args=self.args.fetch)
            print(title)
            for i in ingredients:
                print(i)
            
            
            if self.args.save:
                txt_file = "".join((str(self.args.fetch),'.txt'))
                with open(txt_file,"w",encoding='utf-8') as file:
                    file.write(title + "\n")
                    for i in ingredients:
                        file.write(i+'\n')
                print("Saved as " + txt_file)   
                

        else:
            print(self.app.fetchFood(args=self.args.fetch))





if __name__ == "__main__":
    app = Cli()
    app.run()
