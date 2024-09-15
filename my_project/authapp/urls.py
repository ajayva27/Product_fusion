from django.urls import path
from .views import SignUpView, SignInView,home_view

urlpatterns = [
    path('', home_view, name='home'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('signin/', SignInView.as_view(), name='signin'),
]
