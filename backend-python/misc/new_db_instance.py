import firebase_admin
from firebase_admin import credentials, firestore

def new_db_instance():
    cred = credentials.Certificate("serviceAccountKey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db
