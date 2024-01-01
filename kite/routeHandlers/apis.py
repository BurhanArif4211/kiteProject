from kite.service_quarter import *

def searchUsersByName(request):
    try:
        query = request.GET['qN']# qN stand for query name 
    except KeyError:
        return redirect('/') #JsonResponse({'error': 'Missing query parameter "qN"'}, status=400)

    query_result = store.collection('users1').where('display_name', '==', query).get()
     
    users_data = []
    for doc in query_result:
        user_data = doc.to_dict()
        print(user_data)
        user_info = {'display_name': user_data.get('display_name'),
                     'publicProfileId': user_data.get('publicProfileId')}
        users_data.append(user_info)

    return JsonResponse({'users': users_data})


def notificationRequestHandler(request):
    try:
        claims, decoded_user = validateLogin(request)
        if not claims:
            return TemplateResponse(request, "home/index.html")
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")

    Notifications().see(request.GET.get("id"))
    fetchedAction = Notifications().fetchAction(request.GET.get("id"))
    return Notifications().do(fetchedAction[0],fetchedAction[1])

def notificationsApi(request):
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        return JsonResponse({"state":-1})
    if not claims:
        return JsonResponse({"state":-1})

    if not claims['email_verified']:
        return JsonResponse({"state":-1})
    else:
        profile = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
        publicProfileId = profile.get('publicProfileId')
        jf = Notifications().fetch(publicProfileId)
        jn = Notifications().newexists(publicProfileId)
        jsoncode = {
            "new" : jn,
            "list" : jf
        }
        return JsonResponse({"state":0, "json":jsoncode})

def packageSelectedPage(request):
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        return redirect('/login')
    if not claims:
        return redirect('/login')

    if not claims['email_verified']:
        return redirect('/kite')
    else:
        circuit = request.GET.get('circuit')
        route = circuit
        profile = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
        publicName = profile.get('display_name')
        publicProfileId = profile.get('publicProfileId')
        sdb = sqlite3.connect('temp.db')
        dbx = sdb.cursor()
        g = dbx.execute(f"SELECT oid, json FROM servers WHERE id = '{route}'").fetchone()
        Notifications().insert(randomId(), f"Your {json.loads(g[1])['services']} package is selected", g[0], publicProfileId, publicName, action='answer')
        sdb.commit()
        return HttpResponse(
            div(
                h1(
                    "Request has been submitted"
                )
            )
        )




def selfService(request, oid):
    sdb = sqlite3.connect('temp.db')
    dbx = sdb.cursor()
    g=[]
    g = dbx.execute('SELECT * FROM servers WHERE oid = ?', (oid,)).fetchall()
    sdb.commit()
    return HttpResponse(render_pythonMarkup("tools/json_to_html", resources={"jdata":g}))


def saveService(request):
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        return JsonResponse({"state":-1,"msg":"/login"})
    if not claims:
        return JsonResponse({"state":-1,"msg":"/login"})

    if not claims['email_verified']:
        return JsonResponse({"state":-1,"msg":"/kite"})
    if request.method == 'POST':
        user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
        sdb = sqlite3.connect('temp.db')
        dbx = sdb.cursor()
        decoded_values = [key for key, value in request.POST.items()]
        data = json.loads(request.body.decode('utf-8'))
        json_data = data.get('json')
        dbx.execute("INSERT INTO servers (id, oid, json) VALUES (?, ?, ?)",(randomId(),user_profile_data[0].to_dict().get('publicProfileId'),json_data))

        sdb.commit()
        return JsonResponse({
            "state":0,
            "msg":"<script>location.href='/kite'</script>"
        })

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
                    profile = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
                    post_profile.reference.update({'likes': likers})
                    publicName = profile.get('display_name')
                    publicProfileId = profile.get('publicProfileId')
                    Notifications().insert(randomId(), f"Liked your post","Post wala user", publicProfileId, publicName, action='like') #TODO USer ki id chahiyay yahan posts wala user main tab kam kray ga yah! UI dekh lena (public profile id) yah toh yeh krlo k har post k like main aik jga user ki public id {{likh}} dena or request main pass krna wrna yeh krna k yahan par post ki id say profile id fetch krlena lekin connection lgay ga!!!
                    return HttpResponse('liked')
            else:
                return HttpResponse('posterror')
        else:
            return HttpResponse('posterror')


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
            profile = store.collection('users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()
            publicName = profile.get('display_name')
            publicProfileIdOfLoggeduser = profile.get('publicProfileId')
            # these things help to send notification things at upper 3 lines
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
                Notifications().insert(randomId(), f"Followed you",publicProfileId, publicProfileIdOfLoggeduser, publicName, action='follow')
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

def publicLoadUserPost(request,userIdFromUrl):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest': 
        
        posts_info = []
        user_profile_data = store.collection('users1').where('publicProfileId', '==', userIdFromUrl).get()[0].to_dict()
        publicProfileId=user_profile_data['publicProfileId']
        if 'posts' in user_profile_data:
            posts = user_profile_data['posts']
            for postId in posts:
                post_info = store.collection('posts1').document(postId).get().to_dict()
                posts_info.append(post_info)
                
        context={
            "publicProfileId":publicProfileId,
            'posts_info':posts_info
        }
        
        return TemplateResponse(request,'kite/posts-grid.html',context) # this is much simpler than pmx nonsense

    else:
        return redirect('/')


def loadUserPosts(request):
 if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
    
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")

    user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
    if len(user_profile_data)>0:
        user_profile_data=user_profile_data[0].to_dict()

    posts_info = [doc.to_dict() for doc in store.collection('posts1').where('public_profile_id', '==', user_profile_data['publicProfileId']).get()]
    current_profile_info = store.collection(
        'users1').where('user_id', '==', claims['user_id']).get()[0].to_dict()

    pp_url=current_profile_info.get('pp_url')
    displayName=current_profile_info.get('display_name')

    return HttpResponse(render_pythonMarkup('kite/posts-grid', resources={'posts': posts_info, 'default':{'pp_url':pp_url,'displayName':displayName,"localID" : claims['user_id'] }}))
 else:
     return redirect('/')


def uploadUserPic(request):
    # print(request.FILES)
    if request.method == 'POST'and request.FILES['profilePicture']:
        try:
            claims, decoded_user = validateLogin(request)
        except AuthenticationError as e:
            print(f"Authentication error: {e}")
            return redirect("/login")

        publicProfileId = userIdtoPublicId(claims['user_id'])

        profile_picture = request.FILES['profilePicture']
        file_path = f"userData/{publicProfileId}/pp.jpg"
        
        # Upload the image to Firebase Storage using your existing function
        pp_url = upload_image(file_path, profile_picture.file,profile_picture.content_type)
        auth.update_user(claims['user_id'], photo_url=pp_url,)
        user_query = store.collection('users1').where('user_id', '==', claims['user_id']).stream()
        for doc in user_query:
            # adding current time in orfer to prevent caching this sucessfully fixes the prfile-not-updating-bug. :)
            store.collection('users1').document(doc.id).update({'pp_url': f"{pp_url}?updatedOn={datetime.datetime.now()}"})
        #########################################################

        return JsonResponse({pp_url})
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

        # Upload the image to Firebase Storage 
        post_url = upload_image(file_path, postImage.file, postImage.content_type)

        store.collection('posts1').document(postId).set(
            {
                'public_profile_id': userIdtoPublicId(claims['user_id']),
                'post_url': post_url,
                'post_id': randomId(),
                'post_description': postDescription,
                'likes':[],
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


