import asyncio
from twikit import Client
import json
import os

# Create dummy cookies based on env vars or empty strings
cookies = {
    "auth_token": os.getenv("TW_AUTH_TOKEN", "dummy_token"),
    "ct0": os.getenv("TW_CT0", "dummy_ct0")
}
with open('cookies.json', 'w') as f:
    json.dump(cookies, f)

async def main():
    print("Testing twikit configuration...")
    client = Client('en-US')

    # We load the cookies directly
    client.set_cookies(cookies)

    print("Simulating keyword search 'AI Agent'...")
    try:
        # In a real scenario, this would search and return results
        tweets = await client.search_tweet('AI Agent', 'Latest')
        print(f"Found {len(tweets)} tweets.")
    except Exception as e:
        print(f"Expected Auth Error (no real cookies): {e}")

    print("Simulating Trends fetching...")
    try:
        trends = await client.get_trends('trending')
        print(f"Found {len(trends)} trends.")
    except Exception as e:
        print(f"Expected Auth Error (no real cookies): {e}")

    print("Simulating Real-time stream (Polling)...")
    print("Polling strategy: loop async search_tweet every N seconds and track seen tweet IDs.")

if __name__ == '__main__':
    asyncio.run(main())
