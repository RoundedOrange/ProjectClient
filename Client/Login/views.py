from django.shortcuts import render
from django.shortcuts import redirect
from Login import forms
from Data import models
import hashlib
def hash_code(s,salt='DataWrangler'):
    h=hashlib.sha256()
    s+=salt
    h.update(s.encode())
    return h.hexdigest()
# Create your views here.
def login(request):
    if request.session.get('is_login',None):
        return redirect('/dashboard/')
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            nickname = login_form.cleaned_data.get('nickname')
            password = login_form.cleaned_data.get('password')
            try:
                print("搜索用户")
                user = models.User.objects.get(nickname=nickname)
            except:
                message = '用户不存在！'
                return render(request,'login.html',locals())
            if user.password == hash_code(password):
                #request.session['is_login'] = True
                #request.session['nickname'] = user.nickname
                #request.session['user_id'] = user.user_id
                return redirect('/dashboard/')
            else:
                message = '密码不正确！'
                return render(request,'login.html',locals())
        else:
            return render(request,'login.html',locals())
    login_form = forms.LoginForm()
    return render(request,'login.html',locals())
def register(request):
    if request.session.get('is_login',None):
        return redirect('/dashboard/')
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            nickname = register_form.cleaned_data.get('nickname')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            telephone = register_form.cleaned_data.get('telephone')
            if password1 != password2:
                message = "两次输入的密码不同！"
                return render(request,'register.html',locals())
            else:
                same_name_user= models.User.objects.filter(nickname=nickname)
                if same_name_user:
                    message = "用户名已经存在！"
                    return render(request,'register.html',locals())
                same_telephone_user = models.User.objects.filter(telephone=telephone)
                if same_telephone_user:
                    message = "手机号已经被注册！"
                    return render(request,'register.html',locals())
                new_user = models.User()
                new_user.nickname = nickname
                new_user.password = hash_code(password1)
                new_user.telephone = telephone
                #new_user.save()
                return redirect('/login/')
        else:
            return render(request,'register.html',locals())
    register_form = forms.RegisterForm()
    return render(request,'register.html',locals())
def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/login/')
    request.session.flush()
    return redirect('/login/')