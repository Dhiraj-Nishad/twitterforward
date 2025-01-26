import tweepy
from telethon import TelegramClient
import asyncio
import time

# Twitter API credentials
TWITTER_CONSUMER_KEY = 'LimdXnhuXXgGC4IkXwMQ49Vt6'
TWITTER_CONSUMER_SECRET = 'wVJ8LSa3UiyhtROtlHpciFSdg8BnOM3rVeZG5G5EKLwTcXTUFt'
TWITTER_ACCESS_TOKEN = '1878805655211159552-f9RRNgOf9wXWT4pdjEjr57rFwN2DXt'
TWITTER_ACCESS_TOKEN_SECRET = 'C3ReRKNxZjsAI9HghxyyiMWpYLp9dW5wtP8Jl48hnQmab'

# Telegram API credentials
API_ID = 29199461  # Your API ID from my.telegram.org
API_HASH = '5d5c0797293505649aaa30aa8d1af14a'  # Your API Hash from my.telegram.org
PHONE_NUMBER = '919076273328'  # Your phone number (with country code)
TARGET_USER_ID = '@buybottttt'  # The targeted Telegram username (replace with actual username)

# Set up Twitter API client
auth = tweepy.OAuth1UserHandler(TWITTER_CONSUMER_KEY, TWITTER_CONSUMER_SECRET,
                                TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_TOKEN_SECRET)
twitter_api = tweepy.API(auth)

# Set up Telegram client
telegram_client = TelegramClient('session_name', API_ID, API_HASH)

async def send_message_to_telegram(message):
    async with telegram_client:
        await telegram_client.start(phone=PHONE_NUMBER)
        await telegram_client.send_message(TARGET_USER_ID, message)

def forward_tweets():
    last_tweet_id = None

    while True:
        tweets = twitter_api.user_timeline(screen_name='godofhell__', count=5, tweet_mode='extended')
        
        for tweet in tweets:
            if last_tweet_id is None or tweet.id > last_tweet_id:
                asyncio.run(send_message_to_telegram(tweet.full_text))
                last_tweet_id = tweet.id
        
        time.sleep(60)  # Wait for 1 minute before checking for new tweets

if __name__ == "__main__":
    forward_tweets()
