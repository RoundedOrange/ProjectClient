from django.shortcuts import render,redirect
from django.utils import timezone
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
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    return render(request,'main.html',locals())
def personal_info(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    return render(request,'personal_info.html',locals())
def change_password(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    if request.method == 'POST':
        change_password_form = forms.ChangePasswordForm(request.POST)
        message = "请检查填写的内容！"
        if change_password_form.is_valid():
            old_password = change_password_form.cleaned_data.get('old_password')
            new_password = change_password_form.cleaned_data.get('new_password')
            repeat_password = change_password_form.cleaned_data.get('repeat_password')
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
def change_info(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    if request.method == 'POST':
        change_info_form = forms.ChangeInfoForm(request.POST)
        message = "请检查填写的内容！"
        if change_info_form.is_valid():
            new_nickname = change_info_form.cleaned_data.get('nickname')
            new_birth_date = change_info_form.cleaned_data.get('birth_date')
            new_signature = change_info_form.cleaned_data.get('signature')
            new_gender = change_info_form.cleaned_data.get('gender')
            new_real_name = change_info_form.cleaned_data.get('real_name')
            message = "成功！"
            if(new_nickname != ""):
                if models.User.objects.get(nickname=new_nickname):
                    message = "用户名已被他人使用！"
                    return render(request,'change_info.html',locals())
                else:
                    user.nickname=new_nickname
                    user.save()
                    request.session['nickname'] = new_nickname
            if(new_birth_date != None):
                user.birth_date = new_birth_date
                user.save()
            if(new_signature != ""):
                user.signature = new_signature
                user.save()
            if(new_gender != ""):
                user.gender = new_gender
                user.save()
            if(new_real_name != ""):
                user.real_name = new_real_name
                user.save()
            return render(request,'change_info.html',locals())
    message = "只需修改想修改的字段，其余留空。"
    change_info_form = forms.ChangeInfoForm()
    return render(request,'change_info.html',locals())
def possession_show(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    try:
        devices = models.Device.objects.filter()
        return render(request,'possession_show.html',locals())
    except:
        message = "失败！"
        return render(request,'possession_show.html',locals())
    return render(request,'possession_show.html',locals())
def possession_add(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    target_id = request.GET.get('target_id')
    if target_id == None or int(target_id) != 0:
        if request.method == 'POST':
            possession_add_form = forms.PossessionAddForm(request.POST)
            message = "请检查填写的内容！"
            if possession_add_form.is_valid():
                device = models.Device()
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
                message = "操作成功！"
                return render(request,'possession_add.html',locals())
        possession = models.Device.objects.get(device_id=int(target_id))
        possession_add_form = forms.PossessionAddForm({
                        "OS": possession.OS,
                        "CPU": possession.CPU,
                        "RAM": possession.RAM,
                        "ROM": possession.ROM,
                        "can_run_cuda": possession.can_run_cuda,
                        "description": possession.description,
                        "core_num": possession.core_num,
                        "max_bandwidth": possession.max_bandwidth,
                        "is_server": possession.is_server,
                        "GPU_num": possession.GPU_num,
                    }
                )
        return render(request,'possession_add.html',locals())
    else:
        if request.method == 'POST':
            possession_add_form = forms.PossessionAddForm(request.POST)
            message = "请检查填写的内容！"
            if possession_add_form.is_valid():
                device = models.Device()
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
        possession_add_form = forms.PossessionAddForm()
        return render(request,'possession_add.html',locals())
        
        
def possession_delete(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    array = request.POST.getlist('checkbox')
    for id in array:
        models.Device.objects.get(device_id=id).delete()
    message = "删除成功！"
    try:
        devices = models.Device.objects.filter()
        return render(request,'possession_show.html',locals())
    except:
        message = "失败！"
        return render(request,'possession_show.html',locals())
    return render(request,'possession_show.html',locals())
def dataset_show(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    try:
        datasets = models.Dataset.objects.filter()
        return render(request,'dataset_show.html',locals())
    except:
        message = "失败！"
        return render(request,'dataset_show.html',locals())
    return render(request,'dataset_show.html',locals())
def dataset_add(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    target_id = request.GET.get('target_id')
    if target_id == None or int(target_id) != 0:
        if request.method == 'POST':
            dataset_add_form = forms.DatasetAddForm(request.POST)
            message = "请检查填写的内容！"
            if dataset_add_form.is_valid():
                dataset = models.Dataset()
                total_size = dataset_add_form.cleaned_data.get('total_size')
                description = dataset_add_form.cleaned_data.get('description')
                dataset_name = dataset_add_form.cleaned_data.get('dataset_name')
                data_num = dataset_add_form.cleaned_data.get('data_num')
                is_graph = dataset_add_form.cleaned_data.get('is_graph')
                graph_size = dataset_add_form.cleaned_data.get('graph_size')
                dataset.total_size = total_size
                dataset.description = description
                dataset.dataset_name = dataset_name
                dataset.data_num = data_num
                dataset.is_graph = is_graph
                dataset.graph_size = graph_size
                dataset.save()
                message = "操作成功！"
                return render(request,'dataset_add.html',locals())
        dataset = models.Dataset.objects.get(dataset_id=int(target_id))
        dataset_add_form = forms.DatasetAddForm({
                        "total_size": dataset.total_size,
                        "description": dataset.description,
                        "dataset_name": dataset.dataset_name,
                        "data_num": dataset.data_num,
                        "is_graph": dataset.is_graph,
                        "graph_size": dataset.graph_size,
                    }
                )
        return render(request,'dataset_add.html',locals())
    else:
        if request.method == 'POST':
            dataset_add_form = forms.DatasetAddForm(request.POST)
            message = "请检查填写的内容！"
            if dataset_add_form.is_valid():
                dataset = models.Dataset()
                total_size = dataset_add_form.cleaned_data.get('total_size')
                description = dataset_add_form.cleaned_data.get('description')
                dataset_name = dataset_add_form.cleaned_data.get('dataset_name')
                data_num = dataset_add_form.cleaned_data.get('data_num')
                is_graph = dataset_add_form.cleaned_data.get('is_graph')
                graph_size = dataset_add_form.cleaned_data.get('graph_size')
                dataset.total_size = total_size
                dataset.description = description
                dataset.dataset_name = dataset_name
                dataset.data_num = data_num
                dataset.is_graph = is_graph
                dataset.graph_size = graph_size
                dataset.save()
                message = "操作成功！"
                return render(request,'dataset_add.html',locals())
        dataset_add_form = forms.DatasetAddForm()
        return render(request,'dataset_add.html',locals())
def dataset_delete(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    array = request.POST.getlist('checkbox')
    for id in array:
        models.Dataset.objects.get(dataset_id=id).delete()
    message = "删除成功！"
    try:
        datasets = models.Dataset.objects.filter()
        return render(request,'dataset_show.html',locals())
    except:
        message = "失败！"
        return render(request,'dataset_show.html',locals())
    return render(request,'dataset_show.html',locals())
def task_show(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    try:
        tasks = models.Task.objects.filter()
        return render(request,'task_show.html',locals())
    except:
        message = "失败！"
        return render(request,'task_show.html',locals())
    return render(request,'task_show.html',locals())
def task_add(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    if request.method == 'POST':
        task_add_form = forms.TaskAddForm(request.POST)
        message = "请检查填写的内容！"
        if task_add_form.is_valid():
            task = models.Task()
            start_time = timezone.now()
            dataset = task_add_form.cleaned_data.get('dataset')
            device = task_add_form.cleaned_data.get('device')
    
            task.start_time = start_time
            task.dataset = dataset
            task.device = device
            task.publisher = models.User.objects.get(user_id = request.session.get('user_id'))
            task.save()
            message = "操作成功！"
            return render(request,'task_add.html',locals())
    task_add_form = forms.TaskAddForm()
    return render(request,'task_add.html',locals())
def task_delete(request):
    if not request.session.get('is_login',None):
        return redirect('/login')
    user = models.User.objects.get(user_id=request.session.get('user_id',None))
    array = request.POST.getlist('checkbox')
    for id in array:
        models.Task.objects.get(task_id=id).delete()
    message = "删除成功！"
    try:
        tasks = models.Task.objects.filter()
        return render(request,'task_show.html',locals())
    except:
        message = "失败！"
        return render(request,'task_show.html',locals())
    return render(request,'task_show.html',locals())