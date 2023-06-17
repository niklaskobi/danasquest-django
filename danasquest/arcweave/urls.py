from django.urls import path
from . import views

urlpatterns = [
    path('view_import/', views.view_import, name="view_import"),
    path('play/<str:project_id>', views.next_element, name="next_element"),
]
