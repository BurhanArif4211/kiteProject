import firebase, base64
from ErrorCodes import STATUS_CODES 
fireConfig = {
....
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
