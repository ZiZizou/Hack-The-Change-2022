from firebase_admin import credentials, initialize_app, firestore
from flask import Flask, Blueprint, request, jsonify, render_template, redirect, url_for

cred = credentials.Certificate("key.json")
initialize_app(cred)
db = firestore.client()
user_Ref = db.collection('user')

def add():
    try:
        input = {'Name':'Sarthak', 'Recyclable': '3', 'Non-Recyclable-Value': '5', 'Organic': '7', 'Non-Recyclable-No-Value': '6', 'Rebate': '5000'}
        user_Ref.document(str(8492384932)).set(input)
    except Exception as e:
        return f"An Error Occured: {e}"

add()
