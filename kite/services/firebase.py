import base64
from ErrorCodes import STATUS_CODES 
import firebase
import firebase_admin
from firebase_admin import auth, credentials, firestore,storage
from django.contrib import messages

firebase_admin.initialize_app(credentials.Certificate('potfolio-492d3-firebase-adminsdk-c1s9v-11f6742053.json'),{'storageBucket': 'potfolio-492d3.appspot.com'})
# # firestore Quota: 1GB
store = firestore.client()

#############################################
fireConfig = {
"apiKey" : "AIzaSyDHP6GQhjz0uFtrnuFllumERl-HmGSA9kA",
    "authDomain" : "potfolio-492d3.firebaseapp.com",
    "databaseURL" : "https://potfolio-492d3-default-rtdb.asia-southeast1.firebasedatabase.app",
    "projectId" : "potfolio-492d3",
    "storageBucket" : "potfolio-492d3.appspot.com",
    "messagingSenderId" : "1041514184898",
    "appId" : "1:1041514184898:web:d02a11cc9eac9cd6d7bb5b"
}
fireApp = firebase.initialize_app(fireConfig)
# # Firebase Authentication Quota: 50k Active Users
fireauth = fireApp.auth()
# # firestore Quota: 1GB
# store = fireApp.firestore()
# # Storage Quota: 5GB
# storage1= fireApp.storage()


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

# ! DONOT Touch. The whole website depends on this class and the function below.
class AuthenticationError(Exception):
    pass

def validateLogin(request):
    if "user_data" in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = None
        try:
            decoded_user = base64.b64decode(encoded_user_data).decode()
            claims = auth.verify_id_token(decoded_user)
            # If verification is successful, return both claims and decoded_user
            return [claims, decoded_user]
        except auth.ExpiredIdTokenError:
            del request.session['user_data']
            messages.success(request, ("You were loged out!"))
            raise AuthenticationError("Expired ID token")
        except auth.InvalidIdTokenError:
            del request.session['user_data']
            print("Invalid ID token error")
            raise AuthenticationError("Invalid ID token")
    else:
        return [False, False]
# ! ##############################################################################

def getPublicUrl(blob_path):
    # Get the reference to the blob
    blob = storage.bucket().blob(blob_path)

    # Check if the blob exists
    if blob:
        # Make the uploaded file publicly accessible
        blob.make_public()
        # Get the public URL for the blob
        public_url = blob.public_url
        return public_url

    else:
        # Handle the case where the blob doesn't exist
        return None



