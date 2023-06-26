from django.urls import path
from Dashboard import views
urlpatterns = [
    path('',views.main),
    path('main',views.main),
]