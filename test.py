import firebase_admin
from firebase_admin import credentials
from firebase_admin import storage

cred = credentials.Certificate(
    "./json/obungadiscordbot-firebase-adminsdk-mn0p0-3c97204428.json")
app = firebase_admin.initialize_app(cred, {
    'storageBucket': 'obungadiscordbot.appspot.com'
},  name='storage')

bucket = storage.bucket(app=app)
blob = bucket.blob("images")

print(blob.generate_signed_url(method='GET',))
