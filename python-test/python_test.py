import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

session = requests.Session()
retry = Retry(total=5, backoff_factor=0.1, status_forcelist=[ 500, 502, 503, 504 ])
adapter = HTTPAdapter(max_retries=retry)
session.mount('http://', adapter)

response = session.get("http://172.17.0.2:5000")

print(response.text)
