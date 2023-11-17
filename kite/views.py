from django.shortcuts import render, HttpResponse, redirect
from django.template.response import TemplateResponse
from django.template import loader
from django.contrib import messages
import re,os,base64,random

from ErrorCodes import STATUS_CODES 
from .services.firebase import upload_image, auth,store

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
            userProfileData= store.collection('users1').where('user_id',"==",claims['user_id']).get()  
            if len(userProfileData)>0:
                profileDataId=next(iter(userProfileData[0]))
                context={
                    'user_claims':claims,
                    'user_info': auth.get_account_info(decoded_user),
                    'profile_info':userProfileData[0][profileDataId]
                }
                return TemplateResponse(req, "kite-main.html", context)
            else:
                return render(req, "profile-form.html")
        else:
            del req.session['user_data']
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

# def uploadPROPIC(request):
#     if request.method == 'POST' and 'user_data' in request.session and request.FILES['profileImage']:
#         profileImage = request.FILES['profileImage']
#         try:
#             encoded_user_data = request.session['user_data']
#             decoded_user = base64.b64decode(encoded_user_data).decode()
#             user_info = auth.get_account_info(decoded_user)
#             fN = handle_uploaded_file(profileImage)
#             try:
#                 #child(user_info['users'][0]['localId']).
#                 # DOFF = storage.child("usersData").child(fN).put(f"static/temp/{fN}")
#                 DOFF = storage.child("usersData").child(user_info['users'][0]['localId']).child("propic.kite").put(f"static/temp/{fN}")
#                 print(DOFF)
#             except Exception as error:
#                 print(error)
#             print(fN)
#             # print("REmoving")
#             # os.remove(fN)
#             # storage.child("images/example.jpg").get_url(user["idToken"])
#             return HttpResponse("DONE uploading file")
#         except Exception as error:
#             print(error)
#             return HttpResponse("Error uploading file")

def uploadUserPic(request):
    if request.method == 'POST' and 'user_data' in request.session :
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        claims = auth.verify_id_token(decoded_user)
        profile_picture = request.FILES['pp']
        
        # Define the file path where the image will be stored in Firebase Storage
        file_path = f"userData/{claims['user_id']}/pp.jpg"
        
        # Upload the image to Firebase Storage
        pp_url = upload_image(file_path, profile_picture.file, profile_picture.content_type)
        # print('recived pp_url:' + pp_url)
        auth.update_profile(decoded_user, photo_url=pp_url)
        
        user_info = auth.get_account_info(decoded_user)
        
        # print(user_info)
        
        return redirect('/kite')  # Redirect to the user's profile page or wherever appropriate
  
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

    if user:
        print(user)
        auth.update_profile(user['idToken'], display_name=f"{recived_username}")
        # encoded_user_data = base64.b64encode(f"{user['idToken']}".encode()).decode()
        # request.session['user_data'] = encoded_user_data
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


######################################################################################################################
#                                                   Data Loading Functions                                           #
######################################################################################################################
def loadUserPosts(request):
    if 'user_data' in request.session: 
        encoded_user_data = request.session['user_data']
        decoded_user = base64.b64decode(encoded_user_data).decode()
        claims = auth.verify_id_token(decoded_user)
        
        # post_ids = [post.id for post in request.user.profile_info.posts]
        # posts_data = [(post_id, get_post(post_id)) for post_id in post_ids]
        
        context = {'posts_data': 'example data'}
    
        template = loader.get_template('posts-grid.html')
        html = template.render(context)
    
        return HttpResponse(html)
    
    


######################################################################################################################
#                                                   Helper Functions                                                 #
######################################################################################################################
    
def handle_uploaded_file(paramfile):
    fNN = randomId() + ".kite"
    base_path = r"D:\VirtualDesktop\GeneticEngineerinering\KiteProject"
    temp_path = os.path.join('static', 'temp')
    fN = os.path.join(temp_path, fNN)
    fN2 =  fNN

    with open(fN, 'wb+') as destination:
        for chunk in paramfile.chunks():
            destination.write(chunk)

    return fN2

def randomId():
    returnable = ""
    raw = "qwertyuiopasdfghjklzxcvbnm_1234567890"
    for i in range(20):
        q = random.randint(0, len(raw) - 1)
        returnable += raw[q]
    return returnable

