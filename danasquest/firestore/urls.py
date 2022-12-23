from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.firestore_upload, name="firestore_upload"),
    path('viewuploaded/', views.view_uploaded_chunks, name="view_uploaded_chunks"),
]
