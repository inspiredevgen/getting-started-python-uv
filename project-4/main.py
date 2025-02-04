from fastapi import FastAPI, Body
from fastapi.responses import RedirectResponse
from datasource import CARS
from random import choice

app = FastAPI()

@app.get("/")
async def home():
    return RedirectResponse(url='/docs')

@app.get("/health")
async def health_check():
    return {"status": "UP"}

@app.get("/version")
async def get_version():
    return {"appVersion": "0.1", "release":"27-12-2024", "author": "Adi Bal-Mayel"}

@app.get("/cars")
async def get_all_cars():
    return CARS

@app.get("/random_car")
async def get_random_car():
    return {'car': choice(CARS)}

@app.get("/cars/{car_brand}")
async def get_cars_by_brand(car_brand: str):
    cars_to_return = []
    for car in CARS:
        if car.get('brand').casefold() == car_brand.casefold():
            cars_to_return.append(car)
    if cars_to_return:
        return cars_to_return
    else:
        return {"result": "Not found!"}

@app.get("/cars/")
async def get_car_by_city(city: str):
    cars_to_return = []
    for car in CARS:
        if car.get('city').casefold() == city.casefold():
            cars_to_return.append(car)
    if cars_to_return:
        return cars_to_return
    else:
        return {"result": f"No car found in {city}"}


@app.get("/cars/{brand}/")
async def get_car_by_brand_query(brand: str, model: str):
    cars_to_return = []
    for car in CARS:
        if (car.get('brand').casefold() == brand.casefold()) and (car.get('model').casefold() == model.casefold()):
            cars_to_return.append(car)
    if cars_to_return:
        return cars_to_return
    else:
        return {"result": f"No car found for: {brand} {model}"}

@app.get("/cars/byprovince/{province}")
async def get_cars_by_province(province: str):
    cars_by_province = []
    for car in CARS:
        if car.get('province').casefold() == province.casefold():
            cars_by_province.append(car)
    return cars_by_province

@app.get("/cars/city/{brand}/")
async def get_cars_by_city_path(city: str):
    cars_by_city = []
    for car in CARS:
        if car.get('city').casefold() == city.casefold():
            cars_by_city.append(car)
    return cars_by_city


@app.post("/car/new_car")
async def add_new_car(new_car=Body()):
    CARS.append(new_car)

@app.put("/car/update_car")
async def update_car(updated_car=Body()):
    for i in range(len(CARS)):
        if CARS[i].get('id_car').casefold() == updated_car.get('id_car').casefold():
            CARS[i] = updated_car

@app.delete("/car/delete_car/{car_id}")
async def delete_car(car_id: str):
    for i in range(len(CARS)):
        if CARS[i].get('id_car').casefold() == car_id.casefold():
            print(f">> Found car : {id_car}")
            CARS.pop(i)
            break
