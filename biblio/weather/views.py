from django.shortcuts import render
import requests 
from .models import City
def home(request):
 url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=f07177d92a38e800935d3a4d6019c484'
 cities = City.objects.all() #return all the cities in the database

 weather_data = []

 for city in cities:

    city_weather = requests.get(url.format(city)).json() #request the API data and convert the JSON to Python data types

    weather = {
    'city' : city,
    'temperature' : city_weather['main']['temp'],
    'description' : city_weather['weather'][0]['description'],
    'icon' : city_weather['weather'][0]['icon']
    }

    weather_data.append(weather) #add the data for the current city into our list

 context = {'weather_data' : weather_data}

 return render(request, 'weather.html', context)