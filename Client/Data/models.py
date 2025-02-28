from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    nickname = models.CharField(max_length=20,null=False,unique=True)
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
    total_size = models.CharField(null=True,max_length=256)
    description = models.TextField(max_length=100,default="")
    dataset_name = models.CharField(max_length=256,null=True)
    data_num = models.IntegerField(null=True)
    is_graph = models.BooleanField(null=True)
    graph_size = models.IntegerField(null=True)
    def __str__(self):
        return self.description

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
    OS = models.CharField(max_length=1,choices=OS_CHOICES,null=True)
    CPU = models.CharField(max_length=20,null=True)
    STATUS_CHOICES = (
        ('0','Running'),
        ('1','Occupied'),
        ('2','Vacant'),
        ('3','Offline'),
    )
    status = models.CharField(max_length=1,choices=STATUS_CHOICES,default='0')
    RAM = models.IntegerField(null=True)
    ROM = models.IntegerField(null=True)
    IP = models.CharField(max_length=15,null=True)
    can_run_cuda = models.BooleanField(default=False)
    description = models.TextField(max_length=100,default="")
    core_num = models.IntegerField(default=1)
    max_bandwidth = models.IntegerField(null=True)
    is_server = models.BooleanField(default=False)
    GPU_num = models.IntegerField(default=0)
    def __str__(self):
        return "设备"+str(self.device_id)

class Task(models.Model):
    task_id = models.AutoField(primary_key=True)
    start_time = models.DateField(null=False)
    end_time = models.DateField(null=True)
    accuracy = models.DecimalField(max_digits=5,decimal_places=4,default=0)
    publisher = models.ForeignKey('User',on_delete=models.CASCADE)
    dataset = models.ForeignKey('Dataset',on_delete=models.CASCADE)
    cluster = models.ForeignKey('Device',on_delete=models.CASCADE)
    status = models.IntegerField(default=0)
    safety = models.IntegerField(null=True)
    speed = models.IntegerField(default=50)
    open_source = models.BooleanField(default=False)
    use_fed_model = models.BooleanField(null=True)
    log_name = models.CharField(max_length=256,null=True)
    parameter_file_name = models.CharField(max_length=256,null=True)

