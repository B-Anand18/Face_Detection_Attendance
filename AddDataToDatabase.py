import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred,{
    'databaseURL': ""
})

ref = db.reference('Students')

data = {

    "321654":
        {
            "name":"Murtaz Hassan",
            "major":"Robotics",
            "starting_year":2017,
            "total_attendance":6,
            "standing":"6",
            "year":4,
            "last_attendance_time":"2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emily Blunt",
            "major": "Economics",
            "starting_year": 2018,
            "total_attendance": 12,
            "standing": "15",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "AI",
            "starting_year": 2014,
            "total_attendance": 1,
            "standing": "1",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "120116":
        {
            "name": "B Anand",
            "major": "CSE",
            "starting_year": 2020,
            "total_attendance": 100,
            "standing": "999",
            "year": 4,
            "last_attendance_time": "2022-12-11 00:54:34"
        },



}

for key,value in data.items():
    ref.child(key).set(value)
