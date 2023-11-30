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
            return kitePGHelper(req, publicProfileId,claims)
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
        
        #########################  THIS IS JUST FOR TEST DONOT PUSH IN PRODUCTION WITH THIS CODE  ##############################
        
        users=store.collection('users1').get()
        
        userList=[]
        for i in range(len(users)):
            userList.append(users[i].to_dict())
        ##########################################################################################################################
        user_data = fireauth.get_account_info(decoded_user)['users'][0]
        profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
        user_info = {
         "localID": user_data.get("localId"),
         "email": user_data.get("email"),
         "displayName": user_data.get("displayName"),
         "photoUrl": user_data.get("photoUrl"),
        }
        profile_data_of_currently_logged_in_user = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
        context ={
            'default' :{
            'pic' : profile_data_of_currently_logged_in_user.get('pp_url'), 'name': auth.get_user(claims['user_id']).display_name
            },
  
            'allUsers':userList,
            'user_info': user_info,
            'profile_info':profile_data[0].to_dict(),
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
        user_query = store.collection('users1').where('user_id', '==', claims['user_id']).stream()
        for doc in user_query:
            store.collection('users1').document(doc.id).update({'pp_url': pp_url})
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
                'comments':[], #add comments later by using update method in firebase //It should be better to use Array e.g [{name:aman, caption: caption, time: time},{name: so on}] or how'll you name elements of dict for each comments?
                'added_at': current_time,# TODO IMPORTANT: add a date fetching system from server since users can expliot this!!!
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
        messages.success(request, ("You Were Loged Out!"))
        return redirect("/login")
    else:
        return redirect("/login")

######################################################################################################################
#                                                       APIS                                                         #
######################################################################################################################



def like(request, url):
    if 'user_data' in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        
        try:
            claims = auth.verify_id_token(decoded_user)
        except auth.ExpiredIdTokenError:
            del request.session['user_data']
            messages.success(
                request, ("Your Session got expired! Please login again to continue."))
            return redirect("/login")
        except auth.InvalidIdTokenError:
            # Handle invalid token error, for example, log the error
            print("Invalid ID token error")
            return HttpResponse('{"error":"Invalid user"}')

        # Assuming you have initialized your Firestore client as 'store' and 'db'
        post_query = store.collection('posts1').where('post_id', '==', url).get()

        if post_query:
            post_profile = post_query[0]
            post_profile_data = post_profile.to_dict()

            if 'post_id' in post_profile_data and claims['user_id'] in post_profile_data['post_id']:
                print('User has not liked this post before')
                document_id = post_profile.id
                
                # Retrieve the 'likers' array from the document
                likers = post_profile.get('likers', [])

                if claims['user_id'] in likers:
                    print('User has liked this post before')
                    # Remove the user from the 'likers' array
                    likers.remove(claims['user_id'])

                    # Update the 'likers' array in the Firestore document
                    post_profile.reference.update({'likers': likers})

                    return HttpResponse('{"state":"like"}')
                else:
                    #TODO Else insert into DataBase
                    return HttpResponse('{"state":"liked"}')
            else:
                return HttpResponse('{"error":"Invalid post or user"}')
        else:
            return HttpResponse('{"error":"Post not found"}')
    else:
        return HttpResponse('{"error":"You may be logged out"}')



def followUserByPublicId(request, publicProfileId):
    if 'user_data' in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        try:
            claims = auth.verify_id_token(decoded_user)
        except auth.ExpiredIdTokenError:
            del request.session['user_data']
            messages.success(request, ("You Were Logged Out!"))
            return redirect("/login")

        print(f"the follow function was called by {claims['name']} for {publicProfileId}")
        

        ours_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
        ourPublicProfileId = ours_profile_data[0].to_dict().get('publicProfileId')
        # theirPublicProfileId = publicProfileId
        
        # Check if you are trying to follow yourself
        if publicProfileId == ourPublicProfileId :
            print("You can't follow yourself!")
            return redirect('/')
        
        else:
            # Update 'following' for the current user (Staging)
            ourCurrentFollowing = set(ours_profile_data[0].to_dict().get('following', []))

            if publicProfileId in ourCurrentFollowing:
                # If the user is already in the following list, remove them
                ourCurrentFollowing.remove(publicProfileId)
            else:
                # If the user is not in the following list, add them
                ourCurrentFollowing.add(publicProfileId)
            
            # Here we do the actual update of data.
            user_query = store.collection('users1').where('publicProfileId', '==', ourPublicProfileId ).stream()
            for doc in user_query:
                store.collection('users1').document(doc.id).update({'following': list(ourCurrentFollowing)})

            # Update 'followers' for the other user
            user_query = store.collection('users1').where('publicProfileId', '==', publicProfileId).stream()
            for doc in user_query:
                user_data = doc.to_dict()
                their_current_followers = set(user_data.get('followers', []))
    
                if ourPublicProfileId in their_current_followers:
                    # If the current user is already in the other person's followers list, remove them
                    their_current_followers.remove(ourPublicProfileId)
                else:
                    # If the current user is not in the other person's followers list, add them
                    their_current_followers.add(ourPublicProfileId)
    
                    store.collection('users1').document(doc.id).update({'followers': list(their_current_followers)})

            return redirect('/')






# def followUserByPublicId(request,publicProfileId):
#     if 'user_data' in request.session:
#         encoded_user_data = request.session['user_data']
#         decoded_user = base64.b64decode(encoded_user_data).decode()
#         try:
#             claims = auth.verify_id_token(decoded_user)
#         except auth.ExpiredIdTokenError:
#             del request.session['user_data']
#             messages.success(
#                 request, ("You Were Logged Out!"))
#             return redirect("/login")
        
#         print(f"the follow function was called by {claims['name']} for {publicProfileId}")
#         # print('_________________________________________')
        
#         our_profile_data = store.collection('users1').where('publicProfileId', '==', publicProfileId).get()
#         their_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
        
#         # print(following_profile_data)
#         # print('_________________________________________')
#         # print(follower_profile_data)
#         # print('_________________________________________')
        
      
#         # Check if you are trying to follow yourself
#         if our_profile_data[0].to_dict().get('publicProfileId') == their_profile_data[0].to_dict().get('publicProfileId'):
#             print("You can't follow yourself!")
#             return redirect('/')            
#         else:
#             # Update 'following' for the current user
#             our_current_following = set(our_profile_data[0].to_dict().get('following', []))
            
#             if their_profile_data[0].to_dict().get('publicProfileId') not in our_current_following:
                
#                 user_query = store.collection('users1').where('publicProfileId', '==', our_profile_data[0].to_dict().get('publicProfileId')).stream()
#                 for doc in user_query:    
                    
#                     our_current_following.add(our_profile_data[0].to_dict().get('publicProfileId'))
                    
#                     store.collection('users1').document(doc.id).update({'following': list(our_current_following)})
#             else:
#                 print('The user is already in my following list!')
#                 return redirect('/')
            
#             # Update 'followers' for the other user
#             user_query = store.collection('users1').where('publicProfileId', '==', publicProfileId).stream()
#             for doc in user_query:
#                 user_data = doc.to_dict()
#                 their_current_followers = set(user_data.get('followers', []))
#                 if our_profile_data[0].to_dict().get('publicProfileId') not in their_current_followers:
                    
#                     their_current_followers.add(their_profile_data[0].to_dict().get('publicProfileId'))
                    
#                     store.collection('users1').document(doc.id).update({'followers': list(their_current_followers)})
#                 else:
#                     print("I am already in the other person's list!")
#                     return redirect('/')
        
        

#             return redirect('/')
    
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
        fireauth.send_email_verification(user['idToken'])

        messages.success(
            request, ('Sign Up was Successful Please check Your Email for a Verification link.'))

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
                                            "links": links,'following' : [], 'followers' : [], "niche": niche, 
                                            "city": city, "company": company, "about": about, "publicProfileId":profilePublicId})
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


def loadThirdPersonPost(request,userIdFromUrl):
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
            'user_id', '==', userIdFromUrl).get()


        if 'posts' in user_profile_data[0].to_dict():
            posts = user_profile_data[0].to_dict()['posts']
            for postId in posts:
                post_info = store.collection(
                    'posts1').document(postId).get().to_dict()
                print(post_info)
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


def kitePGHelper(req, publicProfileId,claims): # Be confident About your self. One day you are gonna be proud of your self!
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
        profile_data_of_currently_logged_in_user = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
        context = {
            'default' :{
            'pic' : profile_data_of_currently_logged_in_user.get('pp_url'), 'name': auth.get_user(claims['user_id']).display_name
            },
            'src': publicProfileId,
            'user_info': user_info,
            'profile_info': user_profile_data[0].to_dict(),
        }
        print(context.get("default").get("name"))
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
