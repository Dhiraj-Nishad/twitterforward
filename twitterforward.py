import tweepy
from telethon import TelegramClient
import asyncio
import time

# Twitter API credentials
BEARER_TOKEN = 'AAAAAAAAAAAAAAAAAAAAAEn9yQEAAAAAB8gWlDngigGQzDDvl25vMHE6pTE%3DIoYaAu0IUGLGum0MizBxUbB8nrKCvWMzZwLvGA2dsKVy6JjbNp'  # Your actual bearer token

# Telegram API credentials
API_ID = 29199461  # Your API ID from my.telegram.org
API_HASH = '5d5c0797293505649aaa30aa8d1af14a'  # Your API Hash from my.telegram.org
PHONE_NUMBER = '919076273328'  # Your phone number (with country code)
TARGET_USER_ID = '@buybottttt'  # The targeted Telegram username

# Set up Telegram client
telegram_client = TelegramClient('session_name', API_ID, API_HASH)

async def send_message_to_telegram(message):
    async with telegram_client:
        await telegram_client.start(phone=PHONE_NUMBER)
        await telegram_client.send_message(TARGET_USER_ID, message)

def forward_tweets():
    last_tweet_id = None

    while True:
        try:
            client = tweepy.Client(bearer_token=BEARER_TOKEN)
            response = client.get_users_tweets(id='godofhell__', max_results=5)  # Using username directly
            
            if response.data:
                for tweet in response.data:
                    if last_tweet_id is None or tweet.id > last_tweet_id:
                        asyncio.run(send_message_to_telegram(tweet.text))
                        last_tweet_id = tweet.id
            
            # Wait for 1 minute after fetching and forwarding tweets
            time.sleep(60)  # Wait for 1 minute before checking for new tweets
        
        except tweepy.errors.TooManyRequests as e:
            print(f"Rate limit exceeded: {e}. Waiting for reset.")
            time.sleep(15 * 60)  # Wait for 15 minutes before retrying
        except Exception as e:
            print(f"An error occurred: {e}")
            break  # Exit loop on other errors

if __name__ == "__main__":
    forward_tweets()
