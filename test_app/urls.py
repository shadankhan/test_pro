from django.urls import path
from test_app import views

urlpatterns = [
   path('apple/', views.apple, name="apple"),
   path('orange/', views.orange, name="orange")
]