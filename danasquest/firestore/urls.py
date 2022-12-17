from django.urls import path
from . import views

urlpatterns = [
    path('upload/', views.firestore_upload, name="firestore-upload"),
]
