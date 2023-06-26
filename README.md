# ProjectClient
 
# 如何运行

## 提前下载

需要提前下载好如下软件

|软件名|版本号|
|:-:|:-:|
|anaconda|23.5.0|
|mysql|8.0.33|

## 环境配置

使用anaconda创建虚拟环境

```conda create project_client python=3.8```

激活虚拟环境

```conda activate project_client```

进入目录

```cd ProjectClient```

安装库

```pip install -r requirements.txt```

## 数据迁移

进入ProjectClient/Client目录

```cd Client```

迁移数据库数据

```python manage.py migrate```

## 运行

运行

```python manage.py runserver```