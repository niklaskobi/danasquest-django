import firebase_admin
from firebase_admin import firestore
import pyrebase
import os

COLLECTION_NAME = u'arcweave'
DOCUMENT_NAME = u'development-nk'

CONFIG_DATA_KEY = u'data'
ASSETS_DATA_KEY = u'assets'


def initialize_app():
    if not firebase_admin._apps:
        firebase_admin.initialize_app()


def send_to_firestore(data, assets):
    initialize_app()
    db = firestore.client()
    doc_ref = db.collection(COLLECTION_NAME).document(DOCUMENT_NAME)
    # TODO use batch write (https://firebase.google.com/docs/firestore/manage-data/transactions)
    if data:
        doc_ref.set({CONFIG_DATA_KEY: data})
    if assets:
        for asset in assets:
            doc_ref.set({ASSETS_DATA_KEY: asset['file']})


def read_from_firestore():
    initialize_app()
    db = firestore.client()

    # read all documents from collection
    # users_ref = db.collection(COLLECTION_NAME)
    # docs = users_ref.stream()
    # for doc in docs:
    #     test = doc.to_dict()
    #     print(f'{doc.id} => {doc.to_dict()}')

    doc_ref = db.collection(COLLECTION_NAME).document(DOCUMENT_NAME)
    doc = doc_ref.get()
    return doc.to_dict()["data"]

def upload_to_cloud_storage():
    # WIP:
    firebase = pyrebase.initialize_app()
    storage = firebase.storage()
