from django.urls import path,re_path
from . import views
urlpatterns = [
    path('',views.profile,name='userprofile'),
    path('picupload',views.profilepic,name='profilepic'),
    path('landcropdetail',views.landcropdetail,name='landcropdetail'),
    #re_path('(?P<offset>\d{0,4})/$',
    # views.crop_detail)   landcropdetail
]



