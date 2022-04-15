import requests

headers = {
    'Accept': 'application/json, application/geo+json, application/gpx+xml, img/png; charset=utf-8',
}
call = requests.get('https://api.openrouteservice.org/v2/directions/driving-car?api_key=5b3ce35978511101cf6248f6dede3bef2a433aa4c0a8d00a1d9a0a&start=-73.96829224,40.76212692&end=-73.99295807,40.71379852', headers=headers)

print(call.status_code, call.reason)
print(call.text)





url = "https://maps.googleapis.com/maps/api/distancematrix/json?origins=40.74992371%2C-73.97306061&destinations=40.74789047%2C-73.98472595&key=AIzaSyDKIpNlGkqctkTPhqa8f-PiNhy_irQxo"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
