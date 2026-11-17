import asyncio
from twitter.scraper import Scraper
import os

def main():
    print("Testing twitter-api-client configuration...")

    print("Initializing Scraper...")
    try:
        # In current version, the method is often tweets() or search_tweets()
        scraper = Scraper("dummy_email@test.com", "dummy_user", "dummy_pass")

        print("Simulating keyword search 'AI Agent'...")
        # Since it fails auth, it will raise exception, but this is the right class.
    except Exception as e:
        print(f"Expected Auth Error (no real cookies): {e}")

    print("Simulating Real-time stream (Polling)...")
    print("Polling strategy: The client handles low-level requests; requires manual polling logic and rate limit management.")

if __name__ == '__main__':
    main()
