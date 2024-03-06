from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
import requests


def get_nearby_restaurants(latitude, longitude, radius=500):
    endpoint = "https://webservice.recruit.co.jp/hotpepper/gourmet/v1/"
    
    params = {
        "key": "7a48500c54c2ddb0",
        "lat": latitude,
        "lng": longitude,
        "range": radius,
        "format": "json"
    }

    response = requests.get(endpoint, params=params)
    data = response.json()

    restaurants = data.get("results", {}).get("shop", [])

    return restaurants

def index(request):
    # とりあえず東京駅の緯度経度を使用
    tokyo_station_lat = 35.681236
    tokyo_station_lng = 139.767125

    # 半径500m以内のレストランを取得
    restaurants = get_nearby_restaurants(tokyo_station_lat, tokyo_station_lng)
    return render(request, 'gourmet/index.html', {'restaurants': restaurants})


def detail(request, restaurant_id):
    
    return render(request, 'gourmet/detail.html',)
