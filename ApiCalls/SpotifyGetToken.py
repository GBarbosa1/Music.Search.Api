import requests
from dotenv import load_dotenv
load_dotenv('.env')
class SpotifyToken:

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