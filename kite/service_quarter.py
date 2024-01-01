"""
This file serves with all the needed import and common functions e.g : randomId()
"""
from urllib.parse import urlparse
from django.shortcuts import render, HttpResponse, redirect
import re as regexp
from django.template.response import TemplateResponse
from django.http import JsonResponse, HttpResponse
from django.template import loader
from django.contrib import messages
import random
import base64
import datetime
from firebase_admin import auth, exceptions
import json
from ErrorCodes import STATUS_CODES
from .services.firebase import upload_image,validateLogin,getPublicUrl,AuthenticationError, fireauth, store
from .modules.scorealgo import scorify
from fubam import *
import sqlite3
from .modules.oops import Notifications

from fubam import render_pythonMarkup

"""This is new"""

from .modules.postsalgo import fetch_documents_noalgo,post_fetching_algo
from kite.modules.rankalgo import rankUsers


sdb = sqlite3.connect('temp.db')
dbx = sdb.cursor()
dbx.execute("CREATE TABLE IF NOT EXISTS servers(id TEXT, oid TEXT, json TEXT)")




def getUserInfo(decoded_user):
    # * This function takes current auth token, fetches current user's auth-related personal data, right now, only 4 fields are useful
    # * But in future, this will be used to figure out if a user has google login or normal email login.
    user_info=fireauth.get_account_info(decoded_user)['users'][0]
    user_info = {
            "localID":user_info.get("localId"),
            "email": user_info.get("email"),
            "displayName": user_info.get("displayName"),
            "photoUrl": user_info.get("photoUrl"),
            }
    return user_info

def userIdtoPublicId(user_id):
    # * * This Function Takes a user's privatedUser_id to exchange it for his publicId
    return store.collection('users1').where('user_id','==',user_id).get()[0].to_dict()['publicProfileId']

def getProfileInfo(publicProfileId):
    # * * This function gets all profile data of a user from firebase mainly for cutom filter in the info_filters.py file
    return store.collection('users1').where('publicProfileId','==',publicProfileId).get()[0].to_dict()


def resendEmailVerification(request):
    # This is useless for now
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        print(f"Authentication error: {e}")
        return redirect("/login")
    fireauth.send_email_verification(decoded_user)
    tries = 3   # justfor testing # TODO add custom claims to check how many times the user has sent email verification.
    messages.success(request, (f'Email Resent. Tries Remain: {tries}'))
    return redirect("/login")


def path404(request, slug, exception=None, status=404):
    return render(request, 'templates/404.html', {"slug": slug})



def get_main_domain(input_link):
    parsed_url = urlparse(input_link)
    domain_parts = parsed_url.netloc.split('.')
    if len(domain_parts) > 1:
        main_domain = domain_parts[-2]
    else:
        main_domain = parsed_url.netloc
    return main_domain.split('.')[0]





def randomId():
    returnable = ""
    raw = "qwertyuiopasdfghjklzxcvbnm_1234567890"
    for i in range(20):
        q = random.randint(0, len(raw) - 1)
        returnable += raw[q]
    return returnable


def loadScroll(request):
    return render(request, "testOnScroll.html")

def test(request):
    return HttpResponse(
        [button(
            {"class":"wide","style":f"background-color : rgb({random.randint(0, 255)},{random.randint(0, 255)},{random.randint(0, 255)})"},
              chr(128516 + random.randint(0, 60))
        ) for i in range(600)]

    )


def checkPasswordValidation(password):
    pattern = r"^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$"
    return bool(regexp.match(pattern, password))