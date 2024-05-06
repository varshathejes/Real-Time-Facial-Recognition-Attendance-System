import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL':"https://face-recognition-cf432-default-rtdb.firebaseio.com/"
})

ref = db.reference('Faces')

data={
    "321654":{
        "name":"prabu",
        "major":"M.Sc Data Science",
        "starting_year":"2017",
        "total_attendance":6,
        "year":4,
        "last_attendance_time":"2024-03-17 00:54:34"
    },

    "852741":{
        "name":"emly",
        "major":"M.Sc Data Science",
        "starting_year":"2017",
        "total_attendance":6,
        "year":4,
        "last_attendance_time":"2024-03-17 00:54:34"
    },

    "963852":{
        "name":"elon",
        "major":"M.Sc Data Science",
        "starting_year":"2017",
        "total_attendance":6,
        "year":4,
        "last_attendance_time":"2024-03-17 00:54:34"
    },

    "203249":{
        "name":"thejes",
        "major":"M.Sc Data Science",
        "starting_year":"2020",
        "total_attendance":6,
        "year":4,
        "last_attendance_time":"2024-03-17 00:54:34"
    }
}

for key,value in data.items():
    ref.child(key).set(value)
