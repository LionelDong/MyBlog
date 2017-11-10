# MyBlog
* python版本：python3
* django版本：django1.11
* 用到的包,均可使用pip install安装
 
    1. pymysql
    1. django
    1. pillow
    1. markdown
    1. django-ckeditor
    1. django-haystack
    1. whoosh
    1. jieba 
* 后台使用django进行管理
* 数据库使用mysql
* 将代码clone到本地，在MyBlog文件夹下的setting文件中更改自己的数据库配置
```
 DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'myblog',
        'HOST': '127.0.0.1',
        'PORT': '3306',
        'USER': 'root',
        'PASSWORD': '85276666'
    }
}
```
* 将MyBlog/Post/migrations中的迁移文件***除__init__.py***外全部删除
* >python manager.py makemigrations生成迁移文件
* >python manager.py migrate 根据迁移文件生成数据库文件