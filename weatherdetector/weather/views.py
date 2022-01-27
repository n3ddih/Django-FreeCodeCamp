from django.http import response
from django.shortcuts import render
import json
import urllib.request, urllib.parse

# Create your views here.
def index(request):
	api_id = "5d5d622abad046db360656684d6891e1"
	data = {}
	if request.method == 'POST':
		city = request.POST['city'] # name in the input tag
		params = {
			'q': city,
			'appid':api_id,
		}
		url = 'http://api.openweathermap.org/data/2.5/weather?'+urllib.parse.urlencode(params)
		try:
			res = urllib.request.urlopen(url).read()
			json_data = json.loads(res)
			data = {
				'name' : str(json_data['name']),
				'country_code': str(json_data['sys']['country']),
				'coordinate' : str(json_data['coord']['lon'])+', '+str(json_data['coord']['lat']),
				'weather' : str(json_data['weather'][0]['description']),
				'weather_icon' : str(json_data['weather'][0]['icon']),
				'temp' : str(float(json_data['main']['temp']) - 273.15) + '°C',
				'pressure' : str(json_data['main']['pressure']) + 'hPa',
				'humidity': str(json_data['main']['humidity']) + '%',
			}
		except: data = {'msg' : 'city not found'}
	
	return render(request, 'index.html', data)