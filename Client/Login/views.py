from django.shortcuts import render
from django.shortcuts import redirect
from Login import forms
import hashlib
def hash_code(s,salt='DataWrangler'):
    h=hashlib.sha256()
    s+=salt
    h.update(s.encode())
    return h.hexdigest()
# Create your views here.
def login(request):
    if request.session.get('is_login',None):
        return redirect('/')
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
                return redirect('/')
            else:
                message = '密码不正确！'
                return render(request,'login.html',locals())
        else:
            return render(request,'login.html',locals())
    login_form = forms.LoginForm()
    return render(request,'login.html',locals())
def register(request):
    return render(request,'register.html')
def logout(request):
    if not request.session.get('is_login',None):
        return redirect('/login/')
    request.session.flush()
    return redirect('/login/')