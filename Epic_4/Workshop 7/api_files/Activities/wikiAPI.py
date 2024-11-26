import requests
import json

base_url = 'https://xtools.wmcloud.org/api/page/articleinfo'
# //
page_titles = ['Barack_Obama', 'Margaret_Thatcher', 'Gamal_Abdel_Nasser', 'Mahinda_Rajapaksa']
# //
language = "en"
project= "wikipedia.org"
# //

for title in page_titles:
    api_url = f"{base_url}/{language}.{project}/{title}"
    try:
        response = requests.get(api_url)
        response.raise_for_status()
        data = response.json()
        print(f"Page Title: {data['page']}")
        print(f"Watchers: {data['watchers']}")
        print(f"Page Views: {data['pageviews']}")
        print(f"Revisions: {data['revisions']}")
        print(f"Editors: {data['editors']}")
        print("\n")
    except requests.exceptions.HTTPError as e:
        print(f"HTTP Error: {e}")
    except json.JSONDecodeError as e:
        print(f"JSON Decode Error: {e}")
    except KeyError as e:
        print(f"Key Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
