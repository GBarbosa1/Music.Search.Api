
import requests
from dotenv import load_dotenv
load_dotenv('.env')

class SpotifyUri:

  def __init__(self):
    self.token = None

  def getToken(self):
    
    url = "https://accounts.spotify.com/api/token"
    payload = 'grant_type=client_credentials'
    headers = {
      'Authorization': 'Basic ',
      'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    self.token = response['access_token']


token = SpotifyToken()
token.getToken()
print(token.token)
import requests

url = "https://api.spotify.com/v1/search?query=baile do cinga&type=track&market=us&limit=50&offset=0"

payload = {}
headers = {
  'Authorization': 'Bearer BQAEFF1-3mcyl-aYa7AnvxkJFn4jRqsFx10WLYpRIFVOqimcn4t86aaaOOalyyKfCM-avK0TJaKH1daLnqKyL5bhC1nHt5jrccFW3SBhAGSwA-w66ok'
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
