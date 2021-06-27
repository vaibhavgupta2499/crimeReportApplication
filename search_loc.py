'''search_loc.py'''

from lat_long_finder import get_lat_long
from location_finder import loc_find
from dist_calc import dist_calc
import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('mlhpridehack-firebase-adminsdk-4dqko-259de47b46.json')


def search_loc():
    loc = get_lat_long()
    place = str(loc_find(loc[0], loc[1]))
    #print('Your location is ' + place)

    ref = db.reference("/")
    locs = ref.get()

    min=10000
    for key,value in locs.items():
        dis=dist_calc(loc[0],loc[1],value['lat'],value['long'])
        if(dis<min):
            min=dis
            danger_place_name=str(loc_find(value['lat'],value['long']))

    return([danger_place_name,dis])
