#!/usr/bin/python
import tweepy, time, sys
from textblob import TextBlob
import json
import random
import quotes as QuoteModule

def translateQuote(quote, language):
  t = TextBlob(quote)
  translated = t.translate(to=language)
  return translated.translate(to='en').string

def tweetQuote(page):
  data = open('keys.json')
  keys = json.load(data)
  data.close()

  auth = tweepy.OAuthHandler(keys["consumer_key"], keys["consumer_secret"])
  auth.set_access_token(keys["access_key"], keys["access_secret"])
  api = tweepy.API(auth)

  quotes = QuoteModule.getQuotes(page)
  if not quotes:
    return False

  while (len(quotes) > 0):
    languages = ['ja', 'zh-TW', 'ko', 'th', 'hi']
    language = random.choice(languages)
    print 'using language %s' % language
    quotePair = quotes.pop(random.randint(0, len(quotes)-1))

    if len(quotePair) is not 2:
      continue

    try:
      translated = translateQuote(quotePair[0], language)
      author = quotePair[1].split(",")[0]
      quote = "%s - %s" % (translated, author)
      api.update_status(quote)
      print "tweeted: %s" % quote
    except tweepy.TweepError as e:
      # dont stop if duplicate status happens
      print "TweepError: %s" % e
      continue
    except Exception as e:
      print "textblob.Error: %s" % e
      continue


    # tweet again in 20 min
    time.sleep(60*20)

  return True

if __name__ == '__main__':
  for i in range (101):
    tweetQuote(i)

