# import requests

# # URL of the microservice
# url = "http://0.0.0.0:5000"

# # Send a GET request to the microservice
# response = requests.get(url)

# # Print the status code of the response
# print(f"Status code: {response.status_code}")

# # Print the content of the response
# print(f"Response content: {response.content}")

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=5, backoff_factor=0.1, status_forcelist=[ 500, 502, 503, 504 ])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)

response = session.get("http://localhost:5000")

print(response.text)
