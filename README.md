# hanblog
## 环境

python3.7.1

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

使用models统一管理,在__init__ 中处理,
```python
from .blog import Post, Tag, PostTag
from .comment import Comment
from .react import ReactItem
```

相应的配置可以改写为models, 后期models中引用可以直接导入
```python
async def init(create_db):
    await Tortoise.init(
        db_url=DB_URL,
        modules={'models': ['models']},
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