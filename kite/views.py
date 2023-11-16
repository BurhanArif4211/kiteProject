from django.shortcuts import render, HttpResponse, redirect
from django.template.response import TemplateResponse
from django.contrib import messages
import re
import random
import os
import firebase, base64
# from mega import Mega
from ErrorCodes import STATUS_CODES 

# mega = Mega()  # instance for mega
# megaOperator = mega.login("9aaaaaaaaa99999999@gmail.com", "PASSWORDFORMEGA")

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
# Firebase Authentication
auth = fireApp.auth()
# firestore
store = fireApp.firestore()

######################################################################################################################
#                                                       PAGES                                                        #
######################################################################################################################

def kitePG(req):
    if "user_data" in req.session:
        encoded_user_data = req.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        claims = auth.verify_id_token(decoded_user)
        doesUserExist= store.collection('users1').where('user_id',"==",claims['user_id']).get()
        print(doesUserExist)
        if doesUserExist:
            context={
                'user_info':claims,
                'profile_info':doesUserExist[0]
            }
            print (doesUserExist[0])
            return TemplateResponse(req, "kite-main.html", context)
        else:
            if claims['email_verified']:
                return render(req, "profile-form.html")
            else:
                messages.success(
                    req, ("Please Verify Your Account Email before Going Futher! Check your email Inbox."))
                return redirect("/login")
    else:
        messages.success(
            req, ("Please Signup/Login In order to Continue to your kite."))
        return redirect("/login")

def loginPG(req):
    
    if "user_data" in req.session:
        encoded_user_data = req.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        claims = auth.verify_id_token(decoded_user)
        print(claims)
        if claims['email_verified']:
            return redirect("/kite")
        else:
            messages.success(req,("Please Verify Your Account Email before Going Futher! Check your email."))
            return render(req,'login.html')
    else:
        return render(req,'login.html')

def index(request):
    return render(request, 'index.html')

######################################################################################################################
#                                                NON-Related APIS                                                    #
######################################################################################################################



def resendEmailVerification(request):
    
    if "user_data" in request.session:
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        auth.send_email_verification(decoded_user)
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
        auth.create_user_with_email_and_password(email, password)
        user = auth.sign_in_with_email_and_password(email, password)
        # megaOperator.create_folder(email)
        # megaOperator.create_folder("files",email)

    if user:
        auth.update_profile(
            user['idToken'], display_name=f"{recived_username}")

        print(user)
        encoded_user_data = base64.b64encode(
            f"{user['idToken']}".encode()).decode()

        request.session['user_data'] = encoded_user_data
        auth.send_email_verification(user['idToken'])

        messages.success(
            request, ('Sign Up was Successful Please check Your Email for a Verification link!'))

        return redirect('/login')
    else:
        return redirect('/login')


def createProfile(request):
    if request.method == 'POST' and 'user_data' in request.session:            
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        user_info = auth.verify_id_token(decoded_user)
        
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
        
        
        # extension = (profileImage.name.split("."))[-1]
            # if profileImage.size < 2097152:  # size of file must be lesser than 2 MB if videos were allowed else change it to common illustration files size
                
            #     if extension in ["png", "jpg", "gif", "svg", "tfif", "jpeg", "webp", "gif"]:
            #         handle_uploaded_file(profileImage, user_info)
            #     else:
            #         return HttpResponse(STATUS_CODES["3"])
            # else:
            #     return HttpResponse(STATUS_CODES["2"])


def loginWithEmail(request):
    if request.method == 'POST':
        
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
           user = auth.sign_in_with_email_and_password(email, password)
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
        return redirect("fbi.org")


def loginWithGoogle():
    
    return redirect()

######################################################################################################################
#                                                   Helper Functions                                                 #
######################################################################################################################
    
# def handle_uploaded_file(paramfile, user_info):

#     fNN = randomId()
#     fN = './static/temp/' + fNN
#      # (37 permutation 10) = 1264020397516800 possible names meaning 1/1264020397516800 = 7.911264738801092e-16 probablity of matching names, hence the change is neglectable not going to add file if exists logic!
#     with open(fN, 'wb+') as destination:
#         for chunk in paramfile.chunks():
#             destination.write(chunk)
#     print(fN)
#     print("was fN and is user_info['users'][0]['email']")
#     print(user_info['users'][0]['email'])
#     mega_file = megaOperator.upload(fN,dest_filename=f"{user_info['users'][0]['email']}-propic")#, user_info['users'][0]['email'])
#     print(mega_file)
#     os.remove(fN)


# def randomId():
#     returnable = ""
#     raw = "qwertyuiopasdfghjklzxcvbnm_1234567890"
#     for i in range(20):
#         q = random.randint(0, len(raw) - 1)
#         returnable += raw[q]
#     return returnable

