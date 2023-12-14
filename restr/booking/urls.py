from django.urls import path
from . import views
from .views import SignUpView

urlpatterns = [path('index.html/',views.index,name='index'),
               path('',views.index,name='index'),
               path("accounts/signup/", SignUpView.as_view(), name="signup"),
            ]