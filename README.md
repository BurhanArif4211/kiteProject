![](https://firebasestorage.googleapis.com/v0/b/potfolio-492d3.appspot.com/o/static%2Fmain1-light.png?alt=media&token=33bfec83-9a3e-4fbb-a740-0242a38253f3)
# Kite 

**_ A blazing fast portfolio plateform for self promoted graphic designers of Pakistan. _**

## **The Dev Team:**
[Amaan Ali](https://github.com/DeveloperAmanAli)
[Burhan Arif.](https://github.com/BurhanArif4211)
## **Others**
Soon!

# DOCS FOR FIREBASE (Specific)                                            


## user claims:
   
### when ever you run:
```
    encoded_user_data = req.session['user_data']                 get stored auth token in session
    decoded_user = base64.b64decode(encoded_user_data).decode()  decode the token because its encoded in base64 check signUpEmail() for more info
    claims = auth.verify_id_token(decoded_user)                  this will return above example data from user
    print(claims)
```
### Result:
```
   {'name': 'example', 'iss': 'https://securetoken.google.com/potfolio-492d3',
    'aud': 'potfolio-492d3', 'auth_time': 1700313585, 'user_id': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2',
    'sub': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2', 'iat': 1700313585, 'exp': 1700317185, 'email': 'example777@gmail.com',
    'email_verified': True, 'firebase': {'identities': {'email': ['example777@gmail.com']}, 'sign_in_provider': 'password'}, 'uid': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2'}
```
### Purpose:    
    The purpose for claims is to verify if a user actually exists in our infrastructure.
    also, the claim can provide us quickly with th uid of user to use in in other services (here uid is : 'user_id': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2')

    [REMEMBER!] : This System is used from firebase-rest-api (import firebase)



## user info
    when ever you run:
    user_data = fireauth.get_account_info(decoded_user)  for more info about "decoded_user", read above claims
    result:

    {'kind': 'identitytoolkitGetAccountInfoResponse', 'users': [{'localId': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2', 'email': 'example777@gmail.com',
    'displayName': 'example', 'photoUrl': 'https://storage.googleapis.com/potfolio-492d3.appspot.com/userData/jE0ZoxMelpWnvDsfto9GLtGhJuw2/pp.jpg',
    'passwordHash': 'UkVEQUNURUQ=', 'emailVerified': True, 'passwordUpdatedAt': 1700313563952, 'providerUserInfo': [{'providerId': 'password', 'displayName':
    'example', 'photoUrl': 'https://storage.googleapis.com/potfolio-492d3.appspot.com/userData/jE0ZoxMelpWnvDsfto9GLtGhJuw2/pp.jpg',
    'federatedId': 'example777@gmail.com', 'email': 'example777@gmail.com', 'rawId': 'example777@gmail.com'}], 'validSince': '1700313563',
    'lastLoginAt': '1700313563952', 'createdAt': '1700313563952', 'lastRefreshAt': '2023-11-18T13:19:23.952Z'}]}

     to clean this for use in application,

     user_data=user_data['users'][0]
     user_info = {

     "localID": user_data.get("localId"),
     "email": user_data.get("email"),
     "displayName": user_data.get("displayName"),
     "photoUrl": user_data.get("photoUrl"),

      }
      print(user_info)  this will boil down the data to only needed data

      {'localID': 'jE0ZoxasfasfLtGhJuw2', 'email': 'example@gmail.com',
      'displayName': 'example', 'photoUrl': 'example/pp.jpg'}

      Now this can be used in page contexts or any other place!

      [REMEMBER!] : This System is used from firebase-rest-api (import firebase)


 profile info from firestore collection "users1":

    when ever you run:
    user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
    print(user_profile_data)

    ^ This gives out:

    [<google.cloud.firestore_v1.base_document.DocumentSnapshot object at 0x0000026A567D7B50>]


    To get the dictionary, we use to_dict()
    print(user_profile_data[0].to_dict())

    ^ This gives out:

    {'niche': 'Senior Dev', 'company': 'Master Inc', 'links':
    {'3': '-', '1': 'example.com', '2': 'facebook.com'},
    'country': 'United States', 'user_id': 'jE0Zoxadfadfto9GLtGhJuw2',
    'about': 'I am an Enterpenuier in Manhattan', 'city': 'MANHATTAN'}


    The above data is passed normally as a dictionary to context or used in any api

    [REMEMBER!] : This System is used from firebase_admin (import firebase_admin)


 post info from firestore collection 'posts1':

   when ever you run:
    user_profile_data = store.collection('posts1').where('user_id', '==', claims['user_id']).get()








![](https://firebasestorage.googleapis.com/v0/b/potfolio-492d3.appspot.com/o/static%2Fmain1-dark.png)
# Kite 

_** A blazing fast portfolio plateform for self promoted graphic designers/freelancers. **_

## **Meet The Dev Team:**

[Amaan Ali](https://github.com/DeveloperAmanAli)
****
[Burhan Arif](https://github.com/BurhanArif4211)

## **Others**
Soon!

# DOCS FOR FIREBASE (Specific)                                            


## User claims:
   
### When ever you run:
```py
    encoded_user_data = req.session['user_data']                # get stored auth token in session
    decoded_user = base64.b64decode(encoded_user_data).decode() # decode the token because its encoded in base64 check signUpEmail() for more info
    claims = auth.verify_id_token(decoded_user)                 # this will return above example data from user
    print(claims)
```
### Result:
```py
   {'name': 'example', 'iss': 'https://securetoken.google.com/potfolio-492d3',
    'aud': 'potfolio-492d3', 'auth_time': 1700313585, 'user_id': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2',
    'sub': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2', 'iat': 1700313585, 'exp': 1700317185, 'email': 'example777@gmail.com',
    'email_verified': True, 'firebase': {'identities': {'email': ['example777@gmail.com']}, 'sign_in_provider': 'password'}, 'uid': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2'}
```
### Purpose:    
    The purpose for claims is to verify if a user actually exists in our infrastructure.
    also, the claim can provide us quickly with th uid of user to use in in other services (here uid is : 'user_id': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2')

    ** [REMEMBER!] : This System is used from firebase-rest-api (import firebase) ** 


## user info:

### When ever you run:
```py
    user_data = fireauth.get_account_info(decoded_user) # for more info about "decoded_user", read above claims
    result:

    {'kind': 'identitytoolkitGetAccountInfoResponse', 'users': [{'localId': 'jE0ZoxMelpWnvDsfto9GLtGhJuw2', 'email': 'example777@gmail.com',
    'displayName': 'example', 'photoUrl': 'https://storage.googleapis.com/potfolio-492d3.appspot.com/userData/jE0ZoxMelpWnvDsfto9GLtGhJuw2/pp.jpg',
    'passwordHash': 'UkVEQasfasf=', 'emailVerified': True, 'passwordUpdatedAt': 17001323952, 'providerUserInfo': [{'providerId': 'password', 'displayName':
    'example', 'photoUrl': 'wtsggsd.com/vDsfto9GLtGhJuw2/pp.jpg',
    'federatedId': 'example777@gmail.com', 'email': 'example777@gmail.com', 'rawId': 'example777@gmail.com'}], 'validSince': '1700afs',
    'lastLoginAt': '1700asf52', 'createdAt': '17asf3952', 'lastRefreshAt': '2023-1asdfasf:1asdf52Z'}]}

     # To clean this for use in application,

     user_data=user_data['users'][0]

     user_info = {
     "localID": user_data.get("localId"),
     "email": user_data.get("email"),
     "displayName": user_data.get("displayName"),
     "photoUrl": user_data.get("photoUrl"),
      }
      print(user_info)  #this will boil down the data to only needed data
```
### Result:
      {'localID': 'jE0ZoxasfasfLtGhJuw2', 'email': 'example@gmail.com',
      'displayName': 'example', 'photoUrl': 'example/pp.jpg'}

##### Now this can be used in page contexts or any other place!

    ** [REMEMBER!] : This System is used from firebase-rest-api (import firebase) **


## Profile info from firestore collection:

### When ever you run:

```py
    user_profile_data = store.collection('users1').where('user_id', '==', claims['user_id']).get()
    print(user_profile_data)

    # ^ This gives out:

    [<google.cloud.firestore_v1.base_document.DocumentSnapshot object at 0x0000026A567D7B50>]
    #To get the dictionary, we use to_dict()

    print(user_profile_data[0].to_dict())
    # ^ This gives out:

    {'niche': 'Senior Dev', 'company': 'Master Inc', 'links':
    {'3': '-', '1': 'example.com', '2': 'facebook.com'},
    'country': 'United States', 'user_id': 'jE0Zoxadfadfto9GLtGhJuw2',
    'about': 'I am an Enterpenuier in Manhattan', 'city': 'MANHATTAN'}
```
#### The above data is passed normally as a dictionary to context or used in any api

#### ** [REMEMBER!] : This System is used from firebase_admin (import firebase_admin) **


## post info from firestore collection:

###   When ever you run:
```py
    user_profile_data = store.collection('posts1').where('user_id', '==', claims['user_id']).get()
```
_*to be continued!*_





