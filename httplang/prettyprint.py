import utils
from bs4 import BeautifulSoup as bs


def prettyprint(line):
    soup = bs(utils.typeDetermin(line[1]))
    prettyHTML = soup.prettify().encode('UTF-8')
    print prettyHTML
