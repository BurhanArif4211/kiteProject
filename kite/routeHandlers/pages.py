from kite.service_quarter import *


def communityPG(request):
    try:
        claims, decoded_user = validateLogin(request)
        if not claims:
            return TemplateResponse(request, "home/index.html")
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")

    users=store.collection('users1').get()
    userList=[]
    for i in range(len(users)):
        userList.append(users[i].to_dict())

    profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
    context = {
        'default':{'pp_url':profile_data['pp_url'],'display_name':profile_data['display_name']},
        'allUsers':userList,
        'profile_info':profile_data,
    }
    return TemplateResponse(request, "home/community.html", context)

def serviceForm(request):
    return render(request,'templates/add-service.html')

def index(request):
    
    # try:
    #     claims, decoded_user = validateLogin(request)
    #     if not claims:
    #         return TemplateResponse(request, "home/index.html")
    # except AuthenticationError as e:
    #     print(f"Authentication error: {e}")
    #     return redirect("/login")

    # users=store.collection('users1').get()
    # profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
    # me = profile_data.get("publicProfileId")
    # userListArr = []
    
    # for i in range(len(users)):
    #     x = rankUsers(users[i].to_dict().get("user_id"), me)
    #     userListArr.append([users[i].to_dict(), x[1]])
    
    # sortedR = [item[0] for item in sorted(userListArr, key=lambda x: x[1], reverse=True)]
    # context = {
    # }
    return TemplateResponse(request, "home/index.html")



def feedPG(request):
    # Fetch a single random post
    claims, decoded_user=validateLogin(request)
    postss_data = store.collection('posts1').get()


    posts_data = fetch_documents_noalgo(limit=50)
    """
    Their are two functions fetch_ovcuments_algo and post_feetching_no-algo
    Now we will use fetch_docume... with limit 50 coz we don't have a lots of posts and also if we use 10 as a limit or even 50 we are going to get last 10 or 50 from firebase for this reason i used 50, which cause more probablity of user not reloaing the postpage or leaving the page early
    """

    user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
    pp_url=user_profile_data['pp_url']
    displayName=user_profile_data['display_name']
    
    context={'posts': posts_data,'default':{'pp_url':pp_url,'displayName':displayName,"claims" : claims }}
    # print(context)
    return render(request, 'feed/feed.html',context)

def kitePG(request):

    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")

    if not claims:
        messages.warning(request, ("Please Signup/Login In order to Continue to your kite."))
        return redirect('/login')

    if not claims['email_verified']:
        del request.session['user_data']
        messages.warning(request, ("Please Verify Your Account Email before Going Further! Check your email Inbox."))
        
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
    elif publicProfileId==request.session['logged_profile_info']['publicProfileId']:
        return redirect('/kite')
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

