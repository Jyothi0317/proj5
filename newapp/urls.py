from django.urls import path
from newapp import views
app_name="newapp"

urlpatterns = [
    path('',views.index,name='index'),
    path('home',views.home,name="home"),
    path('child/',views.child,name="child"),
]
    