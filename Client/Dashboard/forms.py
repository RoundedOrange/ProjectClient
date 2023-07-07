from django import forms
from captcha.fields import CaptchaField

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