import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use the application default credentials

cred = credentials.Certificate("database-test-deee5-firebase-auth.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

doc_ref = db.collection(u'cars').document(u'truck')
doc_ref2 = db.collection(u'cars').document(u'truck2')

data = {
    u'model': u'beta',
    u'color': u'black',
    u'name': u'mscompany'
}

data2 = {
    u'model': u'alpha',
    u'color': u'white',
    u'name': u'mscompany'
}
doc_ref.set(data,merge=True)
doc_ref2.set(data2,merge=True)

