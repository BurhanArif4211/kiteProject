from django.contrib import admin
from django.urls import path
from kite.routeHandlers import apis,pages,asyncCompLoaders,authentication as auth

# handler404 = 'apis.path404'

urlpatterns = [
    #optimization
    # Burhan is banned at this point
    path('components/api/services/<str:oid>/',apis.selfService,name='serviceself'),
    path('components/api/notifications/',apis.notificationsApi,name='notifiapi'),

    # Pages
    path('community/',pages.communityPG,name='commpg'),
    # path('community/ranking',kite.ranking.rankingF,name='rs'),
    path('test/',pages.loadScroll,name='ls'),
    path('test/test',pages.test,name=''),
    path('',pages.index,name='home'),
    path('services/chosen/',apis.packageSelectedPage,name='serviceself'),
    path('login/',pages.loginPG,name='login'),
    path('kite/addservice',pages.serviceForm,name='serviceform'),
    path('kite/',pages.kitePG,name='kite'),
    path('kites/<str:publicProfileId>/', pages.publicKitePG, name='kitespublicprofile'),
    path('feed/', pages.feedPG, name='feed'),
    
    # Async Components loading 
    path('uploadpost/',asyncCompLoaders.uploadPostModal,name='uploadpost'),
    path('load/currentnotifications/',asyncCompLoaders.loadCurrentNotifications,name='loadnotifications'),
    path('load/messagebox/',asyncCompLoaders.loadMessageBox,name='loadmessagebox'),
    
    
    # Athentication APIs
    path('api/resetpassword/',auth.send_password_reset_email,name=''),
    path('api/login',auth.loginWithEmail,name='api/login'),
    path('api/googlelogin',auth.loginWithGoogle,name='api/googlelogin'),
    path('api/like/<str:targetPostId>/',apis.likeUserPost,name='like'),
    path('api/saveservice',apis.saveService,name='serviceapi'),
    path('api/follow/<str:publicProfileId>/',apis.followUserByPublicId,name='follow'),
    path('api/signup',auth.signUpWithEmail,name='api/signup'),
    path('api/createprofile',auth.createProfile,name='api/createprofile'),
    path('api/resendemailverification',apis.resendEmailVerification,name='resendemailverification'),
    path('api/logout',auth.logout,name='logout'),
    
    # Data Updating/Uploading APIs
    path('actions/notif',apis.notificationRequestHandler,name='api/uploaduserpic'),
    path('api/uploaduserpic',apis.uploadUserPic,name='api/uploaduserpic'),
    path('api/uploaduserpost',apis.uploadUserPost,name='api/uploadusrpost'),
    
    # Data loading APIs
    path('api/loaduserposts/<str:userIdFromUrl>',apis.publicLoadUserPost,name='api/loadThirdPersonPosts'),
    path('api/loaduserposts',apis.loadUserPosts,name='api/loaduserposts'),    
    # path('api/loadfeedpost/',apis.loadFeedPost,name='api/loadfeedpost'),    
    
    # Search
    path('api/search/', apis.searchUsersByName, name='searchusersbyname'),
]
