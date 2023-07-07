from django.shortcuts import render
from Dashboard import forms
import hashlib
def hash_code(s,salt='DataWrangler'):
    h=hashlib.sha256()
    s+=salt
    h.update(s.encode())
    return h.hexdigest()

# Create your views here.
def main(request):
    return render(request,'main.html')
def personal_info(request):
    return render(request,'personal_info.html')
def change_password(request):
    if request.method == 'POST':
        change_password_form = forms.ChangePasswordForm(request.POST)
        message = "请检查填写的内容！"
        if change_password_form.is_valid():
            old_password = change_password_form.cleaned_data.get('old_password')
            new_password = change_password_form.cleaned_data.get('new_password')
            repeat_password = change_password_form.cleaned_data.get('repeat_password')
            try:
                user = models.User.objects.get(nickname=request.session.get('nickname',None))
            except:
                message = "用户不存在！"
                return render(request,'change_password.html',locals())
            if user.password == hash_code(old_password):
                if repeat_password == new_password:
                    user.password = new_password
                    user.save()
                    message = "修改成功！"
                    return render(request,'change_password.html',locals())
                else:
                    message = "两次新密码不一致！"
                    return render(request,'change_password.html',locals())
            else:
                message = "密码不正确！"
                return render(request,'change_password.html',locals())
    change_password_form = forms.ChangePasswordForm() 
    return render(request,'change_password.html',locals())
def possession_show(request):
    return render(request,'possession_show.html',locals())