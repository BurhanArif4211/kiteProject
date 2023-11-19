from django.shortcuts import render, HttpResponse, redirect
from django.template.response import TemplateResponse
from django.http import JsonResponse, HttpResponse
from django.template import loader
from django.contrib import messages
import re,os,random,base64,datetime
from firebase_admin import auth
from ErrorCodes import STATUS_CODES 
from .services.firebase import upload_image, fireauth,storage,store

######################################################################################################################
#                                              DOCS FOR FIREBASE NOOBS                                               #
######################################################################################################################
#
#### user claims:
#   example user claim:
#    
#   {'name': 'Master Recon', 'iss': 'https://securetoken.google.com/potfolio-492d3',
#    'aud': 'potfolio-492d3', 'auth_time': 1700313585, 'user_id': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2', 
#    'sub': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2', 'iat': 1700313585, 'exp': 1700317185, 'email': 'masterrecon777@gmail.com', 
#    'email_verified': True, 'firebase': {'identities': {'email': ['masterrecon777@gmail.com']}, 'sign_in_provider': 'password'}, 'uid': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2'}
#    
#    when ever you call: 
# 
#    encoded_user_data = req.session['user_data']                # get stored auth token in session
#    decoded_user = base64.b64decode(encoded_user_data).decode() # decode the token because its encoded in base64 check signUpEmail() for more info
#    claims = auth.verify_id_token(decoded_user)                 # this will return above example data from user
#
#    the purpose for claims is to verify if a user actually exists in our website
#    also, the claim can provide us quickly with th uid of user to use in in other services (here uid is : 'user_id': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2')

#    [REMEMBER!] : This System is used from firebase-rest-api (import firebase)

########################################################################################################################
#
#### user info
#    when ever you run:
#    user_data = fireauth.get_account_info(decoded_user) # for more info about "decoded_user", read above claims
#    result:

#    {'kind': 'identitytoolkit#GetAccountInfoResponse', 'users': [{'localId': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2', 'email': 'masterrecon777@gmail.com', 
#    'displayName': 'Master Recon', 'photoUrl': 'https://storage.googleapis.com/potfolio-492d3.appspot.com/userData/jE0ZoxMelpWnvDsfto9GLtGhJuw2/pp.jpg', 
#    'passwordHash': 'UkVEQUNURUQ=', 'emailVerified': True, 'passwordUpdatedAt': 1700313563952, 'providerUserInfo': [{'providerId': 'password', 'displayName': 
#    'Master Recon', 'photoUrl': 'https://storage.googleapis.com/potfolio-492d3.appspot.com/userData/jE0ZoxMelpWnvDsfto9GLtGhJuw2/pp.jpg', 
#    'federatedId': 'masterrecon777@gmail.com', 'email': 'masterrecon777@gmail.com', 'rawId': 'masterrecon777@gmail.com'}], 'validSince': '1700313563', 
#    'lastLoginAt': '1700313563952', 'createdAt': '1700313563952', 'lastRefreshAt': '2023-11-18T13:19:23.952Z'}]}

#     to clean this for use in application,
#        
#     user_data=user_data['users'][0]          
#     user_info = {
#   
#     "localID": user_data.get("localId"),
#     "email": user_data.get("email"),
#     "displayName": user_data.get("displayName"),
#     "photoUrl": user_data.get("photoUrl"),
#   
#      }
#      print(user_info) # this will boil down the data to only needed data
#
#      {'localID': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2', 'email': 'masterrecon777@gmail.com', 
#      'displayName': 'Master Recon', 'photoUrl': 'https://storage.googleapis.com/potfolio-492d3.appspot.com/userData/jE0ZoxMelpWnvDsfto9GLtGhJuw2/pp.jpg'}
#
#      Now this can be used in page contexts or any other place!
#
#      [REMEMBER!] : This System is used from firebase-rest-api (import firebase)
#
#################################################################################################################################
#### profile info from firestore collection "users1":
#
#    when ever you run:
#    user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
#    print(user_profile_data)
# 
#    ^ This gives out:

#    [<google.cloud.firestore_v1.base_document.DocumentSnapshot object at 0x0000026A567D7B50>]

#     
#    To get the dictionary, we use to_dict()
#    print(user_profile_data[0].to_dict())
#
#    ^ This gives out:

#    {'niche': 'Senior Dev', 'company': 'Master Inc', 'links': 
#    {'3': '-', '1': 'masterrecon.com', '2': 'facebook.com'}, 
#    'country': 'United States', 'user_id': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2', 
#    'about': 'I am an Enterpenuier in Manhattan', 'city': 'MANHATTAN'}

#
#    The above data is passed normally as a dictionary to context or used in any api
#
#    [REMEMBER!] : This System is used from firebase_admin (import firebase_admin)
#
###############################################################################################################
#### post info from firestore collection 'posts1':
#    
#   when ever you run:
#    user_profile_data = store.collection('posts1').where('user_id', '==', claims['user_id']).get()
#
#
#
#
#
#
#
#
######################################################################################################################
#                                                       PAGES                                                        #
######################################################################################################################

def kitePG(req):
    if "user_data" in req.session:
        encoded_user_data = req.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        claims = auth.verify_id_token(decoded_user)
        # print(claims)
        
        if claims['email_verified']:
            # Use Firestore to get user profile data
            user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
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
                return TemplateResponse(req, "kite-main.html", context)
            else:
                return render(req, "profile-form.html")
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
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        # template = loader.get_template('upload-post-popup.html')
        # html = template.render()
        return TemplateResponse(request,'upload-post-popup.html')
    else:
        messages.success(request,(f'This link is not supposed to be visited'))
        return redirect("/kite")
    
def loginPG(req):
    
    if "user_data" in req.session:
        encoded_user_data = req.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        claims = fireauth.verify_id_token(decoded_user)
        # print(claims)
        if claims['email_verified']:
            return redirect("/kite")
        else:
            messages.success(req,("Please Verify Your Account Email before Going Futher! Check your email."))
            return render(req,'login.html')
    else:
        return render(req,'login.html')

def index(request):
    # TODO add user_info context
    return render(request, 'index.html')

######################################################################################################################
#                                                NON-Related APIS                                                    #
######################################################################################################################

def uploadUserPic(request):
    if request.method == 'POST' and 'user_data' in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        claims = auth.verify_id_token(decoded_user)
        
        profile_picture = request.FILES['pp']
        file_path = f"userData/{claims['user_id']}/pp.jpg"
        
        # Upload the image to Firebase Storage using your existing function
        pp_url = upload_image(file_path, profile_picture.file, profile_picture.content_type)
        
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
        claims = auth.verify_id_token(decoded_user)
        
        postImage = request.FILES['postImage']
        postDescription = request.POST.get('postDescription')
        postId=randomId()
        current_time=datetime.datetime.now()
        
        file_path = f"postsData/{postId}/1.jpg"
        
        # Upload the image to Firebase Storage using your existing function
        post_url = upload_image(file_path, postImage.file, postImage.content_type)
        
        store.collection('posts1').document(postId).set(
            {
                'user_id':claims['user_id'],
                'post_url':post_url,
                'post_description':postDescription,
                'added_at':current_time,
            }
        )
        
        # Update 'users1' collection by appending postId to the 'posts' field
        user_query = store.collection('users1').where('user_id', '==', claims['user_id']).stream()
        for doc in user_query:
            user_data = doc.to_dict()
            current_posts = user_data.get('posts', [])
            current_posts.append(postId)
            
            store.collection('users1').document(doc.id).update({'posts': current_posts})
        
        # # ALERT!: This is an old method to store pp_url leave it 
        # # Use Firestore to update the document with the new field
        # user_query = store.collection('users1').where('user_id', '==', claims['user_id']).stream()
        # for doc in user_query:
        #     store.collection('users1').document(doc.id).update({'pp_url': pp_url})
        #########################################################
        
        return redirect('/kite')   

    ## this is useless for now
def resendEmailVerification(request):
    
    if "user_data" in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        fireauth.send_email_verification(decoded_user)
        tries=3 #just emulation testing 
        messages.success(request,(f'Email Resent. Tries Remain: {tries}'))
        return redirect("/login")


def logout(request):
    if 'user_data' in request.session:
        del request.session['user_data']
        messages.success(request,("You have been Logged Out!"))
        return redirect("/login")
    else:
        return redirect("/login")

######################################################################################################################
#                                                       APIS                                                         #
######################################################################################################################


def signUpWithEmail(request):
    if request.method == 'POST':
        recived_username = request.POST.get('username')
        password = request.POST.get('password')
        email = request.POST.get('email')
        fireauth.create_user_with_email_and_password(email, password)
        user = fireauth.sign_in_with_email_and_password(email, password)

    if user:
        print(user)
        fireauth.update_profile(user['idToken'], display_name=f"{recived_username}")
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
        user_info = fireauth.verify_id_token(decoded_user)
        
        country = request.POST.get('country')
        city = request.POST.get('city')
        niche = request.POST.get('niche')
        company = request.POST.get('company')
        about = request.POST.get('about')
        link1 = request.POST.get('link1')
        link2 = request.POST.get('link2')
        link3 = request.POST.get('link3')
        links={"1": link1,"2": link2,"3": link3}
        
        try:
            store.collection('users1').add({'user_id':user_info['user_id'],"country": country, "links": links, "niche": niche, "city": city, "company": company, "about": about,  })
            print('User Profile Created!')
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
           encoded_user_data = base64.b64encode(f"{user['idToken']}".encode()).decode()
           request.session['user_data'] = encoded_user_data
           return redirect("/kite")
           
             
        except:
            error="To be determined"
            messages.success(request,(f"Sign in error: {error}"))
            return redirect("/login") 
    else:
        messages.success(request,("what are you trying to do?"))
        return redirect("https://www.fbi.org")


######################################################################################################################
#                                                   Data Loading Functions                                           #
######################################################################################################################
def loadUserPosts(request):
    if 'user_data' in request.session: 
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        claims=fireauth.verify_id_token(decoded_user)
        posts_info=[]
        user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
        
        if 'posts' in user_profile_data[0].to_dict():
            posts=user_profile_data[0].to_dict()['posts']
            for postId in posts:
                post_info=store.collection('posts1').document(postId).get().to_dict()
                # print(post_info)
                posts_info.append(post_info) #append items to this until loop finishes
            
        
        return TemplateResponse(request, 'posts-grid.html', {'posts': posts_info})
    
# this can be used to avoid confusion 
#  def getPostInfoById(postId):
#      return post_info=store.collection('posts1').document(postId).get().to_dict()

######################################################################################################################
#                                                   Helper Functions                                                 #
######################################################################################################################
    
def randomId():
    returnable = ""
    raw = "qwertyuiopasdfghjklzxcvbnm_1234567890"
    for i in range(20):
        q = random.randint(0, len(raw) - 1)
        returnable += raw[q]
    return returnable

