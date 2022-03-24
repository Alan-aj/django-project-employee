from django.urls.conf import include
from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('register',views.register),
    path('login',views.login,name="login"),
    path('admin',views.admin,name="admin_home"),
    path('employee',views.employee,name="employee_home"),
    path('update/<int:id>',views.update),
    path('logout',views.logout,name="logout"),
]