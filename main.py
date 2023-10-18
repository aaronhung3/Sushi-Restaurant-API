from fastapi import FastAPI, APIRouter
from requests import *
from typing import Optional


app = FastAPI(title="Sushi Restaurants API", openapi_url="/openapi.json")

api_router = APIRouter()

API_key="AIzaSyC76LufLw4-PC66ceSFgz3U7SYJklRt3GU"
base_url='https://maps.googleapis.com/maps/api/place/autocomplete/json?'
location_url = 'https://maps.googleapis.com/maps/api/geocode/json?'

app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")