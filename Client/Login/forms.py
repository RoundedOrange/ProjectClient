from django import forms
from captcha.fields import CaptchaField

class LoginForm(forms.Form):
    nickname = forms.CharField(label="用户名",max_length=128,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入用户名','autofocus':''}))
    password = forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'input-material','placeholder':'请输入密码'}))
    captcha = CaptchaField(label='验证码')

class RegisterForm(forms.Form):
    nickname = forms.CharField(label="用户名",max_length=128,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入用户名','autofocus':''}))
    password1 = forms.CharField(label="密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'input-material','placeholder':'请输入密码'}))
    password2 = forms.CharField(label="确认密码",max_length=256,widget=forms.PasswordInput(attrs={'class':'input-material','placeholder':'再次输入密码'}))
    telephone = forms.CharField(label="手机号",max_length=11,widget=forms.TextInput(attrs={'class':'input-material','placeholder':'请输入11位手机号'}))
    captcha = CaptchaField(label='验证码')