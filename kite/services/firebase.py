import base64
from ErrorCodes import STATUS_CODES 
import firebase
import firebase_admin
from firebase_admin import credentials, firestore,storage

fireConfig = {
"apiKey" : "AIzaSyDHP6GQhjz0uFtrnuFllumERl-HmGSA9kA",
    "authDomain" : "potfolio-492d3.firebaseapp.com",
    "databaseURL" : "https://potfolio-492d3-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId" : "potfolio-492d3",
    "storageBucket" : "potfolio-492d3.appspot.com",
    "messagingSenderId" : "1041514184898",
    "appId" : "1:1041514184898:web:d02a11cc9eac9cd6d7bb5b"
}

firebase_admin.initialize_app(credentials.Certificate('../../../Downloads/potfolio-492d3-firebase-adminsdk-c1s9v-a2c77c2b1c.json'),{'storageBucket': 'potfolio-492d3.appspot.com'})
# # firestore Quota: 1GB
store = firestore.client()
# storage=storage

fireApp = firebase.initialize_app(fireConfig)
# # Firebase Authentication Quota: 10k Active Users
fireauth = fireApp.auth()
# # firestore Quota: 1GB
# store = fireApp.firestore()
# # Storage Quota: 5GB
# storage= fireApp.storage()

def upload_image(file_path, file_stream, content_type):
    """
    Upload an image to Firebase Storage.

    Parameters:
    - file_path: The path where the file will be stored in Firebase Storage.
    - file_stream: A file-like object representing the image.
    - content_type: The content type of the image (e.g., 'image/jpeg', 'image/png').

    Returns:
    - The download URL of the uploaded image.
    """
    blob = storage.bucket().blob(file_path)
    blob.upload_from_file(file_stream, content_type=content_type)

    # Make the uploaded file publicly accessible
    blob.make_public()

    # Get the permanent download URL
    download_url = blob.public_url
    return download_url


