import requests

url = "https://www.google.com"

try:
    response = requests.get(url)

    if response.status_code == 200:
        print("Application Status: UP")
    else:
        print("Application Status: DOWN")

    print("HTTP Status Code:", response.status_code)

except requests.exceptions.RequestException:
    print("Application Status: DOWN")