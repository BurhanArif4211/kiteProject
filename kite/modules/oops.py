from django.shortcuts import render, HttpResponse, redirect
import datetime
import sqlite3

db= sqlite3.connect("temp.db")
dbx = db.cursor()
dbx.execute("create table if not exists notification(id text,body text,towards text,time text,by text,state integer,publicname text,action text)")

class Notifications:
    def insert(self,uid, body, towards, by ,publicname,action=""):
        db = sqlite3.connect("temp.db")
        dbx = db.cursor()
        dbx.execute("insert into notification values (?,?,?,?,?,?,?,?)", (uid, body, towards, datetime.datetime.now(), by, 0,publicname,action))
        db.commit()
        db.close()

    def newexists(self,towards):
        db = sqlite3.connect("temp.db")
        dbx = db.cursor()
        g=dbx.execute(f"select * from notification where state = 0 and towards = '{towards}'").fetchall()
        db.commit()
        db.close()
        return len(g)

    def see(self,uid):
        db = sqlite3.connect("temp.db")
        dbx = db.cursor()
        dbx.execute(f"UPDATE notification SET state = 1 WHERE id = '{uid}'")
        db.commit()
        db.close()

    def delete(self,uid):
        db = sqlite3.connect("temp.db")
        dbx = db.cursor()
        dbx.execute(f"delete from notification WHERE id = '{uid}'")
        db.commit()
        db.close()

    def fetchAction(self,oid):
        db = sqlite3.connect("temp.db")
        dbx = db.cursor()
        g = dbx.execute(f"select action,towards from notification WHERE id = '{oid}'").fetchone()
        db.commit()
        db.close()
        return g

    def fetch(self,uid):
        db = sqlite3.connect("temp.db")
        dbx = db.cursor()
        g = dbx.execute(f"select * from notification WHERE towards = '{uid}'").fetchall()
        db.commit()
        db.close()
        return g

    def do(self,action,other):
        if action == 'answer':
            return redirect(f'/contact/?person={other}')