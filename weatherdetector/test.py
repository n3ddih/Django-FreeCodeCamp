import json
import urllib.request, urllib.parse

data = {}
api_id = "5d5d622abad046db360656684d6891e1"
# res = '{"coord":{"lon":105.8412,"lat":21.0245},"weather":[{"id":803,"main":"Clouds","description":"broken clouds","icon":"04d"}],"base":"stations","main":{"temp":308.15,"feels_like":313.06,"temp_min":308.15,"temp_max":308.15,"pressure":1003,"humidity":48,"sea_level":1003,"grnd_level":1001},"visibility":10000,"wind":{"speed":6.12,"deg":156,"gust":6.29},"clouds":{"all":53},"dt":1626251964,"sys":{"type":1,"id":9308,"country":"VN","sunrise":1626214992,"sunset":1626262879},"timezone":25200,"id":1581130,"name":"Hanoi","cod":200}'
# res = '{"cod":"404","message":"city not found"}'

city = 'Viet Nam'
params = {
	'q': city,
	'appid':api_id,
	}
url = 'http://api.openweathermap.org/data/2.5/weather?'+urllib.parse.urlencode(params)
try:
	res = urllib.request.urlopen(url).read()
	json_data = json.loads(res)
except: print("Not Found")
print(data)