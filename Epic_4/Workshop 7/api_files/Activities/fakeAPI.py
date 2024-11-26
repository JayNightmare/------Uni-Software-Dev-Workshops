import requests
import json

base_url = "https://jsonplaceholder.typicode.com"
user_id = 6

def fetch_data(endpoint, params=None):
    """Fetch data from a given JSONPlaceholder endpoint."""
    try:
        response = requests.get(f"{base_url}/{endpoint}", params=params)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    return []

# Fetch posts
print("Fetching posts...")
posts = fetch_data("posts", {"userId": user_id})
if posts:
    print("\nPosts by user:")
    for post in posts[:5]:  # Display first 5 posts
        print(f"- {post['title']}")

# Fetch to-dos
print("\nFetching to-dos...")
todos = fetch_data("todos", {"userId": user_id})
if todos:
    print("\nTo-dos by user:")
    for todo in todos[:5]:  # Display first 5 to-dos
        status = "Completed" if todo["completed"] else "Pending"
        print(f"- {todo['title']} ({status})")

# Fetch albums
print("\nFetching albums...")
albums = fetch_data("albums", {"userId": user_id})
if albums:
    print("\nAlbums by user:")
    for album in albums[:5]:  # Display first 5 albums
        print(f"- {album['title']}")
