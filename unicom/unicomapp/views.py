# from django.contrib.auth.models import User,Group
# from rest_framework import viewsets
# from unicomapp.serializers import UserSerializers,GroupSerializers
#
#
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from unicomapp.models import  Snippet
# from unicomapp.serializers import SnippetSerializers


# class UserViewSet(viewsets.ModelViewSet):
#     '''
#        允许用户查看或者编辑的API路径
#     '''
#     queryset = User.objects.all()
#     serializer_class = UserSerializers
#
# class GroupViewSet(viewsets.ModelViewSet):
#     queryset = Group.objects.all()
#     serializer_class = GroupSerializers


# class JSONResponse(HttpResponse):
#     '''
#         把数据渲染成json格式，返回一个HttpResponse
#     '''
#     def __init__(self,data,**kwargs):
#         content = JSONRenderer().render(data)
#         # 数据格式不止json一种，xml
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse,self).__init__(content,**kwargs)

# 增删改查
# API 的根视图支持列出所有的snippet或者创建一个新的snippet
# csrf_exempt  不具有CSRF令牌的客户端对此视图进行POST也是被允许的
# @csrf_exempt
# def snippet_list(request):
#     '''
#         查询所有和插入一条数据
#     '''
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializers(snippets,many=True)
#         return JSONResponse(serializer.data)
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializers(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data,status=201)
#     return JSONResponse(serializer.errors,status=400)
#
# @csrf_exempt
# def snippet_detail(request,pk):
#     '''
#         获取筛选数据，更新单个操作，和删除单个操作
#     '''
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#     if request.method == 'GET':
#         serializer = SnippetSerializers(snippet)
#         return JSONResponse(serializer.data)
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializers(snippet,data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors,status=400)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)

'''
    基于函数视图的请求和响应
'''

# from rest_framework import status
# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from unicomapp.models import Snippet
# from unicomapp.serializers import SnippetSerializers
#
# @api_view(['GET','POST'])
# def snippet_list(request,format=None):
#     '''
#         查询所有
#     '''
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializers(snippets, many=True)
#         return Response(serializer.data)
#     elif request.method == 'POST':
#         serializer = SnippetSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#     return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#
# @api_view(['GET','PUT','DELETE'])
# def snippet_detail(request,pk,format=None):
#     '''
#         获取筛选数据，更新单个操作，和删除单个操作
#     '''
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#     if request.method == 'GET':
#         serializer = SnippetSerializers(snippet)
#         return Response(serializer.data)
#     elif request.method == 'PUT':
#         # data = JSONParser().parse(request)
#         serializer = SnippetSerializers(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

'''
    基于类的视图的请求和响应
'''
# import os
# import django
# os.environ.setdefault('DJANGO_SETTINGS_MODULE','unicom.settings')
# django.setup()
#
# from unicomapp.models import Snippet
# from unicomapp.serializers import SnippetSerializers
# from django.http import Http404
#
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status
#
# class SnippetList(APIView):
#
#     # 查询
#     def get(self,request,format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializers(snippets,many=True)
#         return Response(serializer.data)
#     # 添加
#     def post(self,request,format=None):
#         serializer = SnippetSerializers(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data,status=status.HTTP_201_CREATED)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
# class SnippetDetail(APIView):
#
#     def get_object(self,pk):
#         try:
#             snippet = Snippet.objects.get(pk=pk)
#             return snippet
#         except Snippet.DoesNotExist:
#             raise Http404
#     # 检索
#     def get(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializers(snippet)
#         return Response(serializer.data)
#     # 更新
#     def put(self,request,pk,format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializers(snippet,data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
#
#     # 删除
#     def delete(self, request,pk,format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


'''
   通过使用mixins类编写视图
'''
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE','unicom.settings')
django.setup()


from unicomapp.models import Snippet
from unicomapp.serializers import SnippetSerializers

from rest_framework import mixins
from rest_framework import generics

class SnippetList(mixins.ListModelMixin,mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializers

    def get(self,request,*args,**kwargs):
        return self.list(request,*args,**kwargs)
    def post(self,request,*args,**kwargs):
        return self.create(request,*args,**kwargs)

class SnippetsDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializers

    def get(self,request,*args,**kwargs):
        return self.retrieve(request,*args,**kwargs)
    def put(self,request,*args,**kwargs):
        return self.update(request,*args,**kwargs)
    def delete(self,request,*args,**kwargs):
        return self.destroy(request,*args,**kwargs)























