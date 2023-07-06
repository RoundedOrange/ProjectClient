from django import forms
from captcha.fields import CaptchaField

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label="旧密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'input-material','placeholder':'请输入旧密码','autofocus':''}))
    new_password = forms.CharField(label="新密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'input-material','placeholder':'请输入新密码'}))
    repeat_password = forms.CharField(label="重复新密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'input-material','placeholder':'请重新输入新密码'}))
    captcha = CaptchaField(label='验证码')