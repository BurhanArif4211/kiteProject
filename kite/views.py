from django.shortcuts import render, HttpResponse, redirect
from django.template.response import TemplateResponse
from django.http import JsonResponse, HttpResponse
from django.template import loader
from django.contrib import messages
import random
import base64
import datetime
from firebase_admin import auth
from ErrorCodes import STATUS_CODES
from .services.firebase import upload_image, fireauth, storage, store

# INFO: the docs have been moved to README.md

######################################################################################################################
#                                                       PAGES                                                        #
######################################################################################################################


def publicKitePG(req, publicProfileId):
    if "user_data" in req.session:
        encoded_user_data = req.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        try:
            claims = auth.verify_id_token(decoded_user)
        except auth.ExpiredIdTokenError:
            del req.session['user_data']
            messages.success(
                req, ("You Were Logged Out!"))
            return redirect("/login")
        if claims['email_verified']:
            return kitePGHelper(req, publicProfileId)
    else:
        return redirect('/login')


def kitePG(req):
    if "user_data" in req.session:
        encoded_user_data = req.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        try:
            claims = auth.verify_id_token(decoded_user)
            # print(claims)
        except auth.ExpiredIdTokenError:
            del req.session['user_data']
            messages.success(
                req, ("You Were Logged Out!"))
            return redirect("/login")

        if claims['email_verified']:
            # Use Firestore to get user profile data
            user_profile_data = store.collection('users1').where(
                'user_id', '==', claims['user_id']).get()
            # print(user_profile_data[0].to_dict())
            if len(user_profile_data) > 0:
                # Retrieve user account information
                user_data = fireauth.get_account_info(decoded_user)['users'][0]
                # print(user_data)
                user_info = {
                    "localID": user_data.get("localId"),
                    "email": user_data.get("email"),
                    "displayName": user_data.get("displayName"),
                    "photoUrl": user_data.get("photoUrl"),
                }
                # print(user_info)
                context = {
                    'user_claims': claims,
                    'user_info': user_info,
                    'profile_info': user_profile_data[0].to_dict(),
                }
                return TemplateResponse(req, "kite/kite-main.html", context)
            else:
                return render(req, "authentication/profile-form.html")
        else:
            del req.session['user_data']
            messages.success(
                req, ("Please Verify Your Account Email before Going Further! Check your email Inbox."))
            return redirect("/login")
    else:
        messages.success(
            req, ("Please Signup/Login In order to Continue to your kite."))
        return redirect("/login")


def uploadPost(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # this is for security
        return TemplateResponse(request, 'kite/upload-post-popup.html')
    else:
        # messages.success(request,(f'This link is not supposed to be visited'))
        return redirect("/kite")


def loginPG(req):

    if "user_data" in req.session:
        encoded_user_data = req.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        try:
            claims = auth.verify_id_token(decoded_user)
            # print(claims)
        except auth.ExpiredIdTokenError:
            del req.session['user_data']
            messages.success(
                req, ("You Were Logged Out!"))
            return redirect("/login")

        # print(claims)
        if claims['email_verified']:
            return redirect("/kite")
        else:
            messages.success(
                req, ("Please Verify Your Account Email before Going Futher! Check your email."))
            return render(req, 'authentication/login.html')
    else:
        return render(req, 'authentication/login.html')


def index(request):
    if "user_data" in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        try:
            claims = auth.verify_id_token(decoded_user)
            # print(claims)
        except auth.ExpiredIdTokenError:
            del request.session['user_data']
            messages.success(
                request, ("You Were Loged Out!"))
            return redirect("/login")
        user_data = fireauth.get_account_info(decoded_user)['users'][0]
        # print(user_data)
        user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
        user_info = {
         "localID": user_data.get("localId"),
         "email": user_data.get("email"),
         "displayName": user_data.get("displayName"),
         "photoUrl": user_data.get("photoUrl"),
        }
        # print(user_info)
        context = {
            'user_claims': claims,
            'user_info': user_info,
            'profile_info': user_profile_data[0].to_dict(),
        }
        return TemplateResponse(request, "home/index.html", context)
    else:
            return TemplateResponse(request, "home/index.html")

######################################################################################################################
#                                                NON-Related APIS                                                    #
######################################################################################################################


def uploadUserPic(request):
    if request.method == 'POST' and 'user_data' in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        try:
            claims = auth.verify_id_token(decoded_user)
            # print(claims)
        except auth.ExpiredIdTokenError:
            del request.session['user_data']
            messages.success(
                request, ("You Were Logged Out!"))
            return redirect("/login")

        profile_picture = request.FILES['pp']
        file_path = f"userData/{claims['user_id']}/pp.jpg"

        # Upload the image to Firebase Storage using your existing function
        pp_url = upload_image(file_path, profile_picture.file,
                              profile_picture.content_type)

        auth.update_user(claims['user_id'], photo_url=pp_url,)

        # # ALERT!: This is an old method to store pp_url leave it
        # # Use Firestore to update the document with the new field
        # user_query = store.collection('users1').where('user_id', '==', claims['user_id']).stream()
        # for doc in user_query:
        #     store.collection('users1').document(doc.id).update({'pp_url': pp_url})
        #########################################################

        return redirect('/kite')


def uploadUserPost(request):
    if request.method == 'POST' and 'user_data' in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        try:
            claims = auth.verify_id_token(decoded_user)
            # print(claims)
        except auth.ExpiredIdTokenError:
            del request.session['user_data']
            messages.success(
                request, ("You Were Logged Out!"))
            return redirect("/login")

        postImage = request.FILES['postImage']
        postDescription = request.POST.get('postDescription')
        postId = randomId()
        current_time = datetime.datetime.now()

        file_path = f"postsData/{postId}/1.jpg"

        # Upload the image to Firebase Storage using your existing function
        post_url = upload_image(
            file_path, postImage.file, postImage.content_type)

        store.collection('posts1').document(postId).set(
            {
                'user_id': claims['user_id'],
                'post_url': post_url,
                'post_description': postDescription,
                'likes':[],
                'comments':{#add comments later by using update system in firebase
                    },
                'added_at': current_time,
            }
        )

        # Update 'users1' collection by appending postId to the 'posts' field
        user_query = store.collection('users1').where(
            'user_id', '==', claims['user_id']).stream()
        for doc in user_query:
            user_data = doc.to_dict()
            current_posts = user_data.get('posts', [])
            current_posts.append(postId)

            store.collection('users1').document(
                doc.id).update({'posts': current_posts})

        # # ALERT!: This is an old method to store pp_url leave it
        # # Use Firestore to update the document with the new field
        # user_query = store.collection('users1').where('user_id', '==', claims['user_id']).stream()
        # for doc in user_query:
        #     store.collection('users1').document(doc.id).update({'pp_url': pp_url})
        #########################################################

        return redirect('/kite')

    # this is useless for now


def resendEmailVerification(request):

    if "user_data" in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        fireauth.send_email_verification(decoded_user)
        tries = 3  # just emulation testing
        messages.success(request, (f'Email Resent. Tries Remain: {tries}'))
        return redirect("/login")


def logout(request):
    if 'user_data' in request.session:
        del request.session['user_data']
        messages.success(request, ("You have been Logged Out!"))
        return redirect("/login")
    else:
        return redirect("/login")

######################################################################################################################
#                                                       APIS                                                         #
######################################################################################################################


def follow(request,profile):
    if 'user_data' in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        try:
            claims = auth.verify_id_token(decoded_user)
            # print(claims)
        except auth.ExpiredIdTokenError:
            del request.session['user_data']
            messages.success(
                request, ("You Were Logged Out!"))
            return redirect("/login")

        secondperson_profile_data = store.collection('users1').where(
            'profile', '==', profile).get()
        user_profile_data = store.collection('users1').where(
            'user_id', '==', claims['user_id']).get()
        print(secondperson_profile_data[0].to_dict())
        print(user_profile_data[0].to_dict())
        print(claims['user_id'])

        #TODO just fetch and set documents of these two lines
        store.collection("users1").document(claims['user_id']).update({'following':[secondperson_profile_data[0].to_dict().get('user_id')] + user_profile_data[0].to_dict().get('following')})
        store.collection("users1").document(secondperson_profile_data[0].to_dict().get('user_id')).update({'followers':([secondperson_profile_data[0].to_dict().get('user_id')] + user_profile_data[0].to_dict().get('followers'))})
        return HttpResponse('followed')
def signUpWithEmail(request):
    if request.method == 'POST':
        recived_username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        fireauth.create_user_with_email_and_password(email, password)
        user = fireauth.sign_in_with_email_and_password(email, password)

    if user:
        print(user)
        fireauth.update_profile(
            user['idToken'], display_name=f"{recived_username}")
        # encoded_user_data = base64.b64encode(f"{user['idToken']}".encode()).decode()
        # request.session['user_data'] = encoded_user_data
        fireauth.send_email_verification(user['idToken'])

        messages.success(
            request, ('Sign Up was Successful Please check Your Email for a Verification link!'))

        return redirect('/login')
    else:
        return redirect('/login')


def createProfile(request):
    if request.method == 'POST' and 'user_data' in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        try:
            user_info = auth.verify_id_token(decoded_user)
            # print(claims)
        except auth.ExpiredIdTokenError:
            del request.session['user_data']
            messages.success(
                request, ("You Were Logged Out!"))
            return redirect("/login")

        country = request.POST.get('country')
        city = request.POST.get('city')
        niche = request.POST.get('niche')
        company = request.POST.get('company')
        about = request.POST.get('about')
        profilePublicId = randomId()
        link1 = request.POST.get('link1')
        link2 = request.POST.get('link2')
        link3 = request.POST.get('link3')
        links = {"1": link1, "2": link2, "3": link3}

        try:
            store.collection('users1').add({'user_id': user_info['user_id'], "country": country,
                                            "links": links,'following' : [], 'followers' : [], "niche": niche, "city": city, "company": company, "about": about, "publicProfileId":profilePublicId})
            messages.success(request, ("Profile Created! Now Lets Get to know about each other."))
            return redirect("/kite")

        except Exception as e:
            print(e)
            return HttpResponse(f"Error inserting data or uploading file {e}")

    else:
        redirect("/login")


def loginWithEmail(request):
    if request.method == 'POST':

        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = fireauth.sign_in_with_email_and_password(email, password)
            print(user)
            encoded_user_data = base64.b64encode(
                f"{user['idToken']}".encode()).decode()
            request.session['user_data'] = encoded_user_data
            return redirect("/kite")

        except:
            error = "To be determined"
            messages.success(request, (f"Sign in error: {error}"))
            return redirect("/login")
    else:
        messages.success(request, ("what are you trying to do?"))
        return redirect("https://www.fbi.gov")


######################################################################################################################
#                                                   Data Loading Functions                                           #
######################################################################################################################
def loadUserPosts(request):
    if 'user_data' in request.session and request.headers.get('X-Requested-With') == 'XMLHttpRequest': # For security so the user can't load his posts separately!
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        try:
            claims = auth.verify_id_token(decoded_user)
            # print(claims)
        except auth.ExpiredIdTokenError:
            del request.session['user_data']
            messages.success(
                request, ("You Were Logged Out!"))
            return redirect("/login")

        posts_info = []
        user_profile_data = store.collection('users1').where(
            'user_id', '==', claims['user_id']).get()

        if 'posts' in user_profile_data[0].to_dict():
            posts = user_profile_data[0].to_dict()['posts']
            for postId in posts:
                post_info = store.collection(
                    'posts1').document(postId).get().to_dict()
                # print(post_info)
                # append items to 'posts_info' until loop finishes
                posts_info.append(post_info)
        # print(posts_info)

        return TemplateResponse(request, 'kite/posts-grid.html', {'posts': posts_info})

# this can be used to avoid confusion
#  def getPostInfoById(postId):
#      return post_info=store.collection('posts1').document(postId).get().to_dict()

######################################################################################################################
#                                                   Helper Functions                                                 #
######################################################################################################################

# loads profile using path


def kitePGHelper(req, publicProfileId): # Be confident About your self. One day you are gonna be proud of your self!
    user_profile_data = store.collection('users1').where('publicProfileId', '==', publicProfileId).get()
    
    if len(user_profile_data) > 0:
        print(f"11: {user_profile_data[0].to_dict()}")

        user_data = auth.get_user(user_profile_data[0].to_dict().get('user_id'))
        print(user_data)
        user_info = {
            "localID": user_data.uid,
            "email": user_data.email,
            "displayName": user_data.display_name,
            "photoUrl": user_data.photo_url,
        }
        print(user_info)
        context = {
            'src': publicProfileId,
            'user_info': user_info,
            'profile_info': user_profile_data[0].to_dict(),
        }

        return TemplateResponse(req, "kite/kite-public.html", context)
    else:
        # TODO In future i will make a 404 page so the user may know that the wrong ID does not exist! ;) 
        return redirect('/kite' )  #render(req, "authentication/profile-form.html")  # I dont understand why you rendered this form here.



def randomId():
    returnable = ""
    raw = "qwertyuiopasdfghjklzxcvbnm_1234567890"
    for i in range(20):
        q = random.randint(0, len(raw) - 1)
        returnable += raw[q]
    return returnable
