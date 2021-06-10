from django.urls import path
from register import views
urlpatterns = [
    path('signup/',views.signup,name='signup'),
    path('login/',views.login,name='login'),
    path('logout',views.logout,name='logout'),
    path('passwordreset',views.passreset,name='passreset'),
    path('login/login',views.login),
    path('signup/signup',views.signup),
    path('activate/<uidb64>/<token>',views.activate,name='activate')
]