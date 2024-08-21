from django.contrib import admin
from django.urls import path
from mysqlcrud import views

urlpatterns = [
    path('admin/', admin.site.urls),    #http://localhost/phpmyadmin/
    path('',views.home,name='Home'),
    path('insert/',views.insert),
    path('update/<int:id>',views.update),
]
