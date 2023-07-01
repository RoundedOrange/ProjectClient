from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=10,null=False)
    telephone = models.CharField(max_length=10)
    birth_date = models.DateField(null=True)
    is_administrator = models.BooleanField(default=False)
    register_time = models.DateField(null=False)
    signature = models.TextField(max_length=100,default="")
    avatar = models.ImageField(null=False,upload_to='avatar/')
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=20,null=True)
    gender = models.BooleanField(null=True)

class Dataset(models.Model):
    dataset_id = models.IntegerField(primary_key=True)
    size = models.IntegerField()
    description = models.TextField(max_length=100,default="")
    uploader = models.ForeignKey('User',on_delete=models.CASCADE)

class Model(models.Model):
    model_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=10)
    description = models.TextField(max_length=100,default="")

class Device(models.Model):
    device_id = models.IntegerField(primary_key=True)
    OS_CHOICES = (
        ('1','Windows'),
        ('2','Linux'),
        ('3','macOS'),
        ('4','iOS'),
        ('5','Android'),
    )
    OS = models.CharField(max_length=1,choices=OS_CHOICES,null=False)
    CPU = models.CharField(max_length=20,null=True)
    STATUS_CHOICES = (
        ('0','Normal'),
        ('1','Offline'),
        ('2','Error'),
    )
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='0')
    RAM = models.IntegerField()
    ROM = models.IntegerField()
    IP = models.CharField(max_length=15)
    can_run_cuda = models.BooleanField(default=False)
    description = models.TextField(max_length=100,default="")
    core_num = models.IntegerField(default=1)
    bandwidth = models.IntegerField()

class Task(models.Model):
    task_id = models.IntegerField(primary_key=True)
    start_time = models.DateField(null=False)
    end_time = models.DateField(null=True)
    accuracy = models.DecimalField(max_digits=5,decimal_places=4,default=0)
    publisher = models.ForeignKey('User',on_delete=models.CASCADE)
    dataset = models.ForeignKey('Dataset',on_delete=models.CASCADE)
    model = models.ForeignKey('Model',on_delete=models.CASCADE)
    device = models.ForeignKey('Device',on_delete=models.CASCADE)