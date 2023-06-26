# ProjectClient
 
# 如何运行

## 环境配置

1. 使用anaconda创建虚拟环境
```conda create project_client python=3.8```

2. 激活虚拟环境
```conda activate project_client```

3. 进入目录
```cd ProjectClient```

4. 安装库
```pip install -r requirements.txt```

## 数据迁移

1. 进入ProjectClient/Client目录
```cd Client```

2. 迁移数据库数据
```python manage.py migrate```

## 运行

1. 运行
```python manage.py runserver```