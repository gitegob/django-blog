import urllib.request
from django.shortcuts import render
from django.conf import settings
import json

# Create your views here.


def index(request):
    if request.method == 'POST':
        city = request.POST['city']
        try:
            res = urllib.request.urlopen(
                'https://api.openweathermap.org/data/2.5/weather?q='+city+'&appid='+settings.WEATHER_API_KEY).read()
            json_data = json.loads(res)
            data = {
                'country_code': str(json_data['sys']['country']),
                'coordinates': str(json_data['coord']['lon'])+' '+str(json_data['coord']['lat']),
                'temp': str(json_data['main']['temp'])+' K',
                'pressure': str(json_data['main']['pressure']),
                'humidity': str(json_data['main']['humidity'])
            }
        except Exception as e:
            print('Error:', e)
            data = {}
    else:
        city = ''
        data = {}
    return render(request, 'weather_index.html', {'city': city,  'data': data})
