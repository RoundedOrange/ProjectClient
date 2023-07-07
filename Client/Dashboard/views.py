from django.shortcuts import render
from Dashboard import forms
from Data import models
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
    try:
        devices = models.Device.objects.filter()
        return render(request,'possission_show.html',locals())

    except:
        message = "失败！"
        return render(request,'possession_show.html',locals())
    return render(request,'possession_show.html',locals())
def possession_add(request):
    if request.method == 'POST':
        possession_add_form = forms.PossessionAddForm(request.POST)
        message = "请检查填写的内容！"
        if possession_add_form.is_valid():
            device = models.Device()
            #try:
            OS = possession_add_form.cleaned_data.get('OS')
            CPU = possession_add_form.cleaned_data.get('CPU')
            RAM = possession_add_form.cleaned_data.get('RAM')
            ROM = possession_add_form.cleaned_data.get('ROM')
            can_run_cuda = possession_add_form.cleaned_data.get('can_run_cuda')
            description = possession_add_form.cleaned_data.get('description')
            core_num = possession_add_form.cleaned_data.get('core_num')
            max_bandwidth = possession_add_form.cleaned_data.get('max_bandwidth')
            is_server = possession_add_form.cleaned_data.get('is_server')
            GPU_num = possession_add_form.cleaned_data.get('GPU_num')
            device.OS = OS
            device.CPU = CPU
            device.RAM = RAM if (RAM != '') else 0
            device.ROM = ROM if (ROM != '') else 0
            device.can_run_cuda = can_run_cuda
            device.description = description
            device.core_num = core_num if (core_num != None) else 0
            device.max_bandwidth = max_bandwidth if (max_bandwidth != None) else 0
            device.is_server = is_server
            device.GPU_num = GPU_num if (GPU_num != None) else 0
            device.IP = '0.0.0.0'
            device.save()
            message = "添加成功！"
            return render(request,'possession_add.html',locals())
            #except:
                #message = "添加失败！"
                #return render(request,'possession_add.html',locals())
    possession_add_form = forms.PossessionAddForm()
    return render(request,'possession_add.html',locals())