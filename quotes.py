import goslate
import os
import pickle
from pyquery import PyQuery as pq

def generateQuotes(page):
  URL = "https://www.goodreads.com/quotes?page=%s" % page
  d = pq(url=URL)
  quotesStr = d('.quoteText').text()

  quotes = quotesStr.split(u'\u201c')
  quotes = [i.encode('ascii', 'ignore') for i in quotes]
  quotes = [i.split("  ") for i in quotes]

  return quotes

def getQuotes(page):
  fileName = 'quotes%s.pkl' % page
  if not os.path.exists(fileName):
    quotes = generateQuotes(page)
    with open(fileName, 'w') as f:
      pickle.dump(quotes, f)
  else:
    with open(fileName, 'r') as f:
      quotes = pickle.load(f)

  return quotes

if __name__ == '__main__':
  getQuotes(1)
