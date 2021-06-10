from django.urls import path,re_path
from . import views
urlpatterns = [
#    path('',views.detail,name='detail'),
    path('about/',views.about,name='about'),
    path('blog/',views.blog,name='blog'),
    path('search/',views.search,name='search'),
    re_path('cropsinland/(?P<offset>[a-zA-Z0-9]+)',views.cropsinland),
    #re_path('(?P<offset>\d{0,4})/$',views.crop_detail)
    re_path('crop/(?P<offset>\d{0,4})/$',views.crop_detail),
    re_path('land/(?P<offset>\d{0,4})/$',views.land_detail)
]