from django.urls import path
from accounts import views
from . import views

urlpatterns = [
    path('signup/', views.SignUpView.as_view(), name='signup'),
]
