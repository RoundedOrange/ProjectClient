from django.contrib import admin
from Data.models import User,Dataset,User_Dataset,Device,Task
# Register your models here.
admin.site.register(User)
admin.site.register(Dataset)
admin.site.register(User_Dataset)
admin.site.register(Device)
admin.site.register(Task)