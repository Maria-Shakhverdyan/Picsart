import requests

'''Problem: Write a script to send a GET request to https://jsonplaceholder.typicode.com/invalid-url
using the requests module. Implement error handling to catch and print status codes and error messages if the request fails.
'''

try:
    responce = requests.get('https://jsonplaceholder.typicode.com/invalid-url')
    responce.raise_for_status()

except requests.exceptions.HTTPError as http_err:
    print(f"HTTP error occured: {http_err} (Status code: {responce.status_code})")

except requests.exceptions.RequestException as err:
    print(f"Other error occured: {err}")