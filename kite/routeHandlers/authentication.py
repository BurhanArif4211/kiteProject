from kite.service_quarter import *
from jose import jwt

def loginWithGoogle(req):
   return redirect(fireauth.create_authentication_uri("google.com"))


def signUpWithEmail(request):
    try:
        if request.method == 'POST':
            recived_username = request.POST.get('username')
            email = request.POST.get('email')
            password = request.POST.get('password')

            if not checkPasswordValidation(password):

                messages.warning(
                    request, ("Too weak password! Must have 8 characters with one digit and one alphabet."))
                return redirect("/login")

            fireauth.create_user_with_email_and_password(email, password)
            user = fireauth.sign_in_with_email_and_password(email, password)

        if user:
            fireauth.update_profile(
                user['idToken'], display_name=f"{recived_username}")
            fireauth.send_email_verification(user['idToken'])
            messages.info(
                request, ('Sign Up was successful! Please check your mails for a verification link.'))
            return redirect('/login')
        else:
            return redirect('/login')
    except exceptions.AlreadyExistsError as e:
        messages.error(request, "Account exists.")
        return redirect('/login')
    except Exception as e:
        messages.error(request, "Something went wrong.")
        return redirect('/login')


def createProfile(request):
    if request.method == 'POST':
     try:
        try:
            claims, decoded_user = validateLogin(request)
        except AuthenticationError as e:
            print(f"Authentication error: {e}")
            return redirect("/login")
        if not claims:
            messages.warning(
                request, ("Please Signup/Login In order to Continue to your kite."))
            return redirect("/login")
        elif not claims['email_verified']:
            del request.session['user_data']
            messages.warning(
                request, ("Please Verify Your Account Email before Going Further! Check your email Inbox."))
            return redirect("/login")
        else:
            user_info = getUserInfo(decoded_user)
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
                    {'display_name': user_info['displayName'],
                     'user_id': claims['user_id'],
                     "country": country,
                     "links": links,
                     'following': [],
                     'followers': [],
                     "niche": niche,
                     "city": city,
                     "company": company,
                     "about": about,
                     "publicProfileId": publicProfileId,
                     'pp_url': f"{getPublicUrl('static/default.jpg')}"
                     })

                return redirect("/kite")
            except Exception as e:
                print(e)
                return HttpResponse(f"Error inserting data or uploading file {e}")
     except Exception as e:
        messages.error(
            request, ("Something went wrong, try again."))
        return redirect("/login")
    else:
        messages.warning(
            request, ("Please Signup/Login In order to Continue to your kite."))
        return redirect("/login")


def loginWithEmail(request):
    if request.method == 'POST' and 'user_data' not in request.session:
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            claims = fireauth.sign_in_with_email_and_password(email, password)
            #print(user)
            encoded_user_data = base64.b64encode(f"{claims['idToken']}".encode()).decode()
            request.session['user_data'] = encoded_user_data
            
            
            profileInfo=store.collection('users1').where('user_id','==',claims['localId']).get()[0].to_dict()
            if profileInfo:
                request.session['logged_profile_info']=profileInfo
                pass
            return redirect("/kite")
        except Exception as e:
            messages.error(request, (f"Sign in error: {e}"))
            return redirect("/login")
    else:
        
        return redirect("/")


def send_password_reset_email(request):
    try:
        email = request.GET.get("email")
        fireauth.send_password_reset_email(email)
        emailExists=store.collection
        messages.info(request, (f"Password reset link sent to {email}."))
        return redirect("/login")

    except Exception as e:# this is very bad practice, exeption handling is a complex problem.
        print(e)
        messages.error(request, ("Something went wrong."))
        return redirect("/login")
    
def logout(request):
    if 'user_data' in request.session:
        del request.session['user_data']
        del request.session['logged_profile_info']
        
        messages.success(request, ("You were loged out!"))
        return redirect("/login")
    else:
        return redirect("/login")
