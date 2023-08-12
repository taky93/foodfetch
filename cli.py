from Api.food import Nosalty
import logging
import argparse


class Cli:
    def __init__(self):
        self.app = Nosalty()
        logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
        self.keywords = ['save', 'single']
        self.parser = argparse.ArgumentParser()
        self.parser.add_argument('-f', '--fetch', metavar="", help="Fetch list of food")
        self.parser.add_argument(
         '-s', '--single', help="Pick single food", action='store_true')
        self.args = self.parser.parse_args()

    def run(self):

        if self.args.fetch and self.args.single:
            title, ingredients = self.app.singleFood(args=self.args.fetch)
            print(title)
            for i in ingredients:
                print(i)

        else:
            print(self.app.fetchFood(args=self.args.fetch))





if __name__ == "__main__":
    app = Cli()
    app.run()
