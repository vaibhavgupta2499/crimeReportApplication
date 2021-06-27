'''report_new_loc'''

from lat_long_finder import get_lat_long
from location_finder import loc_find
import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('mlhpridehack-firebase-adminsdk-4dqko-259de47b46.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL':'https://mlhpridehack-default-rtdb.asia-southeast1.firebasedatabase.app/'})

def report_new_loc():
    loc=get_lat_long()
    place=str(loc_find(loc[0],loc[1]))
    print('Your location is '+place)
    ref = db.reference("/")
    dic={'record':{'lat':loc[0],'long':loc[1]}}

    for key, value in dic.items():
        ref.push().set(value)
