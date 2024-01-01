from urllib.parse import urlparse
from django.shortcuts import render, HttpResponse, redirect
from django.template.response import TemplateResponse
from django.http import JsonResponse, HttpResponse
from django.template import loader
from django.contrib import messages
import random
import sqlite3
import base64
import datetime
from firebase_admin import auth
from ErrorCodes import STATUS_CODES
from .services.firebase import upload_image,validateLogin,getPublicUrl,AuthenticationError, fireauth, store# storage
from datetime import datetime, timedelta
from .modules.scorealgo import scorify

db = sqlite3.connect('temp.db')
dbx = db.cursor()
dbx.execute("create table if not exists rank(id, rank)")
def rankingF(request):
    try:
        claims, decoded_user = validateLogin(request)
    except AuthenticationError as e:
        return JsonResponse({"state":-1,"msg":"/login"})
    if not claims:
        return JsonResponse({"state":-1,"msg":"/login"})

    if not claims['email_verified']:
        return JsonResponse({"state":-1,"msg":"/kite"})
    else:
        current_time = datetime.now().time()
        # target time (10:30 AM)
        target_time = datetime.strptime("10:35", "%H:%M").time()

        # Compare the current time with the target time
        if current_time == target_time:
            print("It's 10:30 AM!")
            db = sqlite3.connect('temp.db')
            dbx = db.cursor()
            dbx.execute("truncate table rank")
            user1_collection_ref = store.collection("user1")
            # Get all documents in the "user1" collection
            docs = user1_collection_ref.stream()
            #for each ranking
            for docd in docs:
                doc = doc.to_dict()
                scorify(claim) 

        else:
            db = sqlite3.connect('temp.db')
            dbx = db.cursor()
            h = dbx.execute(f"select rank,score from rank where id = '{claims['user_id']}'").fetchone()
            print("It's not 10:30 AM yet.")
            return JsonResponse({"state":0,"data":h})