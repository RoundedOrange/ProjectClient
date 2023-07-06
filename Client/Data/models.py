from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=10,null=False,unique=True)
    real_name = models.CharField(max_length=10,null=False)
    telephone = models.CharField(max_length=11)
    birth_date = models.DateField(null=True)
    is_administrator = models.BooleanField(default=False)
    register_time = models.DateTimeField(auto_now_add=True)
    signature = models.TextField(max_length=100,default="")
    avatar = models.ImageField(null=False,upload_to='avatar/')
    password = models.CharField(max_length=256)
    email = models.CharField(max_length=20,null=True)
    gender = models.BooleanField(null=True)
    balance = models.IntegerField(default=0)

class Dataset(models.Model):
    dataset_id = models.AutoField(primary_key=True)
    size = models.IntegerField()
    description = models.TextField(max_length=100,default="")

class User_Dataset(models.Model):
    user = models.ForeignKey('User',on_delete=models.CASCADE)
    Dataset = models.ForeignKey('Dataset',on_delete=models.CASCADE)
    money = models.IntegerField()
    begin_date = models.DateField(null=False)
    end_date = models.DateField(null=False)

class Device(models.Model):
    device_id = models.AutoField(primary_key=True)
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
        ('0','Running'),
        ('1','Occupied'),
        ('2','Vacant'),
        ('3','Offline'),
    )
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='0')
    RAM = models.IntegerField()
    ROM = models.IntegerField()
    IP = models.CharField(max_length=15)
    can_run_cuda = models.BooleanField(default=False)
    description = models.TextField(max_length=100,default="")
    core_num = models.IntegerField(default=1)
    max_bandwidth = models.IntegerField()

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    start_time = models.DateField(null=False)
    end_time = models.DateField(null=True)
    accuracy = models.DecimalField(max_digits=5,decimal_places=4,default=0)
    publisher = models.ForeignKey('User',on_delete=models.CASCADE)
    dataset = models.ForeignKey('Dataset',on_delete=models.CASCADE)
    device = models.ForeignKey('Device',on_delete=models.CASCADE)