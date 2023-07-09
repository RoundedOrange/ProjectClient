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
    path('dataset_show',views.dataset_show),
    path('dataset_add',views.dataset_add),
    path('dataset_delete',views.dataset_delete),
    path('task_show',views.task_show),
    path('task_add',views.task_add),
    path('task_delete',views.task_delete),
    path('change_info',views.change_info),
    
]