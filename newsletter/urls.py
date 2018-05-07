from django.conf.urls import url
from accounts import views

urlpatterns = [

    url(r'^newsletter/$', views.login_and_signup, name='login_and_signup'),

]
