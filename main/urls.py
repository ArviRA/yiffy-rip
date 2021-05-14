
from . import views
from django.urls import path

# Create your views here.


urlpatterns = [path("",views.home,name="home"),
path('send_name',views.rip,name="rip")]