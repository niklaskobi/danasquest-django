from django.urls import path
from . import views

urlpatterns = [
    path('view_import/', views.view_import, name="view_import"),
]
