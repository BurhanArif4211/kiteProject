from urllib.parse import urlparse
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
from .services.firebase import upload_image,validateLogin,getPublicUrl,AuthenticationError, fireauth, store# storage
from .modules.scorealgo import scorify
from fubam import render_pythonMarkup

######################################################################################################################
#                                                       PAGES                                                        #
######################################################################################################################

def index(request):
    try:
        claims, decoded_user = validateLogin(request)
        if not claims:
            return TemplateResponse(request, "home/index.html")
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")

    #########################  THIS IS JUST FOR TEST DONOT PUSH IN PRODUCTION WITH THIS CODE  ##############################
    users=store.collection('users1').get()
    userList=[]
    for i in range(len(users)):
        userList.append(users[i].to_dict())
    ##########################################################################################################################

    profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
    # user_info=getUserInfo(decoded_user)
    context = {
        'default':{'pp_url':profile_data['pp_url'],'display_name':profile_data['display_name']},
        'allUsers':userList,
        #'user_info':user_info, #Depricated
        'profile_info':profile_data,
    }
    return TemplateResponse(request, "home/index.html", context)



def kitePG(request):

    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")

    if not claims:
        messages.success(request, ("Please Signup/Login In order to Continue to your kite."))
        return redirect('/login')

    if not claims['email_verified']:
        del request.session['user_data']
        messages.success(request, ("Please Verify Your Account Email before Going Further! Check your email Inbox."))
        return redirect("/login")

    if claims['email_verified']:
        # Use Firestore to get user profile data
        user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()

        if len(user_profile_data) > 0:
        # print(user_profile_data[0].to_dict())
            # Retrieve user account information
            # user_info=getUserInfo(decoded_user)
            # print(user_info)
            context = {
                'niches': user_profile_data[0].to_dict().get('niche').split(','),
                    'urls': [
                    [get_main_domain(   user_profile_data[0].to_dict().get('links').get('2')),user_profile_data[0].to_dict().get('links').get('2')]
                    ,[get_main_domain(user_profile_data[0].to_dict().get('links').get('1')),user_profile_data[0].to_dict().get('links').get('1')]
                    ,[get_main_domain(user_profile_data[0].to_dict().get('links').get('3')),user_profile_data[0].to_dict().get('links').get('3')]
                    ],
                    'score' : scorify(claims['user_id']),
                'user_claims': claims,
                # 'user_info': user_info, now it is depricated!
                'profile_info': user_profile_data[0].to_dict(),
            }
            return TemplateResponse(request, "kite/kite-main.html", context)
        else:
            return render(request, "authentication/profile-form.html")

def publicKitePG(request, publicProfileId):

    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")
    if not claims:
       return redirect('/login')
    if not claims['email_verified'] :
        return redirect('/login')
    else:
       return publicKitePGHelper(request, publicProfileId,decoded_user,claims)


def feedPG(request):
    # Fetch a single random post
    claims, decoded_user=validateLogin(request)
    postss_data = store.collection('posts1').get()
    posts_data=[]
    for post_data in postss_data:
        post_data=post_data.to_dict()
        posts_data.append(post_data)
    # print(posts_data)
   
    
    user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
    pp_url=user_profile_data['pp_url']
    displayName=user_profile_data['display_name']
    
    context={'posts': posts_data,'default':{'pp_url':pp_url,'displayName':displayName,"claims" : claims }}
    # print(context)
    return render(request, 'feed/feed.html',context)

    # return HttpResponse(render_pythonMarkup('feed/post-card', resources={'posts': post_data, 'default':{'pp_url':pp_url,'displayName':displayName,"claims" : claims }}))
    
#########   this will be used to load next post in the future for infinite scrolling.
# def loadFeedPost(request):
#     # Fetch a new random post
#     post_ref = store.collection('posts1').limit(1).get()
#     post_data = post_ref[0].to_dict()

#     return JsonResponse({
#         'post': post_data,
#     })

def loginPG(request):

    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")
    if not claims:
        return TemplateResponse(request, "authentication/login.html")

    if claims['email_verified']:
        return redirect("/kite")
    else:
        del request.session['user_data']
        messages.success(
            request, ("Please Verify Your Account Email before Going Futher! Check your email."))
        return render(request, 'authentication/login.html')

def uploadPostModal(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':  # this is for security
        return TemplateResponse(request, 'kite/upload-post-popup.html')
    else:
        # messages.success(request,(f'This link is not supposed to be visited'))
        return redirect("/kite")


######################################################################################################################
#                                       Authentication & Information                                                 #
######################################################################################################################

def signUpWithEmail(request):
    if request.method == 'POST':
        recived_username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        fireauth.create_user_with_email_and_password(email, password)
        user = fireauth.sign_in_with_email_and_password(email, password)

    if user:
        # print(user)
        fireauth.update_profile(
            user['idToken'], display_name=f"{recived_username}")
        fireauth.send_email_verification(user['idToken'])
        messages.success(
            request, ('Sign Up was Successful Please check Your Email for a Verification link.'))
        return redirect('/login')
    else:
        return redirect('/login')


def createProfile(request):
    if request.method == 'POST':
        try:
            claims, decoded_user = validateLogin(request)
        except AuthenticationError as e:
            print(f"Authentication error: {e}")
            return redirect("/login")
        if not claims:
            messages.success(request, ("Please Signup/Login In order to Continue to your kite."))
            return redirect("/login")
        elif not claims['email_verified']:
            del request.session['user_data']
            messages.success(request, ("Please Verify Your Account Email before Going Further! Check your email Inbox."))
            return redirect("/login")
        else:
            user_info=getUserInfo(decoded_user)
            country = request.POST.get('country')
            city = request.POST.get('city')
            niche = request.POST.get('niche')
            company = request.POST.get('company')
            about = request.POST.get('about')
            publicProfileId = randomId()
            link1 = request.POST.get('link1')
            link2 = request.POST.get('link2')
            link3 = request.POST.get('link3')
            links = {"1": link1, "2": link2, "3": link3}
            try:
                store.collection('users1').add(
                    {'display_name':user_info['displayName'],
                    'user_id': claims['user_id'],
                     "country": country,
                     "links": links,
                     'following' : [],
                     'followers' : [],
                     "niche": niche,
                     "city": city,
                     "company": company,
                     "about": about,
                     "publicProfileId":publicProfileId,
                     'pp_url':f"{getPublicUrl('static/default.jpg')}"
                     })

                return redirect("/kite")
            except Exception as e:
                print(e)
                return HttpResponse(f"Error inserting data or uploading file {e}")
    else:
        messages.success(request, ("Please Signup/Login In order to Continue to your kite."))
        return redirect("/login")

def loginWithEmail(request):
    if request.method == 'POST' and 'user_data' not in request.session:
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            user = fireauth.sign_in_with_email_and_password(email, password)
            print(user)
            encoded_user_data = base64.b64encode(
                f"{user['idToken']}".encode()).decode()
            request.session['user_data'] = encoded_user_data
            return redirect("/kite")
        except Exception as e:

            messages.success(request, (f"Sign in error: {e}"))
            return redirect("/login")
    else:
        # messages.success(request, ("what are you trying to do?"))
        return redirect("/")

######################################################################################################################
#                             Authentication Utilities                                                               #
######################################################################################################################


def getUserInfo(decoded_user):
    # * This function takes current auth token, fetches current user's auth-related personal data, right now, only 4 fields are useful
    # * But in future, this will be used to figure out if a user has google login or normal email login.
    user_info=fireauth.get_account_info(decoded_user)['users'][0]
    user_info = {
            "localID":user_info.get("localId"),
            "email": user_info.get("email"),
            "displayName": user_info.get("displayName"),
            "photoUrl": user_info.get("photoUrl"),
            }
    return user_info

def userIdtoPublicId(user_id):
    # * * This Function Takes a user's privatedUser_id to exchange it for his publicId
    return store.collection('users1').where('user_id','==',user_id).get()[0].to_dict()['publicProfileId']

def getProfileInfo(publicProfileId):
    # * * This function gets all profile data of a user from firebase mainly for cutom filter in the info_filters.py file
    return store.collection('users1').where('publicProfileId','==',publicProfileId).get()[0].to_dict()


def resendEmailVerification(request):
    # This is useless for now
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")
    fireauth.send_email_verification(decoded_user)
    tries = 3  # just for testing # TODO add custom claims to check how many times the user has sent email verification.
    messages.success(request, (f'Email Resent. Tries Remain: {tries}'))
    return redirect("/login")

def logout(request):
    if 'user_data' in request.session:
        del request.session['user_data']
        messages.success(request, ("You were loged out!"))
        return redirect("/login")
    else:
        return redirect("/login")

######################################################################################################################
#                                              Data Upload Functions                                                 #
######################################################################################################################

def uploadUserPic(request):
    if request.method == 'POST'and request.FILES['pp']:
        try:
            claims, decoded_user = validateLogin(request)
        except AuthenticationError as e:
            print(f"Authentication error: {e}")
            return redirect("/login")

        publicProfileId = userIdtoPublicId(claims['user_id'])

        profile_picture = request.FILES['pp']
        file_path = f"userData/{publicProfileId}/pp.jpg"
        # Upload the image to Firebase Storage using your existing function
        pp_url = upload_image(file_path, profile_picture.file,profile_picture.content_type)
        auth.update_user(claims['user_id'], photo_url=pp_url,)
        user_query = store.collection('users1').where('user_id', '==', claims['user_id']).stream()
        for doc in user_query:
            # adding current time in orfer to prevent caching this sucessfully fixes the prfile-not-updating-bug. :)
            store.collection('users1').document(doc.id).update({'pp_url': f"{pp_url}?updatedOn={datetime.datetime.now()}"})
        #########################################################

        return redirect('/kite')
    else:
        return redirect('/')

def uploadUserPost(request):
 if request.method == 'POST' and request.FILES['postImage']:
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")
    if not claims:
        return redirect('/login')
    if not claims['email_verified']:
        return redirect('/kite')
    else:

        postImage = request.FILES['postImage']
        postDescription = request.POST.get('postDescription')
        postId = randomId()
        current_time = datetime.datetime.now()

        file_path = f"postsData/{postId}/1.jpg"

        # Upload the image to Firebase Storage using your existing function
        post_url = upload_image(file_path, postImage.file, postImage.content_type)

        store.collection('posts1').document(postId).set(
            {
                'public_profile_id': userIdtoPublicId(claims['user_id']),
                # 'user_id':{claims['user_id']},# comment this maybe
                'post_url': post_url,
                'post_id': randomId(),
                'post_description': postDescription,
                'likes':[],
                #'liked':[],
                'comments':[], #add comments later by using update method in firebase //It should be better to use Array e.g [{name:aman, caption: caption, time: time},{name: so on}] or how'll you name elements of dict for each comments?
                'added_at': current_time, # TODO IMPORTANT: add a date fetching system from server users can expliot this!!!
            }
        )

        # Update 'users1' collection by appending postId to the 'posts' field
        user_query = store.collection('users1').where('user_id', '==', claims['user_id']).stream()
        for doc in user_query:
            user_data = doc.to_dict()
            current_posts = user_data.get('posts', [])
            current_posts.append(postId)

            store.collection('users1').document(doc.id).update({'posts': current_posts})

        return redirect('/kite')
 else:
      return redirect('/')

######################################################################################################################
#                                                   Data Loading Functions                                           #
######################################################################################################################
def loadUserPosts(request):
 if request.headers.get('X-Requested-With') == 'XMLHttpRequest': # For security so the user can't load his posts separately!
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")

    posts_info = []
    user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
    # user_info=getUserInfo(decoded_user)

    # print(user_info)

    if len(user_profile_data)>0:
        user_profile_data=user_profile_data[0].to_dict()

    if 'posts' in user_profile_data:
        posts = user_profile_data['posts']
        for postId in posts:
            post_info = store.collection(
                'posts1').document(postId).get().to_dict()
            # print(post_info)
            # append items to 'posts_info' until loop finishes
            posts_info.append(post_info)
    # print(posts_info)
    current_profile_info = store.collection(
        'users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
    # print(current_profile_info)

    pp_url=current_profile_info.get('pp_url')
    displayName=current_profile_info.get('display_name')

    # return TemplateResponse(request, 'kite/posts-grid.html', {'posts': posts_info, 'default':{'pp_url':pp_url,'displayName':displayName}})
    return HttpResponse(render_pythonMarkup('kite/posts-grid', resources={'posts': posts_info, 'default':{'pp_url':pp_url,'displayName':displayName,"localID" : claims['user_id'] }}))
 else:
     return redirect('/')


def publicLoadUserPost(request,userIdFromUrl):
 if request.headers.get('X-Requested-With') == 'XMLHttpRequest': # For security so the user can't load their posts separately!
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")
    posts_info = []
    user_profile_data = store.collection('users1').where('publicProfileId', '==', userIdFromUrl).get()[0].to_dict()
    if 'posts' in user_profile_data:
        posts = user_profile_data['posts']
        for postId in posts:
            post_info = store.collection('posts1').document(postId).get().to_dict()
            posts_info.append(post_info)
    # print(posts_info)

    pp_url=user_profile_data['pp_url']
    displayName=user_profile_data['display_name']
    return HttpResponse(render_pythonMarkup('kite/posts-grid', resources={'posts': posts_info, 'default':{'pp_url':pp_url,'displayName':displayName,"localID" : claims['user_id'] }}))
 else:return redirect('/')

######################################################################################################################
#                                               Intractions                                                          #
######################################################################################################################
def likeUserPost(request, targetPostId):
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return HttpResponse("redirect")

    if not claims:
        return HttpResponse("redirect")

    if not claims['email_verified']:
        return HttpResponse("redirect")

    else:
        post_query = store.collection('posts1').where('post_id', '==', targetPostId).get()

        if len(post_query) > 0:
            post_profile = post_query[0]
            post_profile_data = post_profile.to_dict()

            if 'post_id' in post_profile_data:
                print('User has not liked this post before')
                document_id = post_profile.id
                # Retrieve the 'likers' array from the document
                likers = post_profile.to_dict().get('likes', [])
                print(f"Likers before update: {likers}")

                if claims['user_id'] in likers:
                    print('User has liked this post before')
                    # Remove the user from the 'likers' array
                    likers.remove(claims['user_id'])
                    print(f"Likers after removing user: {likers}")

                    # Update the 'likers' array in the Firestore document
                    post_profile.reference.update({'likes': likers})
                    print('Post likers updated successfully')

                    return HttpResponse('unliked')
                else:
                    print()
                    likers.append(claims['user_id'])
                    print(f"Likers after appending user: {likers}")

                    # Update the 'likers' array in the Firestore document
                    post_profile.reference.update({'likes': likers})
                    print('Post likes updated successfully')
                    return HttpResponse('liked')
            else:
                print('Invalid post or user')
                return HttpResponse('posterror')
        else:
            print('Post not found')
            return HttpResponse('posterror')

from django.http import JsonResponse



def followUserByPublicId(request, publicProfileId):
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")
    if not claims:
        return redirect('/')
    if claims['email_verified']:

        print(f"The follow function was called by {claims['name']} for {publicProfileId}")

        ourProfileData = store.collection('users1').where('user_id', '==', claims['user_id']).get()

        ourPublicProfileId = ourProfileData[0].to_dict().get('publicProfileId')

        # theirPublicProfileId = publicProfileId
        # Check if you are trying to follow yourself
        if publicProfileId == ourPublicProfileId:
            print("You can't follow yourself!")
            response={
                        "success": False,
                        "message": "You can't follow yourself!",
                        "data":{

                        }
                    }
            return JsonResponse(response)
        else:
            # Update 'following' for the current user (Staging)
            ourCurrentFollowing = set(ourProfileData[0].to_dict().get('following', [])) #following:[...,...,...]

            theirProfileData = store.collection('users1').where('publicProfileId', '==', publicProfileId).get()[0].to_dict()
            theirCurrentFollowers = set(theirProfileData.get('followers', []))

            if publicProfileId in ourCurrentFollowing and ourPublicProfileId in theirCurrentFollowers:
                # If the user is already in the following list, remove them
                ourCurrentFollowing.remove(publicProfileId)
                theirCurrentFollowers.remove(ourPublicProfileId)

            elif not (publicProfileId in ourCurrentFollowing and ourPublicProfileId in theirCurrentFollowers):
                # If the user is not in the following list, add them
                ourCurrentFollowing.add(publicProfileId)
                theirCurrentFollowers.add(ourPublicProfileId)
            # Here we do the actual update of data.

            ourProfileData = store.collection('users1').where('publicProfileId', '==', ourPublicProfileId ).stream()
            for doc in ourProfileData:
                store.collection('users1').document(doc.id).update({'following': list(ourCurrentFollowing)})

            theirProfileData = store.collection('users1').where('publicProfileId', '==', publicProfileId).stream()
            for doc in theirProfileData:
                store.collection('users1').document(doc.id).update({'followers': list(theirCurrentFollowers)})

            response={
                        "success": True,
                        "message": f'You followed/unfollowed {theirCurrentFollowers} ',
                        "data": {
                            "theirFollowerCount": len(theirCurrentFollowers),
                            "ourFollowingCount": len(ourCurrentFollowing)
                        }
                    }
            return JsonResponse(response)

                ##############             ######################                 ################
            # Update 'followers' for the other user
            # theirProfileData = store.collection('users1').where('publicProfileId', '==', publicProfileId).stream()
            # for doc in theirProfileData:
            #     ourFollowersList = doc.to_dict()
            #     theirCurrentFollowers = set(ourFollowersList.get('followers', []))

                # if ourPublicProfileId in theirCurrentFollowers:
                #     # If the current user is already in the other person's followers list, remove them
                #     theirCurrentFollowers.remove(ourPublicProfileId)
                #     store.collection('users1').document(doc.id).update({'followers': list(theirCurrentFollowers)})

                #     response={
                #                 "success": True,
                #                 "message": f'You unfollowed {theirCurrentFollowers} ',
                #                 "data": {
                #                     "followerCount": len(theirCurrentFollowers),
                #                     "followingCount": len(ourCurrentFollowing)
                #                }
                #             }
                #     return JsonResponse()
                # else:
                #     # If the current user is not in the other person's followers list, add them
                #     theirCurrentFollowers.add(ourPublicProfileId)
                #     store.collection('users1').document(doc.id).update({'followers': list(theirCurrentFollowers)})
                #     response={
                #                 "success": True,
                #                 "message": f'You followed {theirCurrentFollowers} ',
                #                 "data": {
                #                     "followerCount": len(theirCurrentFollowers),
                #                     "followingCount": len(ourCurrentFollowing)
                #                }
                #             }
                    # return JsonResponse(response)




# def followUserByPublicId(request, publicProfileId):
#     try:
#         claims, decoded_user = validateLogin(request)
#     except AuthenticationError as e:
#         print(f"Authentication error: {e}")
#         return redirect("/login")

#     if not claims:
#         return redirect('/')

#     if claims['email_verified']:
#         print(f"The follow function was called by {claims['name']} for {publicProfileId}")

#         ours_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
#         ourPublicProfileId = ours_profile_data[0].to_dict().get('publicProfileId')

#         # Check if you are trying to follow yourself
#         if publicProfileId == ourPublicProfileId:
#             print("You can't follow yourself!")
#             response = {
#                 "success": False,
#                 "message": "You can't follow yourself!",
#                 "data": {
#                     "followerCount": False,
#                     "followingCount": False
#                 }
#             }
#             return JsonResponse(response)

#         ### Update 'following' for the current user (Staging)
#         ourCurrentFollowing = set(ours_profile_data[0].to_dict().get('following', []))

#         if publicProfileId in ourCurrentFollowing:
#             # If the user is already in the following list, remove them
#             ourCurrentFollowing.remove(publicProfileId)
#         else:
#             # If the user is not in the following list, add them
#             ourCurrentFollowing.add(publicProfileId)

#         # Here we do the actual update of data.
#         for doc in ours_profile_data:
#             store.collection('users1').document(doc.id).update({'following': list(ourCurrentFollowing)})

#         ### Update 'followers' for the other user

#         # theirProfileData = store.collection('users1').where('publicProfileId', '==', publicProfileId).stream()
#         # for doc in theirProfileData:
#         #     ourFollowersList = doc.to_dict()
#         #     their_current_followers = set(ourFollowersList.get('followers', []))

#         #     if ourPublicProfileId in their_current_followers:
#         #         # If the current user is already in the other person's followers list, remove them
#         #         their_current_followers.remove(ourPublicProfileId)
#         #     else:
#         #         # If the current user is not in the other person's followers list, add them
#         #         their_current_followers.add(ourPublicProfileId)
#         #         store.collection('users1').document(doc.id).update({'followers': list(their_current_followers)})
#         # Update 'followers' for the other user
#         theirProfileData = store.collection('users1').where('publicProfileId', '==', publicProfileId).stream()
#         for doc in theirProfileData:
#             followersList = doc.to_dict()
#             their_current_followers = set(followersList.get('followers', []))
#             if ourPublicProfileId in their_current_followers:
#                 # If the current user is already in the other person's followers list, remove them
#                 their_current_followers.remove(ourPublicProfileId)
#             else:
#                 #If the current user is not in the other person's followers list, add them
#                 their_current_followers.add(ourPublicProfileId)
#                 store.collection('users1').document(doc.id).update({'followers': list(their_current_followers)})

#         # sent to front to update on page
#         response = {
#             "success": True,
#             "message": f'You followed/unfollowed {publicProfileId}',
#             "data": {
#                 "theirFollowerCount": len(their_current_followers) ,  # Update with the actual follower count
#                 "yourFollowingCount": len(ourCurrentFollowing)  # Update with the actual following count
#             }
#         }
#         return JsonResponse(response)


######################################################################################################################
#                                                   Helper Functions                                                 #
######################################################################################################################

# loads profile using path

def publicKitePGHelper(request, publicProfileId,decoded_user, claims):
    user_profile_data = store.collection('users1').where(
        'publicProfileId', '==', publicProfileId).get()

    if len(user_profile_data) > 0:
        # print(f"11: {user_profile_data[0].to_dict()}")
        # user_info=getUserInfo(decoded_user)
        current_user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()

        context = {
            'default':{'pp_url':current_user_profile_data['pp_url'],'display_name':current_user_profile_data['display_name']},# for Base-nav.html
            'current_profile_info':current_user_profile_data,
            # 'user_info': user_info, this is depricated now all info of any user is stored in profile_info
            'profile_info': user_profile_data[0].to_dict(),
            'score' : scorify(user_profile_data[0].to_dict()['user_id']),#chonge later to public profile id maybe
        }

        return TemplateResponse(request, "kite/kite-public.html", context)
    else:

        return redirect('/kite')


def randomId():
    returnable = ""
    raw = "qwertyuiopasdfghjklzxcvbnm_1234567890"
    for i in range(20):
        q = random.randint(0, len(raw) - 1)
        returnable += raw[q]
    return returnable


# Path 404
def path404(request, slug, exception=None, status=404):
    return render(request, 'templates/404.html', {"slug": slug})


def get_main_domain(input_link):
    parsed_url = urlparse(input_link)
    domain_parts = parsed_url.netloc.split('.')
    if len(domain_parts) > 1:
        main_domain = domain_parts[-2]
    else:
        main_domain = parsed_url.netloc
    return main_domain.split('.')[0]