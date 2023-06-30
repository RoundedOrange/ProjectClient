# ProjectClient
 
# 如何运行

## 约定

在此对README文件所使用符号做约定

|符号|意义|
|:-:|:-:|
|[root_dir]|项目所在根目录|
|[local_ip]|本地计算机ip地址|
|[dababase_ip]|数据库所在服务器ip地址|

## 提前下载

需要提前下载好如下软件

|软件名|版本号|
|:-:|:-:|
|anaconda|23.5.0|
|mysql|8.0.33|

## 环境配置

使用anaconda创建虚拟环境

```
conda create project_client python=3.8
```

激活虚拟环境

```
conda activate project_client
```

进入项目目录

```
cd [root_dir]
```

安装库

```
pip install -r requirements.txt
```

## 数据库设置

根据实际情况配置数据库，可以使用本地数据库，也可以使用云端数据库。

### 本地数据库设置

在使用本地数据库之前，需要先创建MysQL本地数据库。若使用云端服务器，这节可不看。

在MySQL中创建新数据库

```SQL
CREATE DATABASE FederatedLearning DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

修改```[root_dir]/Client/Client/settings.py```中```DATABASES```字段的数据

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',#不用修改
        'NAME': 'FederatedLearning',#数据库名字
        'USER': 'client',#用户名
        'PASSWORD': 'password',#密码
        'HOST': 'localhost',#云端数据库地址
        'POST': '3306'#端口
    }
}
```

进入[root_dir]/Client目录

```
cd [root_dir]/Client
```

迁移数据库数据

```
python manage.py migrate
```

### 云端数据库设置

修改```[root_dir]/Client/Client/settings.py```中```DATABASES```字段的数据，本项目目前已经预设好服务器ip连接，无需再修改。

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',#不用修改
        'NAME': 'FederatedLearning',#数据库名字
        'USER': 'client',#用户名
        'PASSWORD': 'password',#密码
        'HOST': '[database_ip]',#云端数据库地址
        'POST': '3306'#端口
    }
}
```

## 运行

进入[root_dir]/Client目录

```
cd [root_dir]/Client
```

运行

```
python manage.py runserver
```