from django import forms
from captcha.fields import CaptchaField
from Data import models
class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label="旧密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'input-material','placeholder':'请输入旧密码','autofocus':''}))
    new_password = forms.CharField(label="新密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'input-material','placeholder':'请输入新密码'}))
    repeat_password = forms.CharField(label="重复新密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'input-material','placeholder':'请重新输入新密码'}))
    captcha = CaptchaField(label='验证码')

class PossessionAddForm(forms.Form):
    OS = forms.ChoiceField(choices=(('1','Windows'),('2','Linux'),('3','macOS'),('4','iOS'),('5','Android')))
    CPU =  forms.CharField(label="CPU",required=False,max_length=256,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入CPU'}))
    RAM = forms.CharField(label="RAM（单位：MB）",required=False,max_length=256,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入RAM'}))
    ROM = forms.CharField(label="ROM（单位：MB）",required=False,max_length=256,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入ROM'}))
    can_run_cuda = forms.BooleanField(label="是否能用CUDA",required=False,widget=forms.CheckboxInput(attrs={'id':'can_run_cuda_checkbox'}))
    description = forms.CharField(label="描述",required=False,max_length=256,widget=forms.Textarea(attrs={'class':'input-material','placeholder':'请填写描述'}))
    core_num = forms.IntegerField(label="核心数",required=False,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入核心数'}))
    max_bandwidth = forms.IntegerField(label="最大带宽（单位：MB/s）",required=False,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入最大带宽'}))
    is_server = forms.BooleanField(label="是否为服务器",required=False,widget=forms.CheckboxInput(attrs={'id':'is_server_checkbox'}))
    GPU_num = forms.IntegerField(label="GPU数",required=False,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入GPU数'}))

class ChangeInfoForm(forms.Form):
    nickname = forms.CharField(label="用户名",required=False,max_length=20,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入新用户名'}))
    birth_date = forms.DateField(label='日期', widget=forms.DateInput(attrs={'type':'date'}),required=False)
    signature = forms.CharField(label="签名",required=False,max_length=256,widget=forms.Textarea(attrs={'class':'input-material','placeholder':'请填写签名'}))
    gender = forms.ChoiceField(choices=((True,'男'),(False,'女')), widget=forms.RadioSelect,required=False)
    real_name = forms.CharField(label="真实姓名",required=False,max_length=10,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入真实姓名'}))

class DatasetAddForm(forms.Form):
    total_size = forms.IntegerField(label="总大小",required=False,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入总大小'}))
    description = forms.CharField(label="描述",required=False,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入数据集描述'}))
    dataset_name = forms.CharField(label="数据集名称",max_length=256,required=False,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入数据集名称'}))
    data_num = forms.IntegerField(label="条目数",required=False,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入数据条目数'}))
    is_graph = forms.BooleanField(label="是否为图",required=False,widget=forms.CheckboxInput(attrs={'id':'is_graph_checkbox'}))
    graph_size =  forms.IntegerField(label="图大小",required=False,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入图大小'}))

class TaskAddForm(forms.Form):
    dataset = forms.ModelChoiceField(label='数据集',queryset=models.Dataset.objects.all())
    cluster = forms.ModelChoiceField(label='集群',queryset=models.Device.objects.all())
    open_source = forms.BooleanField(label="是否开源",widget=forms.CheckboxInput(attrs={'id':'open_source'}))
    use_fed_model = forms.BooleanField(label="是否使用联邦学习",widget=forms.CheckboxInput(attrs={'id':'use_fed_model'}))