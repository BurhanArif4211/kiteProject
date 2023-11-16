from django.contrib import admin
from django.urls import path
from kite import views

urlpatterns = [
    path('',views.index,name='home'),
    # path('about/',views.about,name='about'),
    # path('concept/',views.concept,name='concept'),
    # path('info/',views.info,name='info'),
    path('login/',views.loginPG,name='login'),
    path('kite/',views.kitePG,name='kite'),
    path('api/signup',views.signUpWithEmail,name='api/signup'),
    path('api/login',views.loginWithEmail,name='api/login'),
    path('api/googlelogin',views.loginWithGoogle,name='api/googlelogin'),
    path('api/resendemailverification',views.resendEmailVerification,name='resendemailverification'),
    path('api/logout',views.logout,name='logout'),
    path('api/createprofile',views.createProfile,name='api/createprofile'),
    
]
