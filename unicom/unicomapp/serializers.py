# 用来做数据表示
from django.contrib.auth.models import User,Group
from .models import Snippet,LEXERS,LANGUAGE_CHOICES,STYLE_CHOICES
from rest_framework import serializers


# class UserSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url','username','email','groups')
#
# class GroupSerializers(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url','name')

# class SnippetSerializers(serializers.Serializer):
#     '''
#         serializers  序列化器类
#     '''
#     id = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False,allow_blank=True,max_length=100)
#     code = serializers.CharField(style={'base_template':'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         '''
#         根据提供的验证过得数据创建并返回一个新的 Snippet 实例
#         '''
#         return Snippet.objects.create(**validated_data)
#     def update(self, instance, validated_data):
#         '''
#             根据提供的验证过得数据更新和返回一个已经存在的 Snippet 实例
#         '''
#         instance.title = validated_data.get('title',instance.title)
#         instance.code = validated_data.get('code',instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance


class SnippetSerializers(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ('id','title','code','linenos','language','style')