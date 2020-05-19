Django

![Django](/Users/bruce/Desktop/5月份授课/DRF/Django.jpg)

DRF

![DRF](/Users/bruce/Desktop/5月份授课/DRF/DRF.jpg)

## 一、概述

1. 前后端分离

   ​	前端和后端通过Ajax技术进行通讯，后端只管API的开发

2. DRF（Django Rest Framework）（django-rest-framework.org）

   从models取出数据到views，views处理后到前端

   从models取出数据，先经过序列化操作，然后再传入views

3. 部署

   客户端  <—>  nginx（80）<—> socket(8000) <—> uwsgi  <—>  Django

   客户端  <—>  nginx（80）<—> socket(8000) <—> uwsgi  <—>  DRF —>  vue.js

4. 找出以前项目中的Ajax代码，请求DRF的API

5. 跨域错误：已拦截跨源请求：同源策略禁止读取位于 http://127.0.0.1:8000/users/ 的远程资源。（原因：CORS 头缺少 'Access-Control-Allow-Origin'）

6. 解决跨域错误：django-cors-headers



##  二、序列化

1. 创建序列化类

2. 使用序列化类，在django shell中序列化单个实例

   ```python
   from unicomapp.models import Snippet
   from unicomapp.serializers import SnippetSerializers
   from rest_framework.renders import JSONRenderer
   from rest_framework.parsers import JSONParser
   
   # 插入两条数据
   snippet = Snippet(code='foo = "bar"\n')
   snippet.save()
   snippet = Snippet(code='print = "hello,world"\n')
   snippet.save()
   
   
   #序列化的单个实例
   serializer = SnippetSerializers(snippet)
   serializer.data
   # {'id': 2, 'title': '', 'code': 'print = "hello,world"\n', 'linenos': False, 'language': 'python', 'style': 'friendly'}
   
   
   # 将模型实例转换为Python原生数据类型，要完成序列化过程，我们将数据转换成json
   content = JSONRenderer().render(serializer.data)
   content
   # b'{"id":2,"title":"","code":"print = \\"hello,world\\"\\n","linenos":false,"language":"python","style":"friendly"}'
   
   # 反序列化
   # 第一步 使用流（stream）解析为Python原生的数据类型
   #from django.uitls.six import BytesIO
   from io import BytesIO
   stream = BytesIO(content)
   data = JSONParser().parse(stream)
   # 第二步 将Python原生数据类型恢复成正常的对象实例
   serializer = SnippetSerializers(data=data)
   serializer.is_valid()
   # True
   serializer.validated_data
   # OrderedDict([('title', ''), ('code', 'print = "hello,world"'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])
   serializer.save()
   # <Snippet: Snippet object (3)>
   ```

   

3. 还可以序列化查询结果集（querysets）,只需要给serializer 添加一个many=True标记

   ```python
   >>> serializer = SnippetSerializers(Snippet.objects.all(),many=True)
   >>> serializer.data
   [OrderedDict([('id', 1), ('title', ''), ('code', 'foo = "bar"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 2), ('title', ''), ('code', 'print = "hello,world"\n'), ('linenos', False), ('language', 'python'), ('style', 'friendly')]), OrderedDict([('id', 3), ('title', ''), ('code', 'print = "hello,world"'), ('linenos', False), ('language', 'python'), ('style', 'friendly')])]
   >>> 
   ```

   

4. 使用ModelSerializers（简化的写法）

   SnippetSerializers 类中重复了很多包含在Snippet模型类中的信息，可以使用ModelSerializers进行简化，就跟Django提供了Form类和ModelForm类一样

   DRF 包含 Serializer 类和 ModelSerializer

   做了两件事情：

   （1） 一组自动确定的字段

   （2）默认简单实现了create()和 update()方法

   

## 三、问题积累

1. python shell，flask shell和django shell有什么区别

   命令：python，flask，python manage.py shell

   区别：后两个shell中有上下文的环境





































