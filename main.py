from fastapi import FastAPI
from pydantic import BaseModel
from ApiCalls.SpotifyOperator import  SpotifyOperator
spot = SpotifyOperator() 

app = FastAPI()
class Item(BaseModel):
    name: str| None = None
    trackUri: str| None = None
    imgBase64: str | None = None


class Message(BaseModel):
    text: str
    
@app.get("/Tracks/{query}")
def preco_amplo_total(query:str):
   query = query.split(',')
   spot.getToken()
   spot.getTrackUri(query)
   return spot.trackList


