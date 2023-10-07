#################
import requests #
import random   #
import time     #
#################


categories = ['age', 'alone', 'amazing', 'anger', 'architecture', 'art', 'attitude', 'beauty', 'best', 'birthday', 'business',
              'car', 'change', 'communications', 'computers', 'cool', 'courage', 'dad', 'dating', 'death', 'design', 'dreams',
              'education', 'environmental', 'equality', 'experience', 'failure', 'faith', 'family', 'famous', 'fear', 'fitness',
              'food', 'forgiveness', 'freedom', 'friendship', 'funny', 'future', 'god', 'good', 'government', 'graduation', 'great',
              'happiness', 'health', 'history', 'home', 'hope', 'humor', 'imagination', 'inspirational', 'intelligence', 'jealousy',
              'knowledge', 'leadership', 'learning', 'legal', 'life', 'love', 'marriage', 'medical', 'men', 'mom', 'money', 'morning',
              'movies', 'success']


MAX_RETRIES = 25
RETRY_DELAY = 2

def getQuote():

    # You can get a key by making an account on api-ninjas.com :)
    with open('apiKey.txt') as f:
        _API_KEY = f.read().strip()

    retries = 0
    while retries < MAX_RETRIES:
        category = random.choice(categories)
        _API_URL = 'https://api.api-ninjas.com/v1/quotes?category={}'.format(category)
        response = requests.get(_API_URL, headers={'X-API-Key' : _API_KEY})
        if response.status_code != requests.codes.ok:
            print ('Error:', response.status_code)
            retries += 1
            time.sleep(RETRY_DELAY)
            continue
        try:
            data = response.json()
            if not data:
                raise ValueError('No data returned')
            quote_data = data[0]
            putTogether = '"{}" - {}'.format(quote_data['quote'], quote_data['author'])
            if len(putTogether) > 270:
                raise ValueError('Quote too long')
            print(putTogether)
            return putTogether
        except ValueError as err:
            print(err)
            time.sleep(RETRY_DELAY)

    return None
