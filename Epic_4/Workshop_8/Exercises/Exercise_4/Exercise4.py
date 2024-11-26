import requests
import os
from dotenv import load_dotenv

load_dotenv()

TINYURL_API_URL = "https://api.tinyurl.com/create"
API_KEY = os.getenv("TINYURL_API_KEY")

def shorten_url(long_url):
    try:
        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "url": long_url,
            "domain": "tiny.one"
        }
        response = requests.post(TINYURL_API_URL, headers=headers, json=payload)
        response.raise_for_status()
        short_url = response.json()["data"]["tiny_url"]
        return short_url
    except requests.exceptions.RequestException as err:
        print(f"Error shortening URL: {err}")
        return None

def main():
    print("Welcome to the TinyURL Shortener CLI!")
    long_url = input("Enter the URL you want to shorten: ").strip()

    # Validate the URL (basic validation)
    if not (long_url.startswith("http://") or long_url.startswith("https://")):
        print("Invalid URL. Please ensure it starts with 'http://' or 'https://'.")
        return

    # Call the shorten_url function
    short_url = shorten_url(long_url)
    if short_url:
        print(f"Shortened URL: {short_url}")
    else:
        print("Failed to shorten the URL. Please try again.")

if __name__ == "__main__":
    main()
