# hanblog

## 使用click的group 和subommand 实现命令行

```python
python manage.py --help
python manage.py initdb
```

### initdb中数据库models的配置

models都定义在单文件的models中的时候使用 `modules={"models": ["models"]}`

```python
async def init(create_db):
    await Tortoise.init(
        db_url=DB_URL,
        modules={'models': ['models.base', 'models.blog', 'models.comments', 'models.react']},
        _create_db=create_db
    )
```

### ipython中测试

ipython中直接使用await获取数据
不使用await获取到的是一个对象
```python
In [4]: from models.blog import Post
In [6]: from ext import init
In [7]: await init(False)
In [8]: await Post.all()
Out[8]: []
In [9]: Post.all()
Out[9]: <tortoise.queryset.QuerySet at 0x1f5ea1f38b0>
```