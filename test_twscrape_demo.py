import asyncio
from twscrape import API
import os

async def main():
    print("Testing twscrape configuration...")
    # Initialize the API which manages a local SQLite database for accounts
    api = API()

    # Normally we add an account to the pool like so:
    # await api.pool.add_account("username", "password", "email", "email_password", cookies={"auth_token": "...", "ct0": "..."})
    print("Pool system initialized. Simulating adding an account...")

    print("Simulating keyword search 'AI Agent'...")
    try:
        # The gather function fetches all results.
        # For real streams, one uses async generators.
        count = 0
        async for tweet in api.search("AI Agent", limit=10):
            print(tweet.id, tweet.user.username, tweet.rawContent)
            count += 1
        print(f"Found {count} tweets.")
    except Exception as e:
        print(f"Expected No Account/Auth Error: {e}")

    print("Simulating Real-time stream (Polling)...")
    print("Polling strategy: Twscrape manages proxies and account switching under the hood.")
    print("This allows much higher polling frequency across a pool of bot accounts.")

if __name__ == '__main__':
    asyncio.run(main())
