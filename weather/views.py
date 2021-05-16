import urllib.request
import requests
import json
from django.shortcuts import render, redirect
from .models import City
from .forms import CityForm

from urllib.request import Request, urlopen #from수정
from urllib.parse import urlencode, unquote, quote_plus #from수정

import pandas as pd

def index(request):
  url = 'http://api.openweathermap.org/data/2.5/weather?q={}&units=imperial&appid=3bda876e8cc924b7aa95b8db3cb7dafb'

  err_msg = ''
  message = ''
  message_class = ''

  if request.method == "POST":
    form = CityForm(request.POST)

    if form.is_valid():
      new_city = form.cleaned_data['name']
      existing_city_count = City.objects.filter(name=new_city).count()

      if existing_city_count == 0:
        r = requests.get(url.format(new_city)).json()

        if r['cod'] == 200:
            form.save()
        else:
            err_msg = 'City does not exist in this world!'
      else:
        err_msg = 'City already exists in the database!'

    if err_msg:
      message = err_msg
      message_class = "is-danger"
    else:
      message = "City added succesfully!"
      message_class = "is-success"

  form = CityForm()

  cities = City.objects.all()

  weather_data = []

  for city in cities:
    r = requests.get(url.format(city)).json()

    city_weather = {
      'city': city.name,
      'temperature':round((r["main"]["temp"]-32)*5/9, 2),
      'description': r["weather"][0]["description"],
      'icon': r["weather"][0]["icon"],
    }
    weather_data.append(city_weather)

  context = {
    'weather_data' : weather_data,
    'form' : form,
    'message' : message,
    'message_class' : message_class,
  }
  return render(request, 'weather.html', context)

def delete_city(request, city_name):
  City.objects.get(name=city_name).delete()
  return redirect('home')

def ko_weather(request):
  url = 'http://apis.data.go.kr/1360000/VilageFcstInfoService/getUltraSrtNcst'
  queryParams = '?' + urlencode(
    { quote_plus('ServiceKey') : 'Jpp57VnJpYmaRwehqiOkIiQArKUPSriqhsjo1Qmm138SgZVE4eeSJaF8%2BBkwWSubbIHLe1P%2BP%2FNQHhLncVdvUw%3D%3D', 
    quote_plus('pageNo') : '1', # 페이지 번호 // default : 1
    quote_plus('numOfRows') : '10', # 한 페이지 결과 수 // default : 10
    quote_plus('dataType') : 'JSON', # 응답자료형식
    quote_plus('base_date') : '20151201', # 발표일자 // yyyymmdd
    quote_plus('base_time') : '0600', # 발표시각 // HHMM, 매 시각 40분 이후 호출
    quote_plus('nx') : '18', # 예보지점 X 좌표
    quote_plus('ny') : '1' } # 예보지점 Y 좌표
  )

  request = urllib.request.META(url + unquote(queryParams))
  response_body = urlopen(request).read()
  data = json.loads(response_body)
  print("**************************")
  print(data)
  print("**************************")
  return render(request, 'ko_weather.html', data)