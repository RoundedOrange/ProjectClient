from django.urls import path
from Dashboard import views
urlpatterns = [
    path('',views.main),
    path('main',views.main),
    path('personal_info',views.personal_info),
    path('change_password',views.change_password),
    path('possession_show',views.possession_show),
    path('possession_add',views.possession_add),
    path('possession_delete',views.possession_delete),
    path('change_info',views.change_info),
    path('task_show',views.task_show),
    
]