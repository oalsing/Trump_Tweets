import io
import json
import re
import os.path
import zipfile

trump_folder = 'trump_tweet_data_archive/'

def read_file(filename):
    filename = trump_folder + filename + ".json"
    with open(filename) as f:
        l = f.readlines()
        data = l[0]
        data = data.replace("\n", "")
        js = json.loads(data)
        tweets = []
        for j in js:
            res = re.sub(r"http\S+", "", j['text'])
            res = res.replace('"', "")
            tweets.append(res)

        return tweets


def read_all_tweets():
    years = range(2009, 2018)
    all_tweets = []
    for y in years:
        file = 'condensed_%d' % (y)
        filepath = trump_folder + file + '.json'

        file_exists = False

        if os.path.isfile(filepath):
            print(filepath + ' exists')
            file_exists = True
        else:
            print(filepath + ' does not exist...')
            if os.path.isfile(filepath + '.zip'):
                print('zipped file does exist. Extracting...')
                zipfile.ZipFile(filepath + '.zip').extractall(trump_folder)
                file_exists = True

            else:
                print('zipped file does not exists. Continuing.')
                continue

        if file_exists:
            all_tweets += read_file(file)

    return preprocess_tweets(all_tweets)

def preprocess_tweets(tweets):
    p_tweets = [t for t in tweets if len(t) > 1]
    return p_tweets
