from django.urls import path
from Dashboard import views
urlpatterns = [
    path('',views.hello),
    path('hello',views.hello),
]