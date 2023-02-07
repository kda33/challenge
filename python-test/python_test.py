import requests

# URL of the microservice
url = "http://0.0.0.0:5000"

# Send a GET request to the microservice
response = requests.get(url)

# Print the status code of the response
print(f"Status code: {response.status_code}")

# Print the content of the response
print(f"Response content: {response.content}")
