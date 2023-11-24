from django.contrib import admin
from django.urls import path
from kite import views

urlpatterns = [
    
    # Pages
    path('',views.index,name='home'),
    path('login/',views.loginPG,name='login'),
    path('kite/',views.kitePG,name='kite'),
    path('api/follow/<str:publicProfileId>/',views.followUserByPublicId,name='follow'),
    path('kites/<str:publicProfileId>/', views.publicKitePG, name='kitespublicprofile'),
    path('uploadpost/',views.uploadPost,name='uploadpost'),
    
    # Athentication APIs
    path('api/login',views.loginWithEmail,name='api/login'),
    ## path('api/googlelogin',views.loginWithGoogle,name='api/googlelogin'),
    path('api/signup',views.signUpWithEmail,name='api/signup'),
    path('api/createprofile',views.createProfile,name='api/createprofile'),
    path('api/resendemailverification',views.resendEmailVerification,name='resendemailverification'),
    path('api/logout',views.logout,name='logout'),
    
    # Data Updating/Uploading APIs
    path('api/uploaduserpic',views.uploadUserPic,name='api/uploaduserpic'),
    path('api/uploaduserpost',views.uploadUserPost,name='api/uploadusrpost'),
    
    
    # Data loading APIs
    path('api/loaduserposts',views.loadUserPosts,name='api/loaduserposts'),    
]
