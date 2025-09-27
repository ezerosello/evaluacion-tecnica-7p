from fastapi import FastAPI, Query
import requests

app = FastAPI()

# Función que consulta OpenWeatherMap
def get_weather(city: str, api_key: str):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "city": data["name"],
            "temperature": data["main"]["temp"],
            "description": data["weather"][0]["description"]
        }
    else:
        return {
            "error": "Ciudad no encontrada o API key inválida",
            "status_code": response.status_code,
            "message": response.text
        }

# Endpoint FastAPI
@app.get("/weather")
def weather(city: str = Query(..., description="Nombre de la ciudad")):
    api_key = "9a4e499d3f7bc641d86290a592416c6b"  # Tu API key personal
    return get_weather(city, api_key)



def get_country_data(name: str):
    url = f"https://restcountries.com/v3.1/name/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        return {
            "name": data[0]["name"]["common"],
            "region": data[0]["region"],
            "population": data[0]["population"]
        }
    else:
        return {"error": "País no encontrado"}


@app.get("/country_data")
def country_data(country: str):
    return (get_country_data(country))

# #########################################
# @app.get("/countries")
# def get_countries_by_region(region):
#     pass


# @app.get("/countries/stats")
# def get_stats(metric):
#     pass


# @app.get("/weather/{city}")
# def get_weather(city):
#     pass




# app = FastAPI()

# class Item(BaseModel):
#     text: str
#     is_done: bool = False

# items = []

# @app.get("/")
# def root():
#     return {"Hello":"World"}


# @app.post("/items")
# def create_item(item: Item):
#     items.append(item)
#     return items


# @app.get("/items")
# def list_items(limit: int = 10):
#     return items[0:limit]


# @app.get("/items/{item_id}", response_model=Item)
# def get_item(item_id: int) -> Item:
#     if item_id < len(items):
#         return items[item_id]
#     else:
#         raise HTTPException(status_code=404, detail="Item not found")
    





# ### ENDPOINTS EJERCICIO 1 ###