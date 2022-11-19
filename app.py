from firebase_admin import credentials, initialize_app, firestore
from flask import Flask, Blueprint, request, jsonify, render_template, redirect, url_for

cred = credentials.Certificate("key.json")
initialize_app(cred)
db = firestore.client()
user_Ref = db.collection('user')

def add():
    try:
        input = {'Name':'Sarthak', 'Non-Recyclable': 0, 'Recyclable-Value': 0, 'Organic': 0, 'Recyclable-No-Value': 0, 'Rebate': 5000}
        user_Ref.document(str(8972342342)).set(input)
    except Exception as e:
        return f"An Error Occured: {e}"

def edit(category):

    try:
        all_users = [doc.to_dict() for doc in user_Ref.stream()]
        for user in all_users:
            if 'Name' in user and user['Name']=="Sarthak":

                if category == "non-recyclable":
                    user_Ref.document(str(8972342342)).update({"Non-Recyclable": firestore.Increment(1)}) 
                elif category == "recyclable":
                    user_Ref.document(str(8972342342)).update({"Recyclable-Value": firestore.Increment(1)}) 
                elif category == "organic": 
                    user_Ref.document(str(8972342342)).update({"Organic": firestore.Increment(100)}) 

                
    except Exception as e:
        return f"An Error Occured: {e}"

edit("organic")