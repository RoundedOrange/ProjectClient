from django.contrib import admin
from Data.models import User,Dataset,Model,Device,Task
# Register your models here.
admin.site.register(User)
admin.site.register(Dataset)
admin.site.register(Model)
admin.site.register(Device)
admin.site.register(Task)