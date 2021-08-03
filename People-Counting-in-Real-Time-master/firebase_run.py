import pyrebase
import googlemaps

def dequote(s):
    """
    If a string has single or double quotes around it, remove them.
    Make sure the pair of quotes match.
    If a matching pair of quotes is not found, return the string unchanged.
    """
    if (s[0] == s[-1]) and s.startswith(("'", '"')):
        return s[1:-1]
    return s

def push(num, inp, outp, name):
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
    geocode_result = gmaps.geocode((name), language='ko')
    list = geocode_result[0]

    add = list['formatted_address']
    dict = list['geometry']
    dict = dict['location']

    lat = dict['lat']
    lng = dict['lng']
    #print(lat, lng)

    add = dequote(add)
    name = dequote(name)

    all_users = db.child(name).get()
    all_users = all_users.val()
    data={"name": name, "lat": lat, "lng": lng, "formatted address": add, "nop": num, "inp": inp, "outp": outp}

    if all_users == "None":
        db.child(name).push(data)
    else:
        db.child(name).update(data)

#push(1, 1, 1, "에버랜드")
