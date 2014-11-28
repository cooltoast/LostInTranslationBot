import goslate
import os
import pickle
from pyquery import PyQuery as pq

def generateQuotes():
  d = pq(url="https://www.goodreads.com/quotes?page=1")
  quotesStr = d('.quoteText').text()

  quotes = quotesStr.split(u'\u201c')
  quotes = [i.encode('ascii', 'ignore') for i in quotes]
  quotes = [i.split("  ") for i in quotes]

  return quotes

def getQuotes():
  if not os.path.exists('quotes.pkl'):
    quotes = generateQuotes()
    with open('quotes.pkl', 'w') as f:
      pickle.dump(quotes, f)
  else:
    with open('quotes.pkl', 'r') as f:
      quotes = pickle.load(f)

  return quotes

if __name__ == '__main__':
  getQuotes()
