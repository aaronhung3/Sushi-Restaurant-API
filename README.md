# Sushi-Restaurant-API

Main Goal of the Project:
The goal of the project is to create a software web service that has a request protocol to query
established 3rd party internet services (i.e. Google Maps, etc.) to ingest, aggregate and form the 
restaurant list. 

The problem in question is to get descriptions/locations of sushi restaurants in a city through a 3rd party service and
display them according to what the user wants.

Requirements:
Use FastAPI, Postman, and a 3rd party internet service

Problems When Coding/Researching:
1. Choosing the right 3rd part internet service
   - the first choice was to use google maps, but after working with it for a bit of time, I realized that
     google maps isn't able to locate positions based on city names. While it is possible to do this with
     reverse geocoding/geocoding api, it is not as efficient as using YelpAPI.
2. Getting specific data that is needed from the requests
   - after being able to pull all the data response with the request module, the hard part was separating
     the data that I need and the data that I don't need. One solution was to create an empty list and append
     the information that I need into the list.

Lessons Learned:
1. How FastAPI, Postman works
2. What is API used for and how to code it
3. Understanding JSON structure
4. How to pull requests from 3rd party internet services

How to Run:
1. Clone the app.py file to your computer
2. Open it with a coding software
3. Get your own unique API key from Yelp Developers
4. Put your API Key in the "key.API_KEY" place
5. Run the program
6. Type "localhost:8000/docs" into your web browser URL
7. Type the city of where you want to find sushi restaurants

What's to Come:
- Coding a website that is able to function with the Sushi Restaurant API
