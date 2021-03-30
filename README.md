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

### 前端项目UIKit

UIKit使用webpack打包 https://getuikit.com/docs/webpack

webpack.config.js中指定了src下面的js文件作为webpack打包的原始js文件

#### 使用yarn安装依赖

```yarn install ```

会在项目目录生成node_modules文件

#### dev 开发模式

```yarn run start``` 

会在static/dist下生成打包的文件


#### templates

在模板中使用Mako的语法
```angular2html
<%inherit file="base.html" />  # base.html作为模板使用，注意路径
<%def name="bottom_script()">  # 定义该模板的函数名字为bottom_script
    # url_for 会拼接路径
    <script src="${ app.url_for('static', filename='dist/admin/base.js') }"></script>
</%def>
```

在body中引入并使用
```html
${ self.bottom_script() }
```

最后执行的脚本
```angular2html

<%def name="bottom_script()">
</%def>
```