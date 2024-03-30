import requests
import pandas as pd
import os

twitter_data = []

payload = {
    'api_key': 'd7467272410c7a7034b8c14c11a3195f',
    'query': "APT",  # the topic you want
    'num': '100'  # amount fetched
}

response = requests.get(
    'https://api.scraperapi.com/structured/twitter/search', params=payload)

data = response.json()

# Extract relevant tweet information from 'organic_results'
tweets = data['organic_results']

# Extract desired fields from each tweet
extracted_tweets = []
for tweet in tweets:
    extracted_tweet = {
        'title': tweet.get('title', '').split('/')[-1],  # Extracting title from displayed link
        'snippet': tweet.get('snippet', ''),  # Extracting snipper
        'highlighs': tweet.get('highlighs', ''), # Extracting list of relevant topics 
    }

    extracted_tweets.append(extracted_tweet)

# Convert the extracted tweet data to a DataFrame
df = pd.DataFrame(extracted_tweets)

# Save the DataFrame to a CSV file
# if file exists append the new data to the file

df.to_csv('twitter_data.csv', index=False, mode='a')

print("Data saved to twitter_data.csv")