from api.food import Nosalty
import logging
import argparse

# Object instatiate
app = Nosalty()
logging.basicConfig(format='%(levelname)s:%(message)s', level=logging.DEBUG)
keywords = ['save', 'single']
# App logic

parser = argparse.ArgumentParser()

parser.add_argument('-f', '--fetch', metavar="", help="Fetch list food")
parser.add_argument(
    '-s', '--single', help="Pick single food", action='store_true')

args = parser.parse_args()


def main():
    if args.fetch and args.single:
        title, ingredients = app.singleFood(args=args.fetch)
    print(title)
    for i in ingredients:
        print(i)
    if args.save:
        app.save_food(app.singleFood(args=args.fetch))
        print("Saved")
    else:
        print(app.fetchFood(args=args.fetch))


if __name__ == "__main__":
    main()
