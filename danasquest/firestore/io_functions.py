import firebase_admin
from firebase_admin import firestore
from  google.cloud.storage.blob import Blob

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

    # users_ref = db.collection(COLLECTION_NAME)
    # docs = users_ref.stream()
    #
    # for doc in docs:
    #     print(f'{doc.id} => {doc.to_dict()}')

    doc_ref = db.collection(COLLECTION_NAME).document(DOCUMENT_NAME)
    print(f'Data from firestore document: {doc_ref.to_dict()}')
