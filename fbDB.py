import firebase_admin
from firebase_admin import db

cred_obj = firebase_admin.credentials.Certificate('mlhpridehack-firebase-adminsdk-4dqko-259de47b46.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL':'https://mlhpridehack-default-rtdb.asia-southeast1.firebasedatabase.app/'})

ref = db.reference("/Records")
import json
with open("data_test.json", "r") as f:
	file_contents = json.load(f)

for key, value in file_contents.items():
	ref.push().set(value)