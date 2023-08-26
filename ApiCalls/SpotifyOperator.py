import requests
from dotenv import load_dotenv
import os
load_dotenv('.env')

#Pode ser que volte trackName igual mas URI diferentes
#Definir limit de returns
class SpotifyOperator:

  def __init__(self):
    self.token = None
    self.uri = None
    self.music = None
    self.query = None

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
    trackNameList = []
    trackUriList = []
    url = os.environ['SPOTIFY-URI-URL']
    payload = {}
    params = {"query":query, "type":"track", "market":"US","limit":"6", "offset":"0"}
    headers = {'Authorization': "Bearer " + str(self.token)}
    response = requests.request("get", url, headers=headers, params=params, data=payload).json()
    response = response['tracks']['items']
    for x in range(len(response)):
      trackNameToList = response[x]['name']
      trackUriToList = response[x]['uri']
      trackNameList.append(trackNameToList)
      trackUriList.append(trackUriToList)
    self.tracks = trackNameList
    self.uri = trackUriList
    #return JSON
    #return base64 of images