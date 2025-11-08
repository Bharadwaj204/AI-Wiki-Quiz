import requests
import json

# Test the generate_quiz endpoint
def test_generate_quiz():
    url = "http://localhost:8001/generate_quiz"
    data = {
        "url": "https://en.wikipedia.org/wiki/Artificial_intelligence"
    }
    
    try:
        response = requests.post(url, json=data)
        print(f"Status Code: {response.status_code}")
        print(f"Response: {json.dumps(response.json(), indent=2)}")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    test_generate_quiz()