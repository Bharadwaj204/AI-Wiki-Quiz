import requests
import json

# Test the generate_quiz endpoint
url = "http://127.0.0.1:8000/generate_quiz"
data = {
    "url": "https://en.wikipedia.org/wiki/Alan_Turing"
}

try:
    response = requests.post(url, json=data)
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        print("Success! Response:")
        print(json.dumps(response.json(), indent=2))
    else:
        print("Error Response:")
        print(response.text)
except Exception as e:
    print(f"Request failed: {e}")