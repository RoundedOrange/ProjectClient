from django.shortcuts import render
from django.shortcuts import redirect
from Login import forms
from Data import models
import hashlib
from django.core.cache import cache
from django.http import JsonResponse
from django.utils.crypto import get_random_string
from django.conf import settings
from datetime import datetime
# 导入阿里云短信 SDK
from aliyunsdkcore.client import AcsClient
from aliyunsdkcore.request import CommonRequest
from django.views.decorators.csrf import csrf_exempt
# 获取阿里云短信相关配置
ALIYUN_ACCESS_KEY = settings.ALIYUN_ACCESS_KEY
ALIYUN_ACCESS_SECRET = settings.ALIYUN_ACCESS_SECRET
ALIYUN_SMS_SIGN_NAME = settings.ALIYUN_SMS_SIGN_NAME
ALIYUN_SMS_TEMPLATE_CODE = settings.ALIYUN_SMS_TEMPLATE_CODE

# 创建阿里云短信客户端
client = AcsClient(ALIYUN_ACCESS_KEY, ALIYUN_ACCESS_SECRET, 'default')


def hash_code(s, salt='DataWrangler'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


# Create your views here.
def login(request):
    if request.session.get('is_login', None):
        return redirect('/dashboard/')
    if request.method == 'POST':
        login_form = forms.LoginForm(request.POST)
        message = '请检查填写的内容！'
        if login_form.is_valid():
            nickname = login_form.cleaned_data.get('nickname')
            password = login_form.cleaned_data.get('password')
            try:
                user = models.User.objects.get(nickname=nickname)
            except:
                message = '用户不存在！'
                return render(request, 'login.html', locals())
            if user.password == hash_code(password):
                request.session['is_login'] = True
                request.session['nickname'] = user.nickname
                request.session['user_id'] = user.user_id
                return redirect('/dashboard/')
            else:
                message = '密码不正确！'
                return render(request, 'login.html', locals())
        else:
            return render(request, 'login.html', locals())
    login_form = forms.LoginForm()
    return render(request, 'login.html', locals())


def register(request):
    if request.session.get('is_login', None):
        return redirect('/dashboard/')
    if request.method == 'POST':
        register_form = forms.RegisterForm(request.POST)
        message = "请检查填写的内容！"
        if register_form.is_valid():
            nickname = register_form.cleaned_data.get('nickname')
            password1 = register_form.cleaned_data.get('password1')
            password2 = register_form.cleaned_data.get('password2')
            telephone = register_form.cleaned_data.get('telephone')
            captcha = register_form.cleaned_data.get('captcha')
            if password1 != password2:
                message = "两次输入的密码不同！"
                return render(request, 'register.html', locals())
            else:
                same_name_user = models.User.objects.filter(nickname=nickname)
                if same_name_user:
                    message = "用户名已经存在！"
                    return render(request, 'register.html', locals())
                same_telephone_user = models.User.objects.filter(telephone=telephone)
                if same_telephone_user:
                    message = "手机号已经被注册！"
                    return render(request, 'register.html', locals())
                    # 检查验证码是否匹配
                cache_key = f'register_captcha_{telephone}'
                cached_captcha = cache.get(cache_key)
                if not cached_captcha or captcha != cached_captcha:
                    message = "验证码不正确！"
                    return render(request, 'register.html', locals())
                new_user = models.User()
                new_user.nickname = nickname
                new_user.password = hash_code(password1)
                new_user.telephone = telephone
                # 获取当前日期和时间
                current_datetime = datetime.now()
                new_user.register_time = current_datetime
                new_user.save()
                return redirect('/login/')
        else:
            return render(request, 'register.html', locals())
    register_form = forms.RegisterForm()
    return render(request, 'register.html', locals())


# 发送验证码视图
@csrf_exempt
def send_captcha(request):
    if request.method == 'POST':
        telephone = request.POST.get('telephone')

        # 生成随机验证码
        captcha = get_random_string(length=6, allowed_chars='0123456789')

        # 缓存验证码，有效期为 5 分钟
        cache_key = f'register_captcha_{telephone}'
        cache.set(cache_key, captcha, 300)

        # 发送短信验证码
        aliyun_request = CommonRequest()
        aliyun_request.set_method('POST')
        aliyun_request.set_domain('dysmsapi.aliyuncs.com')
        aliyun_request.set_version('2017-05-25')
        aliyun_request.set_action_name('SendSms')
        aliyun_request.add_query_param('RegionId', 'cn-hangzhou')
        aliyun_request.add_query_param('PhoneNumbers', telephone)
        aliyun_request.add_query_param('SignName', '橘子')
        aliyun_request.add_query_param('TemplateCode', 'SMS_461825575')
        aliyun_request.add_query_param('TemplateParam', f'{{"code":"{captcha}"}}')

        response = client.do_action(aliyun_request)
        # 在这里可以处理短信发送结果，例如打印日志

        return JsonResponse({'status': 'success'})
    else:
        return JsonResponse({'status': 'error', 'message': 'Invalid request method.'})


def logout(request):
    if not request.session.get('is_login', None):
        return redirect('/login/')
    request.session.flush()
    return redirect('/login/')
