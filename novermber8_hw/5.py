import requests

'''Problem: Use the requests module to send a GET request to the URL https://jsonplaceholder.typicode.com/posts.
Retrieve posts by a specific user by adding a query parameter (e.g., ?userId=1).
Parse the JSON response and print the titles of the posts.
'''

try:
    responce = requests.get('https://jsonplaceholder.typicode.com/posts', params={'userId': 1})
    responce.raise_for_status()

    posts = responce.json()

    for post in posts:
        print(post['title'])

except requests.exceptions.RequestException as e:
    print(f"Error executing request: {e}")