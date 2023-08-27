import requests
from dotenv import load_dotenv
import os
import base64
import requests
import json

load_dotenv('.env')

#Pode ser que volte trackName igual mas URI diferentes
#Definir limit de returns
class SpotifyOperator:

  @staticmethod
  def get_as_base64(url):
    return base64.b64encode(requests.get(url).content)

  def __init__(self):
    self.token = None
    self.uri = None
    self.music = None
    self.query = None
    self.trackList = None

  #fazer pool de token
  def getToken(self):
    url = os.environ['SPOTIFY-TOKEN-URL']
    payload = os.environ['SPOTIFY-TOKEN-PAYLOAD']
    headers = {
      'Authorization': os.environ['SPOTIFY-CREDENTIALS-BASE64'],
      'Content-Type': os.environ['SPOTIFY-CONTENT-TYPE']
    }

    response = requests.request("POST", url, headers=headers, data=payload).json()
    self.token = response['access_token']

  def getTrackUri(self,query):
    trackList = []
    url = os.environ['SPOTIFY-URI-URL']
    payload = {}
    params = {"query":query, "type":"track", "market":"US","limit":"6", "offset":"0"}
    headers = {'Authorization': "Bearer " + str(self.token)}
    response = requests.request("get", url, headers=headers, params=params, data=payload).json()
    response = response['tracks']['items']
    for x in range(len(response)):
      trackNameToList = response[x]['name']
      trackUriToList = response[x]['uri']
      base64ToList = SpotifyOperator.get_as_base64(response[x]['album']['images'][0]['url'])
      artistToList = response[x]['album']['artists'][0]['name']
      trackList.append({"trackName":trackNameToList, "trackUri":trackUriToList, "trackArtist":artistToList})#,base64ToList])
    self.trackList = trackList
