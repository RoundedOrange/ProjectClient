from django.urls import path
from Login import views
urlpatterns = [
    path('',views.login),
    path('register',views.register),
    path('send-captcha', views.send_captcha, name='send_captcha'),  # 新增发送验证码的 URL
<<<<<<< Updated upstream
]
=======
    path('logout',views.logout),
# 处理找回密码
    path('findpd', views.findpd, name='findpd'),  # 修改为findpd
   ]
>>>>>>> Stashed changes
