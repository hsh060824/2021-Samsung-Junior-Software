import pyrebase
import googlemaps

address = "경기도 가평군 설악면 미사리로 324-213"

firebaseConfig={"apiKey": "AIzaSyDzQPtXT0XNsllct2DYOpvkVq1utmdGlA8",
    "authDomain": "csidle-2021-junior.firebaseapp.com",
    "projectId": "csidle-2021-junior",
    "databaseURL": "https://csidle-2021-junior-default-rtdb.asia-southeast1.firebasedatabase.app/",
    "storageBucket": "csidle-2021-junior.appspot.com",
    "messagingSenderId": "821458174933",
    "appId": "1:821458174933:web:9ea12e985349b208b2b35c",
    "measurementId": "G-0DJEJJZ886"}

firebase = pyrebase.initialize_app(firebaseConfig)

db=firebase.database()

gmaps = googlemaps.Client(key='AIzaSyBKPKVSTLq_-zotnORmSEKMbqwFvMTna-w')
geocode_result = gmaps.geocode((address), language='ko')
list = geocode_result[0]
dict = list['geometry']
dict = dict['location']

lat = dict['lat']
lng = dict['lng']
print(lat, lng)

x = 3

def push(x):
    data={"name":"restaurant", "lat": lat, "lng": lng, "address": address, "nop": x}
    db.push(data)
