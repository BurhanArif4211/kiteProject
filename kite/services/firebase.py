import firebase, base64
from ErrorCodes import STATUS_CODES 
fireConfig = {
    "apiKey": "AIzaSyDHP6GQhjz0uFtrnuFllumERl-HmGSA9kA",
    "authDomain": "potfolio-492d3.firebaseapp.com",
    "databaseURL": "https://potfolio-492d3-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId": "potfolio-492d3",
    "storageBucket": "potfolio-492d3.appspot.com",
    "messagingSenderId": "1041514184898",
    "appId": "1:1041514184898:web:d02a11cc9eac9cd6d7bb5b"
}

fireApp = firebase.initialize_app(fireConfig)
# Firebase Authentication Quota: 10k Active USers
auth = fireApp.auth()
# firestore Quota: 1GB
store = fireApp.firestore()
# Storage Quota: 5GB
storage= fireApp.storage()
# print('firebase.py   ___________________')



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
    # print('recived File Path:' + file_path)
    
    storage.child(file_path).put(file_stream, content_type)
    
    download_url = storage.child(file_path).get_url(None)
    
    # print('url for stored profile photo:'+ download_url)
    return download_url



# print('_________________________________')