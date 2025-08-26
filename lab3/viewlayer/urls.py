from django.urls import path

from . import views
app_name ="viewlayer"
urlpatterns = [
#CONFurl
    path('', views.home, name='home'),       # http://127.0.0.1:8000/
    path('about/', views.about, name='about'), # http://127.0.0.1:8000/about/


    #URL động (có tham số)
    path('articles/<int:year>/', views.year_archive, name='year-archive'), #/articles/2024/
    path('articles/<int:year>/<int:month>/', views.month_archive, name='month-archive'), #/articles/2024/08/


    #converters vs slug
    path('article/<int:year>/<slug:slug>/', views.article_detail, name='article-detail'),


#VIEWFUNC
    #basic
    path('time/', views.current_datetime, name='time'),
    #response error
    path('myview/', views.my_view, name='view'),#/myview/?x=1
    #http404
    path('detail/', views.my_view, name='detail'),#/detail/?x=1
]