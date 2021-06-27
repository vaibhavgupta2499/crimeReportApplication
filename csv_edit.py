import pandas as pd
import firebase_admin
from firebase_admin import db
cred_obj = firebase_admin.credentials.Certificate('mlhpridehack-firebase-adminsdk-4dqko-259de47b46.json')
default_app = firebase_admin.initialize_app(cred_obj, {'databaseURL':'https://mlhpridehack-default-rtdb.asia-southeast1.firebasedatabase.app/'})
df=pd.read_csv('restaurant_dataSet.csv')
df=df.drop(columns=['Unnamed: 0', 'Neighborhood', 'Neighborhood Latitude','Neighborhood Longitude', 'Venue','Venue Category'],axis=1)
df = df.rename(columns={"Venue Latitude":"lat","Venue Longitude":"long"})
ref = db.reference("/")
for i,row in df.iterrows():
    dic={'record':{'lat':row[0],'long':row[1]}}
    for key,value in dic.items():
        ref.push().set(value)