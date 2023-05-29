import firebase_admin
from firebase_admin import firestore
import pyrebase
from google.cloud import storage

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

def upload_to_cloud_storage(name, content):
    # Initialize
    client = storage.Client()
    bucket = client.get_bucket('danasquest-1d1c2.appspot.com')

    # Download
    # blob = bucket.get_blob('project_settings.json')
    # print(blob.download_as_string())

    # Upload
    # blob2 = bucket.blob('remote/path/storage.txt')
    # blob2.upload_from_filename(filename='/local/path.txt')

def upload_blob_from_memory(file_path, destination_blob_name):
    """Uploads a file to the bucket."""

    # The ID of your GCS bucket
    bucket_name = "danasquest-1d1c2.appspot.com"

    # Initialize
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)

    blob = bucket.blob(file_path)
    blob.upload_from_filename(filename=file_path)

    print(
        f"Uploaded file: {file_path} to bucket: {bucket_name} and blob: {destination_blob_name}"
    )
