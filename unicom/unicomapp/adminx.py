import xadmin

#引入xadmin 里面的视图
from xadmin import views

from .models import User


class BaseSetting(object):
    '''
    xadim 的基础配置
    '''
    enabel_themes = True  #用来开启主题的功能

    use_bootswatch = True

class GlobalSettings(object):
    '''
    设置网站的标题和网页
    '''

    site_title = "1903c"
    site_footer = "1903c - powrd 2020"



#注册
xadmin.site.register(views.BaseAdminView,BaseSetting)
xadmin.site.register(views.CommAdminView,GlobalSettings)



#pyt
class UserAdmin(object):
    '''
    后台展示那些内容
    搜索那些内容
    后台过滤器使用那些内容
    '''
    list_display = ['name','email','message']
    search_fields = ['name','email','message']
    list_filter = ['name','email','message','craete_at']

xadmin.site.register(User,UserAdmin)