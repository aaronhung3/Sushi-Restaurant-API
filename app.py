from fastapi import FastAPI, APIRouter
from requests import *
import key;

app = FastAPI(title="Sushi Restaurants API", openapi_url="/openapi.json")
api_router = APIRouter()

HEADERS = {"Authorization": f"Bearer {key.API_KEY}"} #get your own API key!
base_url = "https://api.yelp.com/v3/businesses/search?"


@api_router.get("/", status_code=200)
async def root():
    return {"API": "Sushi Restaurants"}

@api_router.get("/restaurants/{city}", status_code=200)
async def get_restaurants(*, city: str):
    PARAMETER = {"location": f"{city}, US",
                 "term": "restaurants",
                 "categories": "sushi",
                 "radius": 10000,
                }
    
    response = get(base_url, params=PARAMETER, headers=HEADERS)
    data = response.json()

    restaurants = []
    for item in data["businesses"]:
        restaurants.append({
                "id": item["id"],
                "name": item["name"],
                "category": "sushi",
                "city": item["location"]["city"],
                "state": item["location"]["state"],
                "address": ", ".join(item["location"]["display_address"]),         
            })
        
    if len(restaurants) > 0:
        return restaurants
    else:
        return {"status": "No sushi restaurants were found"}

app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="debug")